from django.test import TestCase

from app.models import CustomUser
from app.models import CustomGroup


class CustomUserTests(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser01", email="testuser01@mail.com", password="top_secret")

    def test_user_string(self):
        self.assertEqual(str(self.user), "testuser01")


class CustomGropTests(TestCase):

    def setUp(self):
        self.group = CustomGroup.objects.create(name="testgroup01")

    def test_group_string(self):
        self.assertEqual(str(self.group), "testgroup01")
