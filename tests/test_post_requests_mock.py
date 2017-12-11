from unittest import TestCase
import requests_mock
from understanding_tests.post import Post


class TestPosts(TestCase):

    @requests_mock.Mocker()
    def test_deny_publish_post(self, mock):
        mock.post("https://jsonplaceholder.typicode.com/posts")

        text = "Once there was a man entitled the great emperor of Joinville."

        Post(text).publish_post()
        self.assertEqual(len(mock.request_history), 0)
        self.assertFalse(mock.called)

    @requests_mock.Mocker()
    def test_accept_publish_post(self, mock):
        mock.post("https://jsonplaceholder.typicode.com/posts")

        text = "Once there was a man entitled the great emperor of " + \
               "Joinville and his name was Udo Dohler. Many towels " + \
               "are named after him."
        published_post = Post(text).publish_post()

        self.assertEqual(len(mock.request_history), 1)
        self.assertTrue(mock.called)
        self.assertEqual(mock.last_request.json(), {"text": text})
