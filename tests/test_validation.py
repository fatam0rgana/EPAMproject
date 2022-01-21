import os
import sys

from department_app import app, db
from tests.base_test import BaseTestCase
from department_app.models.employee_model import Employees
from department_app.service.department_service import add_department_func
from department_app.service.validation import *


class TestValidation(BaseTestCase):

    def test_employee_valid(self):
        """
        Testing validation of employee data
        """
        add_department_func('First', '')
        self.assertEqual((1, 'data validated'), validate_employee_data('Petya', '2000-01-01', 1200, 'First'))
        self.assertEqual((0, 'name, name must only include letters'), validate_employee_data('Pe/ty@', '2000-01-01', 1200, 'First'))
        self.assertEqual((0, 'date, date must be in the format "%Y-%m-%d"'), validate_employee_data('Petya', '20000101', 1200, 'First'))
        self.assertEqual((0, 'salary, salary must be between 300 and 10000 and a multiple of 50'), validate_employee_data('Petya', '2000-01-01', 1210, 'First'))
        self.assertEqual((0, 'department, choose existing department name'), validate_employee_data('Petya', '2000-01-01', 1200, 'F1rst'))

    
    def test_department_valid(self):
        """
        Testing validation of department data
        """
        self.assertEqual((1, 'data validated'), validate_department_data('QA', 'Testing department'))
        self.assertEqual((0, 'name, name must only include letters'), validate_department_data("Q@", 'Testing department'))
        self.assertEqual((0, 'description, description contains invalid symbols'), validate_department_data('QA', 'Testing dep@rtment'))