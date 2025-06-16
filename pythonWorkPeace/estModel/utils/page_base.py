#页面父类
#主要封装一些每个UI都需要的通用的数据、通用的UI操作

class PageBase(object):
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url

    #打开某url
    def open(self,PathUrl):
        self.driver.get(self.base_url+PathUrl)

    #根据元素的定位特征loc来定位到某元素
    def find_element(self,loc):
        by=loc[0]
        value=loc[1]
        return self.driver.find_element(by,value)

    #给某元素loc输入某数据data
    def input(self,loc,data):
        self.find_element(loc).send_keys(data)

    #点击某元素loc
    def click(self,loc):
        self.find_element(loc).click()

    #获取某元素loc的文本内容（可自动去掉首尾空格）
    def getEleText(self,loc,isStrip=True):
        ele=self.find_element(loc)
        if isStrip:
            return ele.text.strip()
        else:
            return ele.text


