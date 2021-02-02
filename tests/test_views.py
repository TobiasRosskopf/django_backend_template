from django.test import TestCase


class ViewTests(TestCase):

    def test_user_not_logged_in(self):
        response = self.client.get('/current_user/')
        self.assertEqual(response.status_code, 401)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'detail': 'Anmeldedaten fehlen.'}
        )

    def test_signup(self):
        data = {
            "username": "testuser01",
            "password": "top_secret",
        }
        response = self.client.post('/signup/', data=data)
        self.assertEqual(response.status_code, 201)
