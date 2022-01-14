import os
import sys
from flask import Flask, jsonify, request

from department_app.models.department_model import Departments, DepartmentsSchema
from department_app.models.employee_model import Employees, EmployeesSchema


sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db, app

employees_schema = EmployeesSchema(many=True)


#add new employee
@app.route("/api/employees", methods = ['GET'])
def api_employees():
    employees = Employees.query.all()
    result_set = employees_schema.dump(employees)
    return jsonify(result_set)

