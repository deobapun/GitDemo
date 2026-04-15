import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class ShopPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    def mobile_selection(self,mobilename):
        mobile_names = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for mobile_name in mobile_names:
            mobile = mobile_name.find_element(By.XPATH, ".//h4[@class='card-title']").text
            if mobile == "mobilename":
                mobile_name.find_element(By.XPATH, ".//button[contains(text(),'Add')]").click()
                time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()