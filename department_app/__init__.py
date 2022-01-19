import department_app.config as config
import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


sys.path.append(os.path.abspath(os.path.join('..')))



#setting configuration
app = Flask(__name__)
app.config.from_object(config)


#creating db
db = SQLAlchemy(app)

from .views import homepage_view, employees_view, add_employee_view, add_department_view, departments_view

from .rest import department_api, employee_api