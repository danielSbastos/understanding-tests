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
