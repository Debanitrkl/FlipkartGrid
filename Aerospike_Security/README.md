# FlipkartGrid (Team Ignitors - Fashion Intelligence)
There are two parts in this folder`Java Spring Boot Cron Job for regular deletion of Expired Styles` ; `Storing Data in Aerospike Database in Protobytes Format`:
 * [**Spring Boot Cron Job**](https://github.com/Debanitrkl/FlipkartGrid/tree/master/Aerospike_Security/spring-boot-aerospike-example-master)
 
  **Steps to install Aerospike & Register the scripts:-**
 1. Install Aerospike
 2. Install Lua 5.1
 3. Install Protobuf
 4. Start Aerospike Server by typing `systemctl start Aerospike` & enter the Aerospike terminal by entering `aql`
 5. Enter `register module 'grid_pb.lua'` & `register module 'script.lua'` & `register module 'pbuf.lua'`
 
Moving on to Running the Cron Job.

Open this Folder as a project in Eclipse or Intellij and run the `SpringBootAerospikeExampleApplication.java` as a SpringBoot Application.

**Requirements**:-
* Aerospike 
* Lua 5.1
* Luarocks
* protobuf
* Eclipse/Intellij IDE
* Oracle Java 11.0.8jdk 
