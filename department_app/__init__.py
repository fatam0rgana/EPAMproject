import logging
import os
import sys

import department_app.config as config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#setting configuration
app = Flask(__name__)
app.config.from_object(config)

#creating db
db = SQLAlchemy(app)

#Creating migrations
migrate = Migrate(app, db, directory = os.path.join('department_app', 'migrations'))

#Creating logger
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger = app.logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

w_logger = logging.getLogger('werkzeug')
w_logger.addHandler(file_handler)
w_logger.setLevel(logging.DEBUG)

from .views import homepage_view, employees_view, add_employee_view, add_department_view, departments_view
from .rest import department_api, employee_api