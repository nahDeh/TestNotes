#个人中心页面
from selenium.webdriver.common.by import By

from utils.page_base import PageBase

class PageUser(PageBase):
    url="/ucenter/index"
    loc_nicen=By.CSS_SELECTOR,"div.user_info > h2"


    def __init__(self,driver,base_url):
        PageBase.__init__(self,driver,base_url)

    def openUrl(self):
        self.open(PageUser.url)

    #获取昵称h2标签的文本内容
    def getNichenText(self):#预期："nswe，欢迎光临"
        return self.getEleText(PageUser.loc_nicen)
