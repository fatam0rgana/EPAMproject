import datetime
import os
import sys
import string

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app.service.common_funcs import get_all_deps


def validate_employee_data(name, date, salary, department):
    for letter in name:
        if letter not in string.ascii_letters and letter != ' ':
            return 0, 'name, name must only include letters'
    if department not in get_all_deps():
        return 0, 'department, choose existing department name'
    if int(salary) < 300 or int(salary) > 10000 or int(salary) % 50 != 0:
        return 0, 'salary, salary must be between 300 and 10000 and a multiple of 50'
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except:
        return 0, 'date, date must be in the format "%Y-%m-%d"'
    return 1, 'data validated'



def validate_department_data(name, description):
    permitted_symbols = '.,!&:; '
    for letter in name:
        if letter not in string.ascii_letters and letter != ' ':
            return 0, 'name, name must only include letters'
    for letter in description:
        if letter not in string.ascii_letters and letter not in permitted_symbols:
            return 0, 'description, description contains invalid symbols'
    return 1, 'data validated'

        
    