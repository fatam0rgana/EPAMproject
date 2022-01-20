import http
import json

from department_app import app, db
from .base_test import BaseTestCase
from department_app.models.employee_model import Employees
from department_app.models.department_model import Departments


class TestDepartmentApi(BaseTestCase):

    def test_get_employees_api(self):
        """
        Testing get_employees function
        """
        client = app.test_client()
        response = client.get('/api/employees')
        
        assert response.status_code == http.HTTPStatus.OK
    

    def test_add_employee_api(self):
        """
        Testing add_employee function
        """
        client = app.test_client()
        department = Departments(dep_name = 'test', dep_description = 'test')
        db.session.add(department)
        db.session.commit()
        data = {
                    "emp_name": "Sasha",
                    "emp_db": "1996-01-01",
                    "emp_salary": "1000",
                    "emp_department": "test"
                }
        response1 = client.post('/api/employees', data=json.dumps(data),
                               content_type='application/json')

        assert response1.status_code == http.HTTPStatus.OK
    

    def test_delete_employee_api(self):
        """
        Testing delete_employee function
        """
        client = app.test_client()
        department = Departments(dep_name = 'test', dep_description = 'test')
        employee = Employees(emp_name = "Sasha", emp_db = "1996-01-01", emp_salary = "1000", emp_department = "test")
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        response = client.delete('/api/employees/delete/1')

        assert response.status_code == http.HTTPStatus.OK
        self.assertEqual(None, Employees.query.first())
    

    def test_edit_employee_api(self):
        """
        Testing edit_employee function
        """
        client = app.test_client()
        department = Departments(dep_name = 'test', dep_description = 'test')
        employee = Employees(emp_name = "Sasha", emp_db = "1996-01-01", emp_salary = "1000", emp_department = "test")
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        data = {
                    "emp_name": "Vasya",
                    "emp_db": "1990-01-01",
                    "emp_salary": "1100",
                    "emp_department": "test"
                }
        response = client.put('/api/employees/edit/1', data=json.dumps(data),
                               content_type='application/json')
        
        assert response.status_code == http.HTTPStatus.OK
        self.assertEqual('Vasya', Employees.query.first().emp_name)