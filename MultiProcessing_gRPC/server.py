from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from concurrent import futures
import contextlib
import datetime
import logging
import math
import multiprocessing
import time
import socket
import sys

import grpc

# import the generated classes
import calculator
import grid_pb2
import grid_pb2_grpc
# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer

LOGGER = logging.getLogger(__name__)
ONE_DAY = datetime.timedelta(days=1)
PROCESS_COUNT = multiprocessing.cpu_count()
THREAD_CONCURRENCY = PROCESS_COUNT

class PredictorServicer(grid_pb2_grpc.Predictor):
    def Process(self, request, context):
        response = grid_pb2.Shop_Processed()
        a = calculator.function(request,context)
        response.Colour = request.Colour
        response.Discount = request.Discount
        response.Ratings_count = request.Ratings_count
        response.Price = request.Price
        response.Ratings = request.Ratings
        response.Score = a
        print(response)
        return response

def _wait_forever(server):
    try:
        while True:
            time.sleep(ONE_DAY.total_seconds())
    except KeyboardInterrupt:
        server.stop(None)

def _run_server(bind_address):
    """Start a server in a subprocess."""
    LOGGER.info('Starting new server.')
    options = (('grpc.so_reuseport', 1),)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=THREAD_CONCURRENCY,),options=options)
    grid_pb2_grpc.add_PredictorServicer_to_server(PredictorServicer(), server)
    server.add_insecure_port(bind_address)
    server.start()
    _wait_forever(server)

@contextlib.contextmanager
def _reserve_port():
    """Find and reserve a port for all subprocesses to use."""
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if(sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) == 0):
        raise RuntimeError("Failed to set SO_REUSEADDR.")
    sock.bind(('', 0))
    try:
        yield sock.getsockname()[1]
    finally:
        sock.close()


def main():
    with _reserve_port() as port:
        bind_address = 'localhost:{}'.format(port)
        LOGGER.info("Binding to '%s'", bind_address)
        sys.stdout.flush()
        workers = []
        for _ in range(PROCESS_COUNT):
            worker = multiprocessing.Process(target=_run_server,args=(bind_address,))
            worker.start()
            workers.append(worker)
        for worker in workers:
            worker.join()


if __name__ == '__main__':
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[PID %(process)d] %(message)s')
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
    main()
