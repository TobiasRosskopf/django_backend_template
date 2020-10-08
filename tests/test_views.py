from django.test import TestCase


class ViewTests(TestCase):

    def test__user_not_logged_in(self):
        """
        Test user not logged in
        """
        response = self.client.get('/app/current_user/?format=json')
        self.assertEqual(response.status_code, 401)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'detail': 'Anmeldedaten fehlen.'}
        )
