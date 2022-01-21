import http
import json

from department_app import app, db
from tests.base_test import BaseTestCase
from department_app.models.department_model import Departments

class TestDepartmentApi(BaseTestCase):

    def test_get_departments_api(self):
        """
        Testing get_departments function
        """
        client = app.test_client()
        response = client.get('/api/departments')
        
        assert response.status_code == http.HTTPStatus.OK
    

    def test_add_department_api(self):
        """
        Testing add_department function
        """
        client = app.test_client()
        data1 = {
        "dep_name" : "Test",
        "dep_description": "test test"
        }    
        response1 = client.post('/api/departments', data=json.dumps(data1),
                               content_type='application/json')

        assert response1.status_code == http.HTTPStatus.OK


    def test_delete_department_api(self):
        """
        Testing delete_department function
        """
        client = app.test_client()
        department = Departments(dep_name = 'test', dep_description = 'test')
        db.session.add(department)
        db.session.commit()
        response = client.delete('/api/departments/delete/1')
        assert response.status_code == http.HTTPStatus.OK
        self.assertEqual(None, Departments.query.first())
    

    def test_department_edit_api(self):
        """
        Testing edit_department function
        """
        client = app.test_client()
        department = Departments(dep_name = 'test', dep_description = 'test')
        db.session.add(department)
        db.session.commit()
        data = {
            'dep_name': 'test update',
            'dep_description': 'test update'
        }
        response = client.put('/api/departments/edit/1', data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        self.assertEqual('test update', Departments.query.first().dep_name)