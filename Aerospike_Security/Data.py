import aerospike

# Configure the client
config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
  print("Connected to Aerospike Cluster")
except:
  import sys
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)

list = [12,"Red", 5, 81, 1, 4.3, 8.2, 5]
key = ('test', 'demo', list[0])
client.apply(key, "pbuf", "put_data", [list[1], list[2], list[3], list[4], list[5], list[6], list[7]])
a= client.apply(key, "pbuf", "verify_data",[])
print(a)
