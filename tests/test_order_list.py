import allure
import requests
from data import Urls

class TestOrderList:
    @allure.title('Список заказов')
    def test_list_order(self):
        response = requests.get(Urls.ORDERS_LIST)
        assert response.status_code == 200 and "orders" in response.json()