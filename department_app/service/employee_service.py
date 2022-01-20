import os
import sys
from flask import flash, request, redirect

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.service.validation import validate_employee_data
from department_app.models.employee_model import Employees


def add_employee_func(name, bd, salary, department):
    """
    Function adds new employee
    """
    try:
        new_emp = Employees(emp_name = name, emp_db = bd, emp_salary = salary, emp_department = department)
        validation = validate_employee_data(name, bd, salary, department)
        if validation[0]:
            db.session.add(new_emp)
            db.session.flush()
            db.session.commit()
            #flash(f"{request.form['employee_name']} added", 'alert-success')
        else:
            db.session.rollback()
            flash(f"Error: Invalid {validation[1]}", 'alert-danger')
    except:
        db.session.rollback()
        flash('Invalid data', 'alert-danger')

    
def delete_employee_func(id):
    """
    Function deletes employee
    """
    try:
        usr_todelete = Employees.query.get_or_404(id)
    except:
        raise Exception('Employee does not exist')
    db.session.delete(usr_todelete)
    db.session.commit()

def edit_employee_func(id, new_name, new_bd, new_salary, new_dep):
    try:
        employee = Employees.query.get_or_404(id)
    except:
        raise Exception('Employee does not exist')
    employee.emp_name = new_name 
    employee.emp_db = new_bd
    employee.emp_salary = new_salary
    employee.emp_department = new_dep
    validation = validate_employee_data(new_name, new_bd, new_salary, new_dep)
    if validation[0]:
        db.session.commit()
    else:
        flash(f"Error: Invalid {validation[1]}", 'alert-danger')