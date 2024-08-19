import requests
import allure
from data import *


class Order:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(color):
        payload = Helpers.test_order(color)
        response = requests.post(Urls.ORDERS_LIST, data=payload)
        return response

class Courier:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        return requests.post(Urls.CREATE_COURIER, data=payload)

    @allure.step('Удаление курьера')
    def delete_courier(courier_id=None):
        return requests.delete(f"{Urls.DELETE_COURIER}/{courier_id}")