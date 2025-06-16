from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaiduResultPage:
    Result_container = (By.ID,"content_left")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def is_result_container_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.Result_container))
            return True
        except :
            return False
    