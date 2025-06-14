# -*- coding: utf-8 -*-

from selenium import webdriver # 导入 webdriver 包
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver=webdriver.Chrome()
# dr = webdriver.Firefox() # 初始化一个火狐浏览器实例：driver
# dr=webdriver.Ie() #调用 IE 浏览器
driver.maximize_window() # 最大化浏览器
driver.implicitly_wait(30)
driver.get("https://gemini.google.com/app") # 通过 get()方法，打开一个 url 站点
# ele_input=driver.find_element(By.ID, "kw")
# ele_input.send_keys("Selenium 自动化测试")
# ele_baiduyixia=driver.find_element(By.ID, "su")
# ele_baiduyixia.click()
input_area = driver.find_element(By.CSS_SELECTOR, "div[data-placeholder='问一问 Gemini']")
input_area.send_keys("你好，Gemini！")
# 等待最多10秒，直到 aria-label='发送' 的按钮变为可点击状态
wait = WebDriverWait(driver, 20)
send_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='发送']")))
# 然后再执行点击操作
send_button.click()

message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "model-response-text")))
out_text = message.text

print("Gemini 回答：")
print(out_text)


time.sleep(50)
driver.quit() # 关闭并退出浏览器