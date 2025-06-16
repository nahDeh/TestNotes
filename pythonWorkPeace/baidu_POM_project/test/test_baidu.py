# -*- coding:UTF-8 -*-
import time,os,sys
sys.path.append(os.getcwd())

from selenium import webdriver
from pages.baiduMainPage import BaiduMainPage
from pages.baiduResultPage import BaiduResultPage
import pytest

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit

def test_search_baidu(driver):
    mainPage = BaiduMainPage(driver)

    mainPage.open()
    mainPage.search("自动化测试")

    resultPage = BaiduResultPage(driver)
    assert resultPage.is_result_container_displayed()
