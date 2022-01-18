import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.department_model import Departments
from department_app.service.validation import validate_department_data

menu = [{'name': 'Departments', 'url': 'departments', 'status': 'active'}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]


@app.route("/add_department", methods = ['POST', 'GET'])
def add_department():
    default = [['', '']]
    if request.method == 'POST':
        try:
            new_dep = Departments(dep_name = request.form['department_name'], dep_description = request.form['department_description'])
            validation = validate_department_data(new_dep.dep_name, new_dep.dep_description)
            if validation[0]:
                db.session.add(new_dep)
                db.session.commit()
                flash(f"{request.form['department_name']} added", 'alert-success')
            else:
                db.session.rollback()
                flash(f'Error: Invalid {validation[1]}', 'alert-danger')
        except:
            db.session.rollback()
            flash('error', 'alert-danger')
    return render_template('add_department.html', default = default, action = '/add_department',menu = menu, dropdown = dropdown, title = 'Add department')