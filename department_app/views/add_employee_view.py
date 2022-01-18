import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments
from department_app.service.validation import validate_employee_data

menu = [{'name': 'Departments', 'url': 'departments', 'status': ''}, {'name': 'Employees', 'url': 'employees', 'status': 'active'}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]


@app.route("/add_employee", methods = ['POST', 'GET'])
def add_employee():
    default = [['', '', '2000-11-17']]
    if request.method == 'POST':
        try:
            new_emp = Employees(emp_name = request.form['employee_name'], emp_db = request.form['employee_age'], emp_salary = request.form['employee_salary'], emp_department = request.form['employee_department'])
            validation = validate_employee_data(new_emp.emp_name, new_emp.emp_db, new_emp.emp_salary, new_emp.emp_department)
            if validation[0]:
                db.session.add(new_emp)
                db.session.flush()
                db.session.commit()
                flash(f"{request.form['employee_name']} added", 'alert-success')
            else:
                db.session.rollback()
                flash(f"Error: Invalid {validation[1]}", 'alert-danger')
        except:
            db.session.rollback()
            flash('Invalid data', 'alert-danger')
    return render_template('add_employee.html', action = '/add_employee', default = default, all_deps = Departments.query.all(), menu = menu, dropdown = dropdown, title = 'Add employee')
