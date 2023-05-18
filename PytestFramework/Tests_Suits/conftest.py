import pytest
from selenium import webdriver
from PytestFramework.Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()

    request.cls.driver = web_driver
    web_driver.delete_all_cookies()
    web_driver.implicitly_wait(10)
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()

    yield
    web_driver.quit()

