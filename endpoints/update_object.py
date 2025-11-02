import requests

from endpoints.base_endpoint import Endpoint


class UpdateObject(Endpoint):
    def update_object_by_id(self, url, obj_id, update_data):
        self.response = requests.put(url + f'/{obj_id}',json=update_data)
        self.response_json = self.response.json()


    def check_name_update(self, name):
        assert self.response_json['name'] == name