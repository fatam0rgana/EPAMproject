import http

from department_app import app
from .base_test import BaseTestCase


class TestBaseView(BaseTestCase):

    def test_homepage(self):
        """
        
        Testing home_page accessibility

        """
        client = app.test_client()
        response1 = client.get('/')
        assert response1.status_code == http.HTTPStatus.OK