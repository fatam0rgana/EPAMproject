import os
import sys
from flask import render_template, url_for, flash, request, redirect

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments

menu = [{'name': 'Departments', 'url': 'departments', 'status': 'active'}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add department', 'url': 'add_employee'}]

def count_avg_and_amount(dep):
    res = Employees.query.filter_by(emp_department = dep)
    sals = [x.emp_salary for x in res]
    try:
        return sum(sals)/len(sals), len(sals)
    except: 
        return 'No employees in department', 0



@app.route("/departments")
def departments():
    salary_and_amount  = {elem.dep_name: count_avg_and_amount(elem.dep_name) for elem in Departments.query.all()}
    return render_template('departments.html', all_deps = Departments.query.all(), characteristics = salary_and_amount, menu = menu, dropdown = dropdown)


@app.route("/departments/delete/<dep_id>", methods = ['GET'])
def delete_department(dep_id):
    if request.method == 'GET':
        dep = Departments.query.filter_by(id = dep_id).first().dep_name
        if count_avg_and_amount(dep)[1]:
            flash(f'You have {count_avg_and_amount(dep)[1]} workers in the department. Please move or delete them.', 'alert-danger')
        else:    
            dep_todelete = Departments.query.get_or_404(dep_id)
            db.session.delete(dep_todelete)
            db.session.commit()
        return redirect(url_for('departments'))


@app.route("/departments/edit/<int:dep_id>", methods = ['POST', 'GET'])
def edit_department(dep_id):

    department = Departments.query.get_or_404(dep_id)
    default = [[department.dep_name, department.dep_description]]

    if request.method == 'POST':
        employees_in_dep = Employees.query.filter_by(emp_department = department.dep_name)
        department.dep_name = request.form['department_name'] 
        department.dep_description = request.form['department_description']
        
        for employee in employees_in_dep:
            employee.emp_department = department.dep_name
            
        db.session.commit()
        return redirect(url_for('departments'))
        
    return render_template('add_department.html', default = default, action = f'/departments/edit/{dep_id}', menu = menu, dropdown = dropdown, title = 'Edit department')