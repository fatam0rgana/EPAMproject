import os
from re import template
import sys
from flask import render_template, url_for, flash, request, redirect
import datetime

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments


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


@app.route("/employees/delete/<emp_id>", methods = ['POST', 'GET'])
def delete_employee(emp_id):
    if request.method == 'GET':
        usr_todelete = Employees.query.get_or_404(emp_id)
        db.session.delete(usr_todelete)
        db.session.commit()
        return redirect(url_for('employees'))


@app.route("/employees/edit/<emp_id>", methods = ['POST', 'GET'])
def edit_employee(emp_id):
    employee = Employees.query.get_or_404(emp_id)
    default = [[employee.emp_name, employee.emp_salary, employee.emp_db]]
    if request.method == 'POST':
        employee.emp_name = request.form['employee_name'] 
        employee.emp_db = request.form['employee_age']
        employee.emp_salary = request.form['employee_salary']
        employee.emp_department = request.form['employee_department']
        db.session.commit()
        return redirect(url_for('employees'))
    return render_template('add_employee.html', action = f'/employees/edit/{emp_id}', default = default, all_deps = Departments.query.all(), menu = menu, dropdown = dropdown, title = 'Edit employee')
    