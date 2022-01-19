import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.department_model import Departments
from department_app.service.department_service import add_department_func

menu = [{'name': 'Departments', 'url': 'departments', 'status': 'active'}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]


@app.route("/add_department", methods = ['POST', 'GET'])
def add_department():
    default = [['', '']]
    if request.method == 'POST':
        try:
            add_department_func(request.form['department_name'], request.form['department_description'])
        except:
            db.session.rollback()
            flash('error', 'alert-danger')
    return render_template('add_department.html', default = default, action = '/add_department',menu = menu, dropdown = dropdown, title = 'Add department')