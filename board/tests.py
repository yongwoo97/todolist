from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
class TestBoard(APITestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/todolist/2022/05/"
        self.register_url = "http://127.0.0.1:8000/api/register/"
        self.user_data = {
            "username": "test@test.com",
            "password": '1234'
        }
        self.client.post(self.register_url,
                         {"username": self.user_data.get("username"),
                          "password": self.user_data.get("password"), },
                         )
        token = Token.objects.get(user__username='test@test.com')
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")


    def test_board(self):

        self.board_data = {
            "date": "2022-05-14 13:10:00",
            "title": "hello world1234",
            "repeat": 1
        }

        response = self.client.post(self.url, data=self.board_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('http://127.0.0.1:8000/api/todolist/2022/05/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



