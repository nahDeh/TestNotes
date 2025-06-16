#首页页面
from selenium.webdriver.common.by import By

from utils.page_base import PageBase

class PageIndex(PageBase):
    url="/"
    loc_login=By.XPATH,"//a[@href='/simple/login' and text()='登录']"


    def __init__(self,driver,base_url):
        PageBase.__init__(self,driver,base_url)

    def openUrl(self):
        self.open(PageIndex.url)

    def click_login(self):
        self.click(PageIndex.loc_login)