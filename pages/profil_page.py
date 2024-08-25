import allure
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    _HISTORY_ORDERBUTTON = [By.XPATH, './/a[text() = "История заказов"]']  # Кнопка История заказов
    _EXITBUTTON = [By.XPATH, './/button[text() = "Выход"]']  # Кнопка Выход
    _ORDER_HISTORY = [By.XPATH,
                      './/div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, '
                      '"text text_type_digits-default")])[last()]']  # История заказов пользователя

    @allure.step('Нажать на кнопку История заказов')
    def click_history(self):
        self.wait_for_element_visible(self._HISTORY_ORDERBUTTON)
        self.click_element(self._HISTORY_ORDERBUTTON)

    @allure.step('Нажать на кнопку Выход')
    def click_logout(self):
        self.wait_until_element_clickable(self._EXITBUTTON)
        self.click_element(self._EXITBUTTON)
