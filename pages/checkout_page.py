import time
from selenium.webdriver.common.by import By

class checkout_page():
    def __init__(self,driver):
        self.driver=driver
    def check_out(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT,"India").click()
        self.driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
        time.sleep(10)
