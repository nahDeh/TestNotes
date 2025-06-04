#页面类
from selenium.webdriver.common.by import By

from utils.page_base import PageBase

class PageBaiduSearch(PageBase):
    url="/" #PathUrl
    loc_zanhao=By.ID,"kw"
    loc_baiduyixia=By.ID,"su"

    def __init__(self,driver,base_url):
        PageBase.__init__(self,driver,base_url)

    #打开页面网址
    def openUrl(self):
        self.open(PageBaiduSearch.url)

    #输入搜索关键字
    def inputSearchKW(self,data):
        self.input(PageBaiduSearch.loc_zanhao,data)

    #点击“百度一下”按钮
    def click_baiduyixia(self):
        self.click(PageBaiduSearch.loc_baiduyixia)