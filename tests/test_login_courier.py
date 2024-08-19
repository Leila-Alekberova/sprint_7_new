import requests
from data import *
from generator import *
import allure

class TestCourierLogin:

    @allure.title('Успешная авторизация')
    def test_login_courier_success(self):
        data = TestUser.correct_user
        response = requests.post(Urls.LOGIN_COURIER, data)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Нельзя авторизоваться без логина')
    def test_login_courier_without_login_false(self):
        data = TestUser.user_without_login
        response = requests.post(Urls.LOGIN_COURIER, data)
        assert response.status_code == 400 and LoginErrors.error_login_without_login_or_password in response.text

    @allure.title('Нельзя авторизоваться без пароля')
    def test_login_courier_without_password_false(self):
        data = TestUser.user_without_password
        response = requests.post(Urls.LOGIN_COURIER, data)
        assert response.status_code == 400 and LoginErrors.error_login_without_login_or_password in response.text
