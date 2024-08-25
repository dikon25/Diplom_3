import pytest
from selenium import webdriver

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if 'chrome' in request.param:
        driver = webdriver.Chrome()
    elif 'firefox' in request.param:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()