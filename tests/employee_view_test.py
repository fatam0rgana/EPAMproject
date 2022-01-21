import http

from department_app import app, db
from .base_test import BaseTestCase
from department_app.models.employee_model import Employees

class TestEmployeeView(BaseTestCase):
    """
    This is the class for departments view test case
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
        Testing employee edit page
        """

        client = app.test_client()
        test_emp = Employees(emp_name = 'test', emp_db = '2000-01-01', emp_salary = 1000, emp_department = 'QA')
        db.session.add(test_emp)
        db.session.commit()
        response1 = client.get('/employees/edit/1')
        assert response1.status_code == http.HTTPStatus.OK
        with self.assertRaises(Exception): client.get('/employees/delete/2')
    

    def test_employee_delete(self):
        """
        Testing employee deletion page
        """

        client = app.test_client()
        test_emp = Employees(emp_name = 'test', emp_db = '2000-01-01', emp_salary = 1000, emp_department = 'QA')
        db.session.add(test_emp)
        db.session.commit()
        response1 = client.get('/employees/delete/1')
        assert response1.status_code == http.HTTPStatus.FOUND
        with self.assertRaises(Exception): client.get('/employees/delete/2')
    

    def test_employee_add(self):
        """
        Testing /add_employee page
        """
        client = app.test_client()
        response1 = client.get('/add_employee')
        assert response1.status_code == http.HTTPStatus.OK
        
    
    def test_employee_search(self):
        """
        Testing search_employee page
        """
        client = app.test_client()
        response1 = client.post('/employees/search_by_name')
        print(response1)
        #Must return bad request because no search string presented
        assert response1.status_code == http.HTTPStatus.BAD_REQUEST

    
