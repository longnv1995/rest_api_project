import requests
from config import BASE_URL

class BaseApi:
    def __init__(self) -> None:
        self.base_url = BASE_URL
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def get(self, endpoint, headers = None, params = None):
        return requests.get(self.base_url + endpoint, headers = headers, params = params)

    def post(self, endpoint, headers = None, data = None):
        return requests.post(self.base_url + endpoint, headers = headers, data = data)