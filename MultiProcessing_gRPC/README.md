# FlipkartGrid (Team Ignitors - Fashion Intelligence)
This Repo features a **Multiprocessing gRPC Server**, able to handle Multiple Client requests and reduce network network traffic. Multiple Server instances are created which helps in handling multiple client requests at a time.

**No. of Server Instances = No .of CPU Processing Cores of the Machine**

**Running the Process**
* In terminal `systemctl start aerospike`

* In a Terminal, Run `python server.py`
  Something Like this shows up, This signifies that my CPU has 8 Cores and 8 server Instances are produced.
  ```
  [PID 4753] Binding to 'localhost:42263'
  [PID 4754] Starting new server.
  [PID 4755] Starting new server.
  [PID 4756] Starting new server.
  [PID 4757] Starting new server.
  [PID 4758] Starting new server.
  [PID 4759] Starting new server.
  [PID 4760] Starting new server.
  [PID 4761] Starting new server.
  ```
  
 In this Case, our Server Address is **localhost:42263**
  
 * In a new terminal, Run `python client.py -- server:address` in this case, `python client.py -- localhost:42263`
 
 We see Something Like this as Output:-
 ```
 No. of requests made =  10000
 Time taken for processing =  0.9854415225982666
 ```
 It can be seen that **Almost 10,000 client requests are processed in 1 second**, speed may vary upto some extent.
  
 **Requirements:-**
 * Python 3.6
 * gRPC Python (python grpcio tools)
 * Aerospike
 
 **References:-**
 * [Aerospike Installation](https://www.aerospike.com/docs/operations/install/)
 * [gRPC Python Installation](https://grpc.io/docs/languages/python/basics/)
