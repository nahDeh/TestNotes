# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_baiduSearch():
    #打开浏览器,打开指定网页
    chromeDriver =  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chromeDriver.maximize_window()
    chromeDriver.get("https://www.baidu.com")


    #开始操作
    search_input = chromeDriver.find_element(By.ID , "kw")
    search_input.send_keys("自动化测试")
    search_button = chromeDriver.find_element(By.ID , "su")
    search_button.click()


    #显示等待
    try:
        wait = WebDriverWait(chromeDriver , 10)
        wait.until(EC.title_contains("自动化测试"))
        #wait.until(EC.visibility_of_element_located((By.ID,"content_t_left")))

        assert "自动化测试" in chromeDriver.title
    
    except Exception as e :
        print(f"\n测试失败,失败原因:{e}")
        assert False

    finally:
        chromeDriver.quit()

    #time.sleep(5)


