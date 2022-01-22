![Coveralls](https://img.shields.io/coveralls/github/fatam0rgana/EPAMproject) ![Travis (.com)](https://img.shields.io/travis/com/fatam0rgana/EPAMproject)

# Department App<a name="top"></a>

### Table of Contents
1. [Description](#description)
2. [How to install](#installation)
3. [Interface guide](#interface)
4. [Author info](#info)

---

## Description<a name="description"></a>
Department App is a simple web application for managing departments and employees. The user is allowed to:

1. Check the lists of departments with department name, description, number of employees and average salary columns. Number of employees and average salary are calculated automatically based on employees data;

2. Check the lists of employees with employee name, salary, age and department in which he works.

3. Perform operations with departments such as adding, editing, deleting

4. Perform operations with employees such as adding, editing, deleting

#### Structure:
* migrations - manages database schema changes
* models - DB models
* service - modules with functions to work with DB (CRUD operations)
* sql - *.sql files to work with DB
* rest - modules with RESTful service implementation
* templates - html templates
* static - *.js and *.css files, images
* tests - modules with unit tests
* views - modules with Web controllers / views

[Back to top](#top)
## How to install<a name="installation"></a>
1. Install Python (my version is 3.8.10)
  
2. Clone repository
  > git clone https://github.com/fatam0rgana/EPAMproject
3. Move to cloned repository
  > cd EPAMproject
4. Create and activate virtual environment
  > python3 -m venv env
   
  > source env/bin/activate
5. Install requirements
  > pip install -r requirements.txt
6. Init database
  > flask db init
7. After installation you can run app through console
  > python3 app.py

[Back to top](#top)
## Interface guide<a name="interface"></a>

#### After you completed these steps, you may see homepage of the application


![image](https://user-images.githubusercontent.com/45520098/150633853-81ac5b5d-48d2-488a-8fd0-144fe5d25a08.png)


#### Departments tab. Here you can see list of departments with all their data, edit and delete departments.


![image](https://user-images.githubusercontent.com/45520098/150633895-eabf346e-e7f8-4c3f-8e77-4e4ede5613c1.png)


#### Employees tab. Here you can see list of employees with all their data, edit and delete employees.


![image](https://user-images.githubusercontent.com/45520098/150633961-1c2a78b3-1fcc-4878-9382-8e88bc03144e.png)


#### Add department and employee tabs will help you to add new record to database. 


![image](https://user-images.githubusercontent.com/45520098/150633999-456e2796-5d10-4940-87bb-d1c7dde427a8.png)


![image](https://user-images.githubusercontent.com/45520098/150634010-6f30b387-9bb6-493c-a6c3-b61a270bce67.png)


#### Search button in the top-right corner will search for employee with entered string in his name.


![image](https://user-images.githubusercontent.com/45520098/150634063-6cf493da-0a31-42ae-8075-af495e7a9db6.png)


[Back to top](#top)
## Author info<a name="info"></a>


* Telegram - @FraunhoferDiffraction
* Email - pazon4ik@gmail.com


[Back to top](#top)
