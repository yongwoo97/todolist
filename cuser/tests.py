from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APITestCase

class CustomUserTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='coninggu@example.com',
            #name='coninggu',
            password='testpassword12!@#'
        )
        self.assertEqual(user.username, 'coninggu@example.com')
        #self.assertEqual(user.name, 'coninggu')
        self.assertFalse(user.is_admin)
        self.assertTrue(user.is_active)

    def test_crete_superuser(self):
        user = get_user_model().objects.create_superuser(
            username='superuser@example.com',
            #name='superuser',
            password='testpassword12!@#'
        )
        self.assertEqual(user.username, 'superuser@example.com')
        #self.assertEqual(user.name, 'superuser')
        self.assertTrue(user.is_admin)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)

class TestRegister(APITestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/register/"

    def test_post_user_data(self):
        self.user_data = {
            "username": "woo22661@naver.com",
            "password": "Fuckchina2@"
        }
        self.client.post(self.url, data=self.user_data)

class TestLogin(APITestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/login/"
        self.register_url = "http://127.0.0.1:8000/api/register/"
    def test_post_login(self):
        self.user_data = {
            "username": "woo22661@naver.com",
            "password": "Fuckchina2@"
        }
        self.client.post(self.register_url, data=self.user_data)
        self.access_token = self.client.post(self.url,
                                            {"username": self.user_data.get("username"),
                                            "password": self.user_data.get("password"), },
                                            ).json()['token']

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")