import http

from department_app import app, db
from .base_test import BaseTestCase
from department_app.models.employee_model import Employees

class TestEmployeeView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_employee_page(self):
        """

        Testing /employees page 
        
        """
        client = app.test_client()
        response1 = client.get('/employees')
        assert response1.status_code == http.HTTPStatus.OK
    

    def test_employee_edit(self):
        """
        Testing employee edit function
        """

        client = app.test_client()
        test_emp = Employees(emp_name = 'test', emp_db = '2000-01-01', emp_salary = 1000, emp_department = 'QA')
        db.session.add(test_emp)
        db.session.commit()
        response1 = client.get('/employees/edit/1')
        response2 = client.get('/employees/edit/2')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.NOT_FOUND
    

    def test_employee_delete(self):
        """
        Testing employee deletion
        """

        client = app.test_client()
        test_emp = Employees(emp_name = 'test', emp_db = '2000-01-01', emp_salary = 1000, emp_department = 'QA')
        db.session.add(test_emp)
        db.session.commit()
        response1 = client.get('/employees/delete/1')
        response2 = client.get('/employees/delete/2')
        assert response1.status_code == http.HTTPStatus.FOUND
        assert response2.status_code == http.HTTPStatus.NOT_FOUND
