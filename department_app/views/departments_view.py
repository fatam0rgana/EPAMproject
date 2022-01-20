import os
import sys
from flask import render_template, url_for, flash, request, redirect

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments
from department_app.service.common_funcs import count_avg_and_amount
from department_app.service.department_service import delete_department_func, edit_department_func


menu = [{'name': 'Departments', 'url': 'departments', 'status': 'active'}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]


#Page of all departments
@app.route("/departments")
def departments():
    salary_and_amount  = {elem.dep_name: count_avg_and_amount(elem.dep_name) for elem in Departments.query.all()}
    print(salary_and_amount)
    return render_template('departments.html', all_deps = Departments.query.all(), characteristics = salary_and_amount, menu = menu, dropdown = dropdown)


#Deleting function
@app.route("/departments/delete/<dep_id>", methods = ['GET'])
def delete_department(dep_id):
    if request.method == 'GET':
        delete_department_func(dep_id)
        return redirect(url_for('departments'))


#Editing function
@app.route("/departments/edit/<int:dep_id>", methods = ['POST', 'GET'])
def edit_department(dep_id):
    try:
        department = Departments.query.get_or_404(dep_id)
    except:
        raise Exception('Department does not exist')
    default = [[department.dep_name, department.dep_description]]
    if request.method == 'POST':
        edit_department_func(dep_id, request.form['department_name'], request.form['department_description'])
        return redirect(url_for('departments'))
    return render_template('add_department.html', default = default, action = f'/departments/edit/{dep_id}', menu = menu, dropdown = dropdown, title = 'Edit department')