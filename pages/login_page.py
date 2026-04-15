import time
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver=driver
    def login(self,name01,password01):
        self.driver.find_element(By.ID, "username").send_keys(name01)
        self.driver.find_element(By.ID, "password").send_keys(password01)
        self.driver.find_element(By.ID, "terms").click()
        self.driver.find_element(By.ID, "signInBtn").click()
        time.sleep(10)
