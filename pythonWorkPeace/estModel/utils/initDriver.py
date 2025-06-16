from selenium import webdriver

#根据浏览器类型来获取不同的浏览器的driver
def init_driver(browerType="chrome",timeout=10,isMax=True):
    browerType=browerType.lower()
    driver=None
    if browerType=="chrome":
        driver = webdriver.Chrome()
    elif browerType=="ie":
        driver=webdriver.Ie()
    elif browerType=="firfox":
        driver=webdriver.Firefox()
    else:
        driver=None

    if isMax:
        driver.maximize_window()

    driver.implicitly_wait(timeout)

    return driver