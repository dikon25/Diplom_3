import allure
from pages.profil_page import ProfilePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Data, Url


class TestProfilePage:
    @allure.title('переход по клику на «Личный кабинет»')
    def test_cross_via_account_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        assert main_page.get_current_url() == Url.LOGIN_PAGE


    @allure.title('переход в раздел «История заказов»')
    def test_cross_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.wait_and_click_account_button()
        profil_page = ProfilePage(driver)
        profil_page.click_history()
        assert main_page.get_current_url() == Url.HISTORY_PAGE


    @allure.title('выход из аккаунта')
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_and_click_account_button()
        login_page = LoginPage(driver)
        login_page.login_account(Data.data)
        main_page.wait_and_click_account_button()
        profil_page = ProfilePage(driver)
        profil_page.click_logout()
        login_page.wait_login_button()
        assert main_page.get_current_url() == Url.LOGIN_PAGE