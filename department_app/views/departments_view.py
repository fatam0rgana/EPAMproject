import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments

menu = [{'name': 'Departments', 'url': 'departments', 'status': 'active'}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]

def count_avg_and_amount(dep):
    res = Employees.query.filter_by(emp_department = dep)
    sals = [x.emp_salary for x in res]
    try:
        return sum(sals)/len(sals), len(sals)
    except: 
        return 'No employees in department', '0'



@app.route("/departments")
def departments():
    salary_and_amount  = {elem.dep_name: count_avg_and_amount(elem.dep_name) for elem in Departments.query.all()}
    return render_template('departments.html', all_deps = Departments.query.all(), characteristics = salary_and_amount, menu = menu, dropdown = dropdown)

