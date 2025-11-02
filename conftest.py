import pytest
import requests

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

url = 'https://api.restful-api.dev/objects'
# url = 'https://fastapi-ggg666.amvera.io/'

@pytest.fixture()
def obj_id():
    create_obj = CreateObject()
    delete_obj = DeleteObject()
    create_data = {
        "id": "12",
        "name": "Ultra Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "419.99",
            "Capacity": "64 GB"
        }
    }

    create_obj.new_object(url=url, create_data=create_data)
    yield create_obj.response_json['id']
    delete_obj.delete_object_by_id(url, create_obj.response_json['id'])
