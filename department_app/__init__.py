from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#setting configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = "adnjkfvfdankvfadkb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql/department.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#creating db
db = SQLAlchemy(app)

from .views import homepage_view, employees_view, add_employee_view, add_department_view, departments_view