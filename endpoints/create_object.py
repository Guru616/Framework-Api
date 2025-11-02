import requests
from endpoints import base_endpoint


class CreateObject(base_endpoint.Endpoint):

    def new_object(self, url, create_data):
        self.response = requests.post(url, json=create_data)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json['name'] == name
