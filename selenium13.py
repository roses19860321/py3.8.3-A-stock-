from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
# 版本对应
# geckodriver 0.17
# Selenium 3.4
# Firefox 52
# python3.7.1
def findElement(locator,timeout=28):
    element=WebDriverWait(web,timeout).until(lambda x:x.find_element(*locator))
    return element
web = webdriver.Firefox()
web.get('https://hippo.gf.com.cn/#StockQuote')
# web.get('https://www.baidu.com/')
loc = ('xpath', "//div[@class='Footer button-num-1']/button[@class='MuiButtonBase-root MuiButton-root MuiButton-text']")
findElement(loc).click()
loc = ('xpath', "//div[@class='Title']/a[@class='Close']")
findElement(loc).click()
loc = ('xpath', "//span[text()='A股']")
findElement(loc).click()
loc = ('xpath', "//span[text()='换手']")
findElement(loc).click()
while 1:
    time.sleep(4)
    for i in range(20):
        txtName=web.find_element_by_xpath('//tr[@data-key='+'"'+str(i)+'"]/td[@class="name"]/span').text
        txtHandover=web.find_element_by_xpath('//tr[@data-key='+'"'+str(i)+'"]/td[@data-id="handover"]').text
        print('{}\t{}\t{}'.format(i,txtName,txtHandover))
    print('----AlmosOu----')
# txt=web.find_element_by_xpath('//tr[@data-key="1"]/td[@data-id="now"]/span')
# print(txt.text)
web.quit()
# click=web.find_element_by_link_text('百度智能门户')