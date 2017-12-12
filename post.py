import json
import requests


class Post():
    MINIMUM_LENGHT = 100

    def __init__(self, text):
        self.text = text
        self.has_accepted_size = self.has_minumum_size((len(self.text)))

    def has_minumum_size(self, length):
        return length > self.MINIMUM_LENGHT

    def publish_post(self):
        if self.has_accepted_size:
            return requests.post(
                "https://jsonplaceholder.typicode.com/posts",
                headers={'content-type': 'application/json'},
                data=json.dumps({'text': self.text})
            )
