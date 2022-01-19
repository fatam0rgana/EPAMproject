import http
from urllib import response
from department_app import app, db
#from department_app.views.departments_view import 
from .base_test import BaseTestCase
from department_app.models.department_model import Departments
from department_app.service.department_service import add_department_func, delete_department_func, delete_department_func, edit_department_func

class TestDepartmentService(BaseTestCase):

    def test_department_add_func(self):
        """
        #Testing department add function
        """
        client = app.test_client()
        add_department_func('qwerty', 'qwerty')
        self.assertEqual(1, Departments.query.count())

    def test_department_delete_func(self):
        """
        Testing delete function
        """
        department = Departments(dep_name = 'name', dep_description = 'description')
        db.session.add(department)
        db.session.commit()
        delete_department_func(1)
        self.assertEqual(0, Departments.query.count())

    def test_department_edit_func(self):
        """
        Testing edit function
        """
        department = Departments(dep_name = 'name', dep_description = 'description')
        db.session.add(department)
        db.session.commit()
        edit_department_func(1, 'newname', 'new_description')
        department = Departments.query.get(1)
        self.assertEqual('newname', department.dep_name)
        self.assertEqual('new_description', department.dep_description)
        

