import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class RecoveryPage(BasePage):
    _RECOVERBUTTON = [By.XPATH, './/button[text() = "Восстановить"]']
    _BUTTONSAVE = [By.XPATH, './/button[text() = "Сохранить"]']
    _INPUTPASSWORD = [By.XPATH, './/*[contains(@class,"input__placeholder")]']
    _VISIBLEBUTTON = [By.XPATH, './/div[contains(@class, "icon-action")]']
    _RECOVERYHEAD = [By.XPATH, './/h2[text() = "Восстановление пароля"]']

    @allure.step('Нажать кнопку Восстановить')
    def click_recovery_button(self):
        self.wait_for_element_visible(self._RECOVERBUTTON)
        self.click_element(self._RECOVERBUTTON)

    @allure.step('Нажать кнопку видимости пароля')
    def click_eye_button(self):
        self.wait_for_element_visible(self._VISIBLEBUTTON)
        self.click_element(self._VISIBLEBUTTON)

    @allure.step('Отображение Восстановление пароля')
    def wait_visibility_recovery_header(self):
        self.wait_for_element_visible(self._RECOVERYHEAD)
        return self.get_text(self._RECOVERYHEAD)

    @allure.step('Дождаться кнопки Сохранить')
    def wait_visibility_save_button(self):
        self.wait_for_element_visible(self._BUTTONSAVE)

    @allure.step('Проверить активность поля')
    def check_is_active_field(self):
        return self.text_in_attribute(self._INPUTPASSWORD, 'input__placeholder-focused')
