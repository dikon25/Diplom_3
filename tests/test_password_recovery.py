import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
from data import Data, Url


class TestRecoveryPage:
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_cross_via_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recovery_page = RecoveryPage(driver)
        assert main_page.get_current_url() == Url.RECOVER_PAGE
        assert recovery_page.wait_visibility_recovery_header() == 'Восстановление пароля'


    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_set_email_and_click_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recovery_page = RecoveryPage(driver)
        login_page.set_email(Data.data)
        recovery_page.click_recovery_button()
        recovery_page.wait_visibility_save_button()
        assert recovery_page.get_current_url() == Url.RESET_PAGE


    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_eye_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_account_button()
        login_page = LoginPage(driver)
        login_page.click_recover_password_button()
        recovery_page = RecoveryPage(driver)
        recovery_page.click_recovery_button()
        recovery_page.click_eye_button()
        assert recovery_page.check_is_active_field() == True