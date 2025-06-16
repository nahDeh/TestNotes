#测试登录业务

import time,os,sys
sys.path.append(os.getcwd())

from utils.initDriver import init_driver
from service.service_login import ServiceLogin

from utils.readConfigFileUtils import readConfig

class TestLogin(object):
    def setup_class(self):
        self.base_url = readConfig("config/webConfig.yaml")["base_url"]

    def teardown_class(self):
        pass

    def setup(self):
        #初始化driver
        self.driver=init_driver()
        #初始化该业务的业务对象
        self.service_login=ServiceLogin(self.driver,self.base_url)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login_001(self):
        self.service_login.service_login_001()

