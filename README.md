# Rockstar G5 // Week 1 evaluation 💫

### About this project 

This repository is part of the evaluation of my first week learning @Enroute.
Consists of a Python app that allows you to read a CSV file as JSON, add a new entry dynamically (in this case, employees) and see a table with the updated results.

### Demo
   ![Demo](https://media2.giphy.com/media/lglsKxXZOfEKMQRofs/giphy.gif)
  - [Main Page (CSV to JSON) ](http://69.164.206.106:5050/).
  - [Add a new employee to the CSV file](http://69.164.206.106:5050/new_employee).
  - [See updated table with data from the CSV file](http://69.164.206.106:5050/employee_table).

### Requirements 
  - Python 3.
  - Docker.
  
### Instructions
  - Clone this repository 
  ```
    git clone https://github.com/keupa/evaluacion_rg5.git
  ```
  - Build the Docker image on the repository directory: 
  ```
    docker build -t evaluacionrg5_new .  
  ```
  - Run the image:
  ```
    docker run --name <container name> -d -p 5050:5050 -v $(pwd)/data/employees.csv:/usr/src/app/data/employees.csv evaluacionrg5_new
  ```
  - Stop the container:
  ```
  docker stop <container name>
  ```
  - Remove the container
  ```
  docker rm -f <container name>
  ```
  
-------------

Thanks to Javier Zepeda & the Enroute team :-) 
 
 
  
  


