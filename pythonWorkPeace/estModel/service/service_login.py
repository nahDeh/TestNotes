#业务类

from page.page_index import PageIndex
from page.page_login import PageLogin
from page.page_user import PageUser

class ServiceLogin(object):
    def __init__(self,driver,base_url):
        #初始化和该业务有关的页面对象们
        self.page_index=PageIndex(driver,base_url)
        self.page_login=PageLogin(driver,base_url)
        self.page_user=PageUser(driver,base_url)


    def service_login_001(self):
        self.page_index.openUrl()
        self.page_index.click_login()

        self.page_login.input_zanhao("nswe")
        self.page_login.input_pwd("111111")
        self.page_login.click_login()

        siji=self.page_user.getNichenText() #"nswe，欢迎光临"

