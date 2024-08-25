import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, locator: tuple, timeout: int = 10):
        self.driver.find_element(*locator)

    @allure.step('Нажать на элемент')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()



    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    def text_in_attribute(self, locator, text):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_attribute(locator, 'class', text))

    def invisibil(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))


    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Получить адрес текущей страницы')
    def get_current_url(self):
        return self.driver.current_url


    def displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Дождатся видимости элемента')
    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        #try:
        #    return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(*locator))
        #except TimeoutException:
        #    print(f'Element with locator {locator} not visible after {timeout} seconds')
        #    return None

    @allure.step('Перейти на страницу')
    def navigate(self, url: str):
        self.driver.get(url)


    def wait_until_element_clickable(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))


    def element_to_be_clickable(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Перетащить заказ')
    def drag_and_drop(self, element, endpoint):
        element = self.driver.find_element(*element)
        endpoint = self.driver.find_element(*endpoint)
        ActionChains(self.driver).drag_and_drop(element, endpoint).perform()


