from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUSerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='John Doe', email='john.doe@example.com', password="Password12345")
        self.assertEqual(user.username, 'John Doe')
        self.assertEqual(user.email, 'john.doe@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='SuperMan', email='superman@example.com', password='Admin12345')
        self.assertEqual(admin_user.username, 'SuperMan')
        self.assertEqual(admin_user.email, 'superman@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
