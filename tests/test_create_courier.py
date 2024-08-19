import allure
import requests
from data import *
from conftest import *
from generator import Courier

class TestCourier:
    @allure.description('Создание курьера с валидными данными')
    def test_create_courier_success(self, create_and_delete_courier):
        response_body = '{"ok":true}'
        response_courier = Courier.create_courier(create_and_delete_courier)
        assert response_courier.status_code == 201 and response_courier.text == response_body

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_courier_was_created(self):
        response = requests.post(Urls.CREATE_COURIER,
            data = TestUser.correct_user)
        assert response.status_code == 409 and RegisterErrors.error_create_already_exist in response.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_false(self):
        response = requests.post(Urls.CREATE_COURIER,
                                 data=TestUser.user_without_login)
        assert response.status_code == 400 and RegisterErrors.error_create_without_login_or_password in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password_false(self):
        response = requests.post(Urls.CREATE_COURIER,
                                 data=TestUser.user_without_password)
        assert response.status_code == 400 and RegisterErrors.error_create_without_login_or_password in response.text


