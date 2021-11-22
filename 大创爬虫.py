import time
import json
from selenium import webdriver

def get_cookies():
        driver = webdriver.Chrome()
        url='https://wenshu.court.gov.cn/'
        driver.get(url)#发送请求
        #打开之后，手动登录一次
        time.sleep(3)
        input('完成登陆后点击enter:')
        time.sleep(3)
        dictcookies = driver.get_cookies()  # 获取cookies
        jsoncookies = json.dumps(dictcookies)  # 转换成字符串保存
        with open('cookie.txt', 'w') as f:
                f.write(jsoncookies)
        print('cookies保存成功！')
        driver.close()


def test():
        driver = webdriver.Chrome()
        url = 'https://wenshu.court.gov.cn/'
        driver.get(url)  # 发送请求
        # 打开之后，手动登录一次
        time.sleep(3)
        with open('cookie.txt', 'r', encoding='utf8') as f:
                listCookies = json.loads(f.read())

                for cookie in listCookies:
                        cookie_dict = {
                                'domain': '.wenshu.court.gov.cn',
                                'name': cookie.get('name'),
                                'value': cookie.get('value'),
                                "expires": '',
                                'path': '/',
                                'httpOnly': False,
                                'HostOnly': False,
                                'Secure': False
                        }
                        driver.add_cookie(cookie_dict)
                driver.refresh()  # 刷新网页,才能实现cookie导入

                #print(cookie_dict)
        time.sleep(3)
        what=input("请输入查询关键词：")
        driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').clear()  # 清空搜索框
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').send_keys("{}".format(what))  # 输入搜索内容
        time.sleep(0.5)
        WHAT = driver.find_element_by_xpath('//*[@id="_view_1540966814000"]/div/div[1]/div[3]')
        WHAT.click()
        driver.refresh()  # 刷新网页,才能实现cookie导入


        time.sleep(1)
        #driver.refresh()
        for i in range(1):
                for j in range(3,8):
                        WHAT =driver.find_element_by_xpath('//*[@id="_view_1545184311000"]/div[{}]/div[6]/div/a[2]'.format(j))
                        WHAT.click()
                        driver.refresh()  # 刷新网页,才能实现cookie导入
                        time.sleep(2)

        input("")


        driver.refresh()  # 刷新网页,才能实现cookie导入

if __name__ == "__main__":

  #get_cookies()
  test()