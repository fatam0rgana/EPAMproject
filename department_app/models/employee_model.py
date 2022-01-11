import os
import sys
from flask_sqlalchemy import SQLAlchemy

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(50), nullable = False)
    emp_db = db.Column(db.String, nullable = False)
    emp_salary = db.Column(db.Integer, nullable = False)
    emp_department = db.Column(db.String(50), nullable = False)