import os
import sys
from department_app import app, db
from .base_test import BaseTestCase

sys.path.append(os.path.abspath(os.path.join('..')))

from department_app.service.department_service import add_department_func
from department_app.service.employee_service import add_employee_func
from department_app.service.common_funcs import count_age, count_avg_and_amount, get_all_deps


class TestCommonFuncs(BaseTestCase):

    def test_count_avg(self):
        """
        Testing 'count_avg_and_amount' function
        """
        add_department_func('First', '')
        add_department_func('Second', '')
        add_employee_func('Vanya', '2000-01-01', 1000, 'First')
        add_employee_func('Vasya', '1999-01-01', 1500, 'First')
        self.assertEqual((1250.0, 2), count_avg_and_amount('First'))
        self.assertEqual(('No employees in department', 0), count_avg_and_amount('Second'))
    

    def test_count_age(self):
        """
        Testing 'count_age' function
        """
        add_department_func('First', '')
        add_employee_func('Vanya', '2000-01-01', 1000, 'First')
        add_employee_func('Vasya', '1999-01-01', 1500, 'First')
        self.assertEqual(22, count_age(1))
        self.assertEqual(23, count_age(2))

    
    def test_get_deps(self):
        """
        Testing 'get_all_deps' function
        """
        add_department_func('First', '')
        add_department_func('Second', '')
        self.assertEqual(['First', 'Second'], get_all_deps())