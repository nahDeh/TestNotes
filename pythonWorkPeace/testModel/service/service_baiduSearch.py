#业务类

from page.page_baiduSearch import PageBaiduSearch

class ServiceBaiduSearch(object):
    def __init__(self,driver,base_url):
        #初始化和该业务有关的页面对象们
        self.page_baiduSearch=PageBaiduSearch(driver,base_url)


    def serbice_baiduSearch_001(self):
        self.page_baiduSearch.openUrl()
        self.page_baiduSearch.inputSearchKW("Selenium自动化")
        self.page_baiduSearch.click_baiduyixia()
