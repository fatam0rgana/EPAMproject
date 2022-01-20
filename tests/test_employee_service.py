import os
import sys
from department_app import app, db
from .base_test import BaseTestCase

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app.models.employee_model import Employees
from department_app.service.department_service import add_department_func
from department_app.service.employee_service import add_employee_func, edit_employee_func, delete_employee_func


class TestEmployeeService(BaseTestCase):

    def test_employee_add_func(self):
        """
        Testing add function
        """
        add_department_func('QA', 'qwe')
        add_employee_func('qwerty', '2000-01-01', 1000, 'QA')
        self.assertEqual(1, Employees.query.count())
    
    def test_employee_delete_func(self):
        """
        Testing delete function
        """
        add_department_func('QA', 'qwe')
        add_employee_func('qwerty', '2000-01-01', 1000, 'QA')
        delete_employee_func(1)
        self.assertEqual(0, Employees.query.count())
    
    def test_employee_edit_func(self):
        """
        Testing edit function
        """
        add_department_func('First dep', 'description')
        add_department_func('Second dep', 'description')
        add_employee_func('Petya', '2000-01-01', 1000, 'First dep')
        edit_employee_func(1, 'Kolya', '2001-01-01', 1200, 'Second dep')
        employee = Employees.query.get(1)
        self.assertEqual('Kolya', employee.emp_name)
        self.assertEqual('2001-01-01', employee.emp_db)
        self.assertEqual(1200, employee.emp_salary)
        self.assertEqual('Second dep', employee.emp_department)
