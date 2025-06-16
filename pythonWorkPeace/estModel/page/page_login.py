#登录页

from selenium.webdriver.common.by import By

from utils.page_base import PageBase

class PageLogin(PageBase):
    url="/simple/login"
    loc_zanhao=By.NAME,"login_info"
    loc_pwd=By.NAME,"password"
    loc_login=By.CSS_SELECTOR,"input.input_submit"

    def oppenUrl(self):
        self.open(PageLogin.url)

    def __init__(self,driver,base_url):
        PageBase.__init__(self,driver,base_url)

    def input_zanhao(self,data):
        self.input(PageLogin.loc_zanhao,data)

    def input_pwd(self,data):
        self.input(PageLogin.loc_pwd,data)

    def click_login(self):
        self.click(PageLogin.loc_login)