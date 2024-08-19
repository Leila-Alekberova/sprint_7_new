import pytest
import data
import json
from data import OrderSuccess
import allure
from generator import Order

class TestCreateOrder():

    @allure.title('Создание заказа с валидными данными')
    @pytest.mark.parametrize('color',
                             (['BLACK'], ['GREY'], ['BLACK', 'GREY'], ['']))
    def test_create_order_success(self, color: list):
        response = Order.create_order(color)
        assert response.status_code == 201 and OrderSuccess.ORDER_CREATE_SUCCESS in response.json()