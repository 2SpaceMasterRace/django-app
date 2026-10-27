from django.test import TestCase


class PollsViewTests(TestCase):
    def test_index_is_available(self):
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
