import json
import requests


class Post():
    MINIMUM_LENGHT = 100

    def __init__(self, text):
        self.text = text
        self.has_accepted_size = self.check_minumum_size((len(self.text)))

    def check_minumum_size(self, lenght):
        if lenght < self.MINIMUM_LENGHT:
            return False
        return True

    def publish_post(self):
        if self.has_accepted_size:
            return requests.post(
                "https://jsonplaceholder.typicode.com/posts",
                headers={'content-type': 'application/json'},
                data=json.dumps({'text': self.text})
            )


# TestCase

import requests_mock
from unittest import TestCase

class TestPosts(TestCase):

    @requests_mock.Mocker()
    def test_deny_publish_post(self, mock):
        mock.post("https://jsonplaceholder.typicode.com/posts")

        text = 'Once there was a man entitled the great emperor of Joinville.'

        Post(text).publish_post()
        self.assertEqual(len(mock.request_history), 0)
        self.assertFalse(mock.called)

    @requests_mock.Mocker()
    def test_accept_publish_post(self, mock):
        mock.post("https://jsonplaceholder.typicode.com/posts", status_code=201)

        text = 'Once there was a man entitled the great emperor of Joinville and ' + \
               'his name was Udo Dohler. Many towels are named after him.'
        published_post = Post(text).publish_post()

        self.assertEqual(published_post.status_code, 201)
        self.assertEqual(len(mock.request_history), 1)
        self.assertTrue(mock.called)
        self.assertEqual(mock.last_request.json(), {'text': text})
