from selenium.webdriver.common.by import By

class utils:
    def __init__(self, driver):
        self.driver = driver
    def assert_success(self,message):
        success_message = self.driver.find_element(By.XPATH,
                                                   "//div[@class='alert alert-success alert-dismissible']").text
        assert message in success_message
        print(success_message)