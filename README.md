# RedBox Developer Job Test

The task is to create a simple TCP socket connection between two docker containers

## Requirements
* Use Python to create the Server and Client
* Use TCP Sockets to create the communication
* The Server and Client should be inside a Docker container
* Use docker-compose to define and run the application

## App definition
* The client should connect to the server and send a message once per second
* The Server should indicate it received a connection (using prints)
* The Server should print the messages it receives from the Client

## Bonus task
**_Make sure that both the Docker images are less than 100MB in size_**