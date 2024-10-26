from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserRegistrationTest(TestCase):

    def setUp(self):
        self.url = reverse('main:register')  


    def test_user_registration_failure(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(User.objects.filter(username='testuser').exists())

class UserLoginTest(TestCase):

    def setUp(self):
        self.url = reverse('main:login')  
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_user_login_success(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(str(response.wsgi_request.user), 'testuser')

    def test_user_login_failure(self):
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class UserLogoutTest(TestCase):

    def setUp(self):
        self.url = reverse('main:login') 
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')  

    def test_user_logout(self):
        response = self.client.get(reverse('main:logout'))  
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class StaticPagesTest(TestCase):

    def test_privacy_policy_page(self):
        response = self.client.get(reverse('main:privacy_policy'))  
        self.assertEqual(response.status_code, 200)  

    def test_terms_of_service_page(self):
        response = self.client.get(reverse('main:terms_of_service'))  
        self.assertEqual(response.status_code, 200)  

    def test_contact_us_page(self):
        response = self.client.get(reverse('main:contact_us'))  
        self.assertEqual(response.status_code, 200)  

