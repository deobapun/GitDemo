class BaseDriver():
    def __init__(self,driver):
        self.driver=driver
    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 500);")