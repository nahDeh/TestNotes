from selenium.webdriver.common.by import By

class BaiduMainPage:
    SEARCH_INPUT = (By.ID,"kw")
    SEARCH_BUTTON = (By.ID,"su")

    def __init__(self , driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    def search(self,keyword):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(keyword)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

