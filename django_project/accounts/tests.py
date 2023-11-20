from django.contrib.auth import get_user_model
from django.urls import reverse, resolve # new
from django.test import TestCase

from .forms import CustomUserCreationForm
from .views import SingUpView


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will",
            email="will123@gmail.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will123@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="will",
            email="will123@gmail.com",
            password="testpass123",
        )
        
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will123@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SigUpPageTest(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)
        
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Not in this page")
        
    
    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
    
    def test_signup_view(self):
        view = resolve("/accounts/sgnup/")
        self.assertEqual(view.fun.__name__, SingUpView.as_view().__name__)
