import os
import sys
from flask import Flask, jsonify, request

from department_app.models.department_model import Departments, DepartmentsSchema
from department_app.models.employee_model import Employees, EmployeesSchema
from department_app.service.validation import validate_employee_data

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db, app

employees_schema = EmployeesSchema(many=True)
employee_schema = EmployeesSchema(many=False)


#add new employee
@app.route("/api/employees", methods = ['POST'])
def api_add_employees():
    try:
        new_emp = Employees(emp_name = request.json['emp_name'], emp_db = request.json['emp_db'], emp_salary = request.json['emp_salary'], emp_department = request.json['emp_department'])
        validation = validate_employee_data(new_emp.emp_name, new_emp.emp_db, new_emp.emp_salary, new_emp.emp_department)
        if validation[0]:
            db.session.add(new_emp)
            db.session.commit()
        else:
            return jsonify({"Error": f"Invalid {validation[1]}"})
        return employee_schema.jsonify(new_emp)
    except Exception as e:
        return jsonify({"Error": "Invalid data"})


#get list of employees
@app.route("/api/employees", methods = ['GET'])
def api_get_employees():
    employees = Employees.query.all()
    result_set = employees_schema.dump(employees)
    return jsonify(result_set)


#edit employee
@app.route("/api/employees/edit/<int:emp_id>", methods = ['PUT'])
def api_edit_employee(emp_id):
    
    employee = Employees.query.get_or_404(emp_id)
    employee.emp_name = request.json['emp_name']
    employee.emp_db = request.json['emp_db']
    employee.emp_salary = request.json['emp_salary']
    employee.emp_department = request.json['emp_department']

    validation = validate_employee_data(employee.emp_name, employee.emp_db, employee.emp_salary, employee.emp_department)
    if validation[0]:
        db.session.commit()
    else:
        return jsonify({"Error": f"Invalid {validation[1]}"})
    
    return jsonify(employees_schema.dump(Employees.query.all()))

#delete employee
@app.route("/api/employees/delete/<int:emp_id>", methods=['DELETE'])
def api_delete_employee(emp_id):
    employee = Employees.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify(employees_schema.dump(Employees.query.all()))
