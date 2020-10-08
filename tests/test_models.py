from django.test import TestCase

from app.models import CustomUser


class CustomUserTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="jacob", email="jacob@mail.com", password="top_secret")

    def test_user_string(self):
        self.assertEqual(self.user.username, "jacob")
