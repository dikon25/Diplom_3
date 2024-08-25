import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Data, Url




class TestMainPage:
    @allure.title('переход по клику на «Конструктор»')
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        main_page.click_constructor_button()
        assert main_page.get_current_url() == Url.STELLA_BURGERS


    @allure.title('переход по клику на «Лента заказов»')
    def test_order_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_list_button()
        assert main_page.get_current_url() == Url.ORDER_PAGE


    @allure.title('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталям')
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        assert main_page.modal_text() == 'Детали ингредиента'


    @allure.title('Проверка всплывающее окно с деталями закрывается кликом по крестику')
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()
        main_page.click_modal_close()
        assert main_page.wait_visibility_constructor_header() == 'Соберите бургер'


    @allure.title('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.ingredient_drag_and_drop()
        assert main_page.get_count_bun() == '2'


    @allure.title('залогиненный пользователь может оформить заказ')
    def test_make_order_auth_user(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        assert main_page.id_modal_is_displayed() == True