import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    _ORDER = [By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]'] #Заказ
    _LAST_ORDER = [By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]'] #Последний заказ
    _ORDER_MODAL_WINDOWN = [By.XPATH, './/div[contains(@class, "Modal_orderBox")]'] #Окно с деталями заказа
    _WORK_ORDER = [By.XPATH, './/*[contains(@class, "orderListReady")]//li[contains(@class,"digits-default")]'] #Заказ в работе
    _ALL_ORDERS = [By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]']  #Счетчик всех заказов
    _FOR_TODAY_ORDERS = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]']  #Счетчик заказов за сегодня



    @allure.step('Нажать на заказ')
    def click_order(self):
        self.wait_for_element_visible(self._ORDER)
        self.click_element(self._ORDER)


    @allure.step('Отображение модального окна с деталями заказа')
    def order_modal_is_displayed(self):
       return self.displayed(self._ORDER_MODAL_WINDOWN)


    @allure.step('Количество заказов за все время')
    def get_count_all_orders(self):
        self.wait_for_element_visible(self._ALL_ORDERS)
        return self.get_text(self._ALL_ORDERS)


    @allure.step('Количество заказов за сегодня')
    def get_count_today_orders(self):
        self.wait_for_element_visible(self._FOR_TODAY_ORDERS)
        return self.get_text(self._FOR_TODAY_ORDERS)


    @allure.step('Получить номер заказа В работе')
    def get_order_in_work(self):
        self.wait_for_element_visible(self._WORK_ORDER)
        return self.get_text(self._WORK_ORDER)


    @allure.step('Получить номер последнего заказа')
    def get_last_order_number(self):
        self.wait_for_element_visible(self._LAST_ORDER)
        return self.get_text(self._LAST_ORDER)