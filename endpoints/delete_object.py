import requests

from endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):
    def delete_object_by_id(self, url, obj_id):
        self.response = requests.delete(url + f'/{obj_id}')
        self.response_json = self.response.json()
