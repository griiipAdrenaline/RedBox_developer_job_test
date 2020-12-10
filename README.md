# RedBox Developer Job Test
This test have two parts:
1. Docker task
1. Python classes task

## Docker task
The task is to create a simple TCP socket connection between two docker containers

### Requirements
* Use Python to create the Server and Client
* Use TCP Sockets to create the communication
* The Server and Client should be inside a Docker container
* Use docker-compose to define and run the application

### App definition
* The client should connect to the server and send a message once per second
* The Server should indicate it received a connection (using prints)
* The Server should print the messages it receives from the Client

### Bonus task
**_Make sure that both the Docker images are less than 100MB in size_**

## Python task

### Task definition
Create a class `Employee` that will take a full name as argument, as well as a set of none, one or more keywords.
Each instance should have a name and a lastname attributes plus one more attribute for each of the keywords, if any.

### Examples

```python
john = Employee("John Doe")    
mary = Employee("Mary Major", salary=120000)    
richard = Employee("Richard Roe", salary=110000, height=178)    
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
```

john.name :arrow_right: "John"    
mary.lastname :arrow_right: "Major"    
richard.height :arrow_right: 178    
giancarlo.nationality :arrow_right: "Italian"

**Notes:** First and last names will be separated by a whitespace. The test will not include any middle names or 
initials.
The value of the keywords can be an int, a str or a list.

## Submission
To submit the solution please create a `.zip` file with your name and send it to `alonk@griiip.com`