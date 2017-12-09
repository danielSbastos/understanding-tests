import json
import requests


class Post():

	def __init__(self, text):
		self.text = text

	def define_post_size(self):
		if len(self.text) <= 100:
			self.size = 'small'
		elif 100 < len(self.text) <= 500:
			self.size = 'medium'
		else:
			self.size = 'big'

	def publish_post(self):
		self.define_post_size()
		if self.size == 'small':
			return

		response = requests.post(
			"https://jsonplaceholder.typicode.com/posts",
			headers={'content-type': 'application/json'},
			data=json.dumps({'size': self.size, 'text': self.text})
		)
		return response

# Test

import requests_mock
from unittest import TestCase

class TestPosts(TestCase):

	@requests_mock.Mocker()
	def test_deny_publish_post(self, mock):
		mock.post("https://jsonplaceholder.typicode.com/posts")

		text = 'Once there was a man entitled the great emperor of Joinville.'

		published_post = Post(text).publish_post()
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
		self.assertEqual(mock.last_request.json(), {'size': 'medium', 'text': text})
