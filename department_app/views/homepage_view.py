import os
import sys
from flask import render_template, url_for, flash, request

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app import app, db

menu = [{'name': 'Departments', 'url': 'departments', 'status': ''}, {'name': 'Employees', 'url': 'employees', 'status': ''}]
dropdown = [{'name': 'Add department', 'url': 'add_department'}, {'name': 'Add employee', 'url': 'add_employee'}]

@app.route("/")
def index():
    return render_template('index.html', menu = menu, dropdown = dropdown, title = 'Homepage')