import os
from re import template
import sys
from flask import render_template, url_for, flash, request
import datetime

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees

menu = [{'name': 'Departments', 'url': 'departments', 'status': ''}, {'name': 'Employees', 'url': 'employees', 'status': 'active'}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]

def count_age(emp):
    temp = datetime.datetime.strptime(Employees.query.filter_by(id = emp).first().emp_db, "%Y-%m-%d")
    today = datetime.date.today()
    return today.year - temp.year - ((today.month, today.day) < (temp.month, temp.day)) 



@app.route("/employees")
def employees():
    age = {elem.id: count_age(elem.id) for elem in Employees.query.all()}
    return render_template('employees.html', all_emps = Employees.query.all(), age = age, menu = menu, dropdown = dropdown, title = 'Employees')
