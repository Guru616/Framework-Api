import requests

from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_object(self, url, obj_id):
        self.response = requests.get(url + f'/{obj_id}')
        self.response_json = self.response.json()

    def check_response_id(self, obj_id):
        assert self.response_json['id'] == obj_id
