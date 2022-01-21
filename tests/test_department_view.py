import http
from urllib import response

from department_app import app, db
from tests.base_test import BaseTestCase
from department_app.models.department_model import Departments
from department_app.service.department_service import add_department_func


class TestDepartmentView(BaseTestCase):
    """
    This is the class for departments view test case
    """

    def test_department_page(self):
        """

        Testing /departments page 
        
        """
        client = app.test_client()
        response1 = client.get('/departments')
        assert response1.status_code == http.HTTPStatus.OK
    

    def test_department_edit(self):
        """
        Testing department edit function
        """

        client = app.test_client()
        test_dep = Departments(dep_name = 'test', dep_description = 'qwe')
        db.session.add(test_dep)
        db.session.commit()
        response1 = client.get('/departments/edit/1')
        assert response1.status_code == http.HTTPStatus.OK
        with self.assertRaises(Exception): client.get('/departments/edit/2')
        
    

    def test_department_delete(self):
        """
        Testing department deletion
        """

        client = app.test_client()
        test_dep = Departments(dep_name = 'test', dep_description = 'qwe')
        db.session.add(test_dep)
        db.session.commit()
        response1 = client.get('/departments/delete/1')
        assert response1.status_code == http.HTTPStatus.FOUND
        with self.assertRaises(Exception): client.get('/departments/delete/2')
    
    
    def test_department_add(self):
        """
        Test of department_add page
        """
        client = app.test_client()
        response1 = client.get('/add_department')
        assert response1.status_code == http.HTTPStatus.OK
