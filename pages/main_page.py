import allure
from pages.base_page import BasePage

from data import Url
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    _ACCOUNT_BUTTON = [By.XPATH, './/*[@href = "/account"]']  #кнопка Личный кабинет в хедере
    _CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text() = "Конструктор"]']  #Кнопка Конструктор
    _ORDER_LIST_BUTTON = [By.XPATH, './/p[text() = "Лента Заказов"]']  # Кнопка Лента заказов
    _ORDER_BUTTON = [By.XPATH, './/button[text() = "Оформить заказ"]']  #Кнопка Оформить заказ
    _PACK_BURGER = [By.XPATH, './/h1[text() = "Соберите бургер"]']  #Заголовок Соберите бургер
    _INGREDIENT_BUTTON = [By.XPATH, './/p[text() = "Флюоресцентная булка R2-D3"]']  #Булка Флюоресцентная булка
    _INGREDIENT_MODAL_WINDOW = [By.XPATH, './/h2[text() = "Детали ингредиента"]']  #Модальное окно Детали ингредиента
    _INGREDIENT_MODAL_CLOSE = [By.XPATH, './/button[contains(@class, "modal__close")]']  #Кнопка закрыть модальное окно
    _INGREDIENT_COUNT = [By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]']  #Счетчик ингредиента
    _BASKET = [By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]']  #Корзина
    _ORDER_ID = [By.XPATH, './/p[text() = "идентификатор заказа"]']  #Идентификатор заказа"
    _ORDER_NUMBER = [By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]']  #Номер заказа
    _OVERLAY = [By.CSS_SELECTOR, '.Modal_modal__loading__3534A']



    @allure.step('Открыть главную страницу Stellar Burgers')
    def open_main_page(self):
        self.navigate(Url.STELLA_BURGERS)

    @allure.step('Дождаться и нажать на кнопку Личный кабинет')
    def wait_and_click_account_button(self):
        self.wait_until_element_clickable(self._ACCOUNT_BUTTON)
        self.click_element(self._ACCOUNT_BUTTON)

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_button(self):
        self.click_element(self._CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку Лента заказов')
    def click_order_list_button(self):
        self.wait_for_element_visible(self._ORDER_LIST_BUTTON)
        self.click_element(self._ORDER_LIST_BUTTON)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        self.wait_for_element_visible(self._ORDER_BUTTON)
        self.click_element(self._ORDER_BUTTON)

    @allure.step('Клик на кнопку Личный кабинет')
    def click_account_button(self):
        self.element_to_be_clickable(self._ACCOUNT_BUTTON)

    @allure.step('Клик на ингредиент')
    def click_ingredient(self):
        self.click_element(self._INGREDIENT_BUTTON)

    @allure.step('Закрыть модальное окно')
    def click_modal_close(self):
        self.wait_for_element_visible(self._INGREDIENT_MODAL_CLOSE)
        self.click_element(self._INGREDIENT_MODAL_CLOSE)

    @allure.step('Отображение модального окна с номером заказа')
    def id_modal_is_displayed(self):
        self.wait_until_element_clickable(self._INGREDIENT_MODAL_CLOSE)
        self.wait_for_element_visible(self._ORDER_ID)
        return self.displayed(self._ORDER_ID)

    @allure.step('Получить название модального окна')
    def modal_text(self):
        return self.get_text(self._INGREDIENT_MODAL_WINDOW)

    @allure.step('Отображение Соберите бургер')
    def wait_visibility_constructor_header(self):
        self.wait_for_element_visible(self._PACK_BURGER)
        return self.get_text(self._PACK_BURGER)

    @allure.step('Перетащить ингредиент в корзину')
    def ingredient_drag_and_drop(self):
        self.wait_for_element_visible(self._INGREDIENT_BUTTON)
        self.drag_and_drop(self._INGREDIENT_BUTTON, self._BASKET)

    @allure.step('Получить количество булок в корзине')
    def get_count_bun(self):
        return self.get_text(self._INGREDIENT_COUNT)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.invisibil(self._OVERLAY)
        return self.get_text(self._ORDER_NUMBER)
