import pytest
import requests
from data import *

@pytest.fixture(scope='function')
def only_create_courier():
    user = Helpers.create_courier_fake()
    yield user

@pytest.fixture(scope='function')
def create_and_delete_courier():
    courier = Helpers.create_courier_fake()
    yield courier
    login_courier = requests.post(Urls.LOGIN_COURIER, data=courier)
    id = login_courier.json()['id']
    requests.delete(Urls.DELETE_COURIER + str(id))