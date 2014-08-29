import requests
import json

class ProductHuntApi:
    def __init__(self, dev_token):
        self.dev_token = dev_token
        self.base_url = 'https://api.producthunt.com/v1/'

    def make_request(self, path, method, payload = None):
        headers = {
            'Authorization' : 'Bearer %s' % self.dev_token
        }
        if method.lower() == 'get':
            return requests.get(self.base_url + path, headers=headers)
        elif method.lower() == 'post':
            return requests.post(self.base_url + path, headers=headers, data=payload)
        elif method.lower() == 'put':
            return requests.put(self.base_url + path, headers=headers, data=payload)
        raise Exception('Unknown method %s' % method)

    def get_posts(self):
        r = self.make_request('posts', 'GET')
        return json.loads(r.content)['posts']