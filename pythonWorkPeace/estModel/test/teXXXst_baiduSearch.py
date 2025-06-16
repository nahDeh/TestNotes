#测试百度搜索业务
from selenium import webdriver  # 导入webdriver包
import time,os,sys
sys.path.append(os.getcwd())

from utils.initDriver import init_driver
from service.service_baiduSearch import ServiceBaiduSearch
from utils.readConfigFileUtils import readConfig

class TestBaiduSearch(object):
    def setup_class(self):
        self.base_url = readConfig("config/webConfig.yaml")["base_url"]

    def teardown_class(self):
        pass

    def setup(self):
        #初始化driver
        self.driver=init_driver()
        #初始化该业务的业务对象
        self.serviceBaiduSearch=ServiceBaiduSearch(self.driver,self.base_url)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_baiduSearch_001(self):
        self.serviceBaiduSearch.serbice_baiduSearch_001()

