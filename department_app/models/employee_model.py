import os
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db, app

ma = Marshmallow(app)

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(50), nullable = False)
    emp_db = db.Column(db.String, nullable = False)
    emp_salary = db.Column(db.Integer, nullable = False)
    emp_department = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return self.id

class EmployeesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'emp_name', 'emp_db', 'emp_salary', 'emp_department')

employee_schema = EmployeesSchema(many=False)
employees_schema = EmployeesSchema(many=True)