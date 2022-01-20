import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments
from department_app.service.validation import validate_employee_data
from department_app.service.employee_service import add_employee_func

menu = [{'name': 'Departments', 'url': 'departments', 'status': ''}, {'name': 'Employees', 'url': 'employees', 'status': 'active'}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]


@app.route("/add_employee", methods = ['POST', 'GET'])
def add_employee():
    default = [['', '', '2000-11-17']]
    
    if request.method == 'POST':
        add_employee_func(request.form['employee_name'], request.form['employee_age'], request.form['employee_salary'], request.form['employee_department'])
            
    return render_template('add_employee.html', action = '/add_employee', default = default, all_deps = Departments.query.all(), menu = menu, dropdown = dropdown, title = 'Add employee')
