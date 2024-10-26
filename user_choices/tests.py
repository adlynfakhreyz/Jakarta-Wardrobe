from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from user_choices.models import UserChoice

class UserChoicesViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        self.product = Product.objects.create(
            name='Test Product',
            category='Test Category',
            price=100.00,
            desc='This is a test product',
            color='Red',
            stock=10,
            shop_name='Test Shop',
            location='Test Location',
            img_url='http://example.com/test.jpg'
        )
        
        self.client.login(username='testuser', password='password123')

    def test_show_user_choices(self):
        response = self.client.get(reverse('user_choices:show_user_choices'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_choices.html')

    def test_add_user_choices(self):
        response = self.client.post(reverse('user_choices:add_user_choices', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserChoice.objects.count(), 1)

    def test_add_existing_user_choice(self):
        self.client.post(reverse('user_choices:add_user_choices', args=[self.product.pk]))
        response = self.client.post(reverse('user_choices:add_user_choices', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Choice already exists.')

    def test_delete_user_choices(self):
        self.client.post(reverse('user_choices:add_user_choices', args=[self.product.pk]))
        response = self.client.delete(reverse('user_choices:delete_user_choices', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(UserChoice.objects.count(), 0)

    def test_delete_non_existing_user_choice(self):
        response = self.client.delete(reverse('user_choices:delete_user_choices', args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Choice does not exist.')

