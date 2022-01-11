import os
import sys
from flask_sqlalchemy import SQLAlchemy

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dep_name = db.Column(db.String(50), nullable = False, unique = True)
    dep_description = db.Column(db.String(150))
