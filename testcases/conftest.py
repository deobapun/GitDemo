from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://rahulshettyacademy.com/loginpagePractise/"
    driver.get(url)
    request.cls.driver=driver #when use request it will use class lavel and we have to use self.driver in the code for avoid error #
    yield
    driver.close()