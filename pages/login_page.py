import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    _INPUT_EMAIL = [By.XPATH, './/label[text() = "Email"]/following-sibling::input']  # Поле ввода Email
    _INPUT_PASSWORD = [By.XPATH, './/label[text() = "Пароль"]/following-sibling::input']  # Поле ввода Пароль
    _LOGIN_BUTTON = [By.XPATH, './/button[text() = "Войти"]']  # Кнопка "Войти" на странице входа
    _RECOVER_PASSWORD_BUTTON = [By.XPATH, './/a[text() = "Восстановить пароль"]'] #Кнопка Восстановить пароль


    @allure.step('Ввести почту')
    def set_email(self, email):
        self.send_keys(self._INPUT_EMAIL, email)


    @allure.step('Ввести пароль')
    def set_password(self, password):
        self.send_keys(self._INPUT_PASSWORD, password)


    @allure.step('Клик на кнопку Войти')
    def click_login_button(self):
        self.wait_for_element_visible(self._LOGIN_BUTTON)
        self.click_element(self._LOGIN_BUTTON)


    @allure.step('Авторизация')
    def login_account(self, user):
        self.set_email(user['email'])
        self.set_password(user['password'])
        self.click_login_button()


    @allure.step('Дождаться кнопку Войти')
    def wait_login_button(self):
        self.wait_for_element_visible(self._LOGIN_BUTTON)


    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_recover_password_button(self):
        self.wait_for_element_visible(self._RECOVER_PASSWORD_BUTTON)
        self.click_element(self._RECOVER_PASSWORD_BUTTON)