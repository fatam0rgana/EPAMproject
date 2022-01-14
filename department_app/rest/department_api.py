import os
import sys
from flask import Flask, jsonify, request

from department_app.models.department_model import Departments, DepartmentsSchema
from department_app.models.employee_model import Employees, EmployeesSchema


sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db, app

departments_schema = DepartmentsSchema(many=True)
department_schema = DepartmentsSchema(many=False)


#add new department
@app.route("/api/departments", methods = ['POST'])
def api_add_departments():
    try:
        new_dep = Departments(dep_name = request.json['dep_name'], dep_description = request.json['dep_description'])
        db.session.add(new_dep)
        db.session.commit()

        return department_schema.jsonify(new_dep)

    except Exception as e:
        return jsonify({"Error": "Invalid data"})


#get list of departments
@app.route("/api/departments", methods = ['GET'])
def api_get_departments():
    departments = Departments.query.all()
    result_set = departments_schema.dump(departments)
    return jsonify(result_set)


#edit existing department
@app.route("/api/departments/edit/<int:dep_id>", methods = ['PUT'])
def api_edit_department(dep_id):
    
    department = Departments.query.get_or_404(dep_id)
    employees_in_dep = Employees.query.filter_by(emp_department = department.dep_name)

    department.dep_name = request.json['dep_name']
    department.dep_description = request.json['dep_description']

    for employee in employees_in_dep:
            employee.emp_department = department.dep_name
    
    db.session.commit()

    return jsonify(departments_schema.dump(Departments.query.all()))
