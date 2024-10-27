from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Rating, Comment
from user_choices.models import UserChoice

class ProductViewsTest(TestCase):

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

    def test_show_products_by_price(self):
        response = self.client.get(reverse('products:show_products_by_price'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_show_products_by_category(self):
        response = self.client.get(reverse('products:show_products_by_category', args=['Test Category']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_product_detail(self):
        response = self.client.get(reverse('products:product_detail', args=[self.product.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_review_products(self):
        response = self.client.get(reverse('products:review_products', args=[self.product.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add a Comment')

    def test_add_rating(self):
        response = self.client.post(reverse('products:add_rating'), {
            'product_id': self.product.uuid,
            'rating': 5
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.count(), 1)

    def test_page_gaada(self):
        response = self.client.get('/products/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_add_comment(self):
        response = self.client.post(reverse('products:add_comment'), {
            'product_id': self.product.uuid,
            'comment': 'Great product!'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 1)

    def test_get_ratings_comments(self):
        self.client.post(reverse('products:add_rating'), {
            'product_id': self.product.uuid,
            'rating': 5
        })
        self.client.post(reverse('products:add_comment'), {
            'product_id': self.product.uuid,
            'comment': 'Great product!'
        })
        
        response = self.client.get(reverse('products:get_ratings_comments', args=[self.product.uuid]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('ratings', response.json())
        self.assertIn('comments', response.json())

    def test_find_product(self):
        response = self.client.get(reverse('products:find_product'), {'q': 'Test Product'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

