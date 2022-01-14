import os
import sys
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import db, app

ma = Marshmallow(app)

class Departments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dep_name = db.Column(db.String(50), nullable = False, unique = True)
    dep_description = db.Column(db.String(150))

    def __repr__(self):
        return self.id
    

class DepartmentsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'dep_name', 'dep_description')

department_schema = DepartmentsSchema(many=False)
departments_schema = DepartmentsSchema(many=True)