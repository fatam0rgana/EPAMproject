import os
import sys
from flask import flash, request, redirect

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.service.common_funcs import count_avg_and_amount
from department_app.service.validation import validate_department_data
from department_app.models.department_model import Departments
from department_app.models.employee_model import Employees

def add_department_func(name, description):
    """
    Function adds new department
    """
    try:
        new_dep = Departments(dep_name = name, dep_description = description)
        validation = validate_department_data(new_dep.dep_name, new_dep.dep_description)
        if validation[0]:
            db.session.add(new_dep)
            db.session.commit()
            #flash(f"{request.form['department_name']} added", 'alert-success')
        else:
            db.session.rollback()
            flash(f'Error: Invalid {validation[1]}', 'alert-danger')
    except:
        flash("Invalid data", 'alert-danger')


def edit_department_func(id, new_name, description):
    """
    Function edits existing department
    """
    department = Departments.query.get_or_404(id)
    employees_in_dep = Employees.query.filter_by(emp_department = department.dep_name)
    try:
        department.dep_name = new_name 
        department.dep_description = description
        validation = validate_department_data(new_name, description)
        if validation[0]:
            for employee in employees_in_dep:
                employee.emp_department = new_name
            db.session.commit()
        else:
            flash(f"Error: Invalid {validation[1]}", 'alert-danger')

    except:
        flash("Invalid data", 'alert-danger')
    

def delete_department_func(id):
    """
    Function deletes department
    """
    try:
        dep = Departments.query.filter_by(id = id).first().dep_name
    except:
        raise Exception('Department does not exist')
    if count_avg_and_amount(dep)[1]:
        flash(f'You have {count_avg_and_amount(dep)[1]} workers in the department. Please move or delete them.', 'alert-danger')
    else:    
        dep_todelete = Departments.query.get_or_404(id)
        db.session.delete(dep_todelete)
        db.session.commit()
  