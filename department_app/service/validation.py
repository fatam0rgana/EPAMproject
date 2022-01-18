import datetime
import re
import os
import sys

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app.service.common_funcs import get_all_deps


def validate_employee_data(name, date, salary, department):
    name_pattern = re.compile(r"^[a-z]+$", re.I)
    if not name_pattern.match(name):
        return 0, 'name, name must omly include letters'
    if department not in get_all_deps():
        return 0, 'department, choose existing department name'
    if int(salary) < 300 and int(salary) > 10000 and int(salary) % 50 != 0:
        return 0, 'salary, salary must be between 300 and 10000 and a multiple of 50'
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except:
        return 0, 'date, date must be in the format "%Y-%m-%d"'
    return 1, 'data validated'



def validate_department_data(name, description):
    name_pattern = re.compile(r"^[a-z]+$", re.I)
    descr_pattern = re.compile("^(?!.*~#@'\"%$)(.*)$")
    if not name_pattern.match(name):
        return 0, 'name, name must only include letters'
    if not descr_pattern.match(description):
        return 0, 'description, contsins invalid symbols'
    return 1, 'data validated'

        
    