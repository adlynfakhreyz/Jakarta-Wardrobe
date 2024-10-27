from django.test import TestCase


# Create your tests here.

class ProfileTest(TestCase):
    def test_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_update(self):
        response = self.client.get('/profile/update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_update.html')