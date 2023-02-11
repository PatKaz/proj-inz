from django.test import TestCase,Client
from django.urls import reverse 
from django.core import mail
from django.core.mail import send_mail
from django.contrib.auth.models import User

class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'telephone': '1234567890',
            'content': 'Test message'
        }
    def test_mail(self):
        self.data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'telephone': '1234567890',
            'content': 'Test message'
        }
        content='''
        Wiadomość od: {}
        Nr tel: {}

        Treść wiadomości: {}
        '''.format(self.data['email'],self.data['telephone'],self.data['content'])
        send_mail(self.data['name'], content,'', ['emailapp621@gmail.com'])


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.username = 'test1'
        self.password = 'test123!hha@#'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
