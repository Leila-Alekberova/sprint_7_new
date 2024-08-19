import pytest
import json
from faker import Faker

class Urls:
    URL = 'http://qa-scooter.praktikum-services.ru/'
    LOGIN_COURIER = f'{URL}api/v1/courier/login'
    DELETE_COURIER = f'{URL}/api/v1/courier'
    CREATE_COURIER = f'{URL}api/v1/courier/'
    ORDERS_LIST = f'{URL}api/v1/orders'
    ORDER_TRACK = f'{URL}api/v1/orders/track'

class Helpers:

    @staticmethod
    def create_courier_fake():
        fake = Faker()
        login = fake.name()
        password = fake.password()
        first_name = fake.first_name()
        user = {
            "login": login,
            "password": password,
            "first_name": first_name
        }
        return user

    @staticmethod
    def test_order(color):
        order = {
            "firstName": "Имя",
            "lastName": "Фамилия",
            "address": "Дмитровское шоссе",
            "metroStation": 4,
            "phone": "+79999753389",
            "rentTime": 3,
            "deliveryDate": "2024 - 08 - 20",
            "comment": "комментарий",
            "color": color
        }
        return json.dumps(order)

class TestUser:
    correct_user = {
        "login": "ninj11qqa",
        "password": "123"
    }

    user_without_login = {
        "login": "",
        "password": "TestTest123"
    }

    user_without_password = {
        "login": "Test_login",
        "password": ""
    }

class LoginErrors:
    error_login_without_login_or_password = "Недостаточно данных для входа"
    error_login_user_not_found = "Учетная запись не найдена"

class RegisterErrors:
    error_create_without_login_or_password = "Недостаточно данных для создания учетной записи"
    error_create_already_exist = "Этот логин уже используется"

class DeliteErrors:
    error_delete_without_id = "Недостаточно данных для удаления курьера"
    error_delete_not_found_id = "Курьера с таким id нет"

class CouriersErrors:
    error_count_orders_without_data = "Недостаточно данных для поиска"
    error_count_orders_not_found = "Курьер не найден"

class OrdersErrors:
    error_track_order_without_data = "Недостаточно данных для поиска"
    error_track_order_not_found = "Заказа с таким id не существует"
    error_accept_order_not_found = "Курьера с таким id не существует"
    error_accept_order_no_complete = "Этот заказ нельзя завершить"

class DeliteOrders:
    error_accept_order_without_number = "Недостаточно данных для поиска"
    error_accept_order_not_found = "Заказ не найден"
    error_accept_order_in_work = "Этот заказ уже в работе"

class OrderSuccess:
    ORDER_CREATE_SUCCESS = "track"
    ORDER_LIST_SUCCESS = "orders"