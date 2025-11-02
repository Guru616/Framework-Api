from conftest import url
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject


def test_create_post():
    new_object_endpoint = CreateObject()
    create_data = {
        "id": "12",
        "name": "Ultra Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "419.99",
            "Capacity": "64 GB"
        }
    }

    new_object_endpoint.new_object(url=url, create_data=create_data)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(create_data['name'])


def test_read_get(obj_id):
    get_object = GetObject()
    get_object.get_object(url, obj_id)
    get_object.check_response_is_200()
    get_object.check_response_id(obj_id)


def test_update_put(obj_id):
    update_obj = UpdateObject()
    update_data = {
        "id": "12",
        "name": "Gyper Ultra Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "419.99",
            "Capacity": "64 GB"
        }
    }
    update_obj.update_object_by_id(url=url, obj_id=obj_id, update_data=update_data)
    update_obj.check_response_is_200()
    update_obj.check_name_update(name=update_data['name'])


def test_delete(obj_id):
    delete_obj = DeleteObject()
    #delete_obj.check_response_is_200()
    delete_obj.delete_object_by_id(url, obj_id)
    #delete_obj.check_response_is_404()
