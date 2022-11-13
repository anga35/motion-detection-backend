from rest_framework.test import APITestCase
from django.urls import reverse

# Create your tests here.
class BaseTestCase(APITestCase):

    def setUp(self) -> None:
        registeration_credentials={
            'email':'test@gmail.com',
            'fullname':'Test User',
            'password':'testuser123',
            'confirm_password':'testuser123'
        }
        url=reverse('create-user')
        response=self.client.post(url,data=registeration_credentials)
        url=reverse('login')
        login_credentials={
            'email':'test@gmail.com',
            'password':'testuser123'
        }
        response=self.client.post(url,data=login_credentials)
        self.token=f'Token {response.json()["access_token"]}'      



    def test_all_captures(self):
        url=reverse('all-captures')
        response=self.client.get(url,HTTP_AUTHORIZATION=self.token)
        print(response)
