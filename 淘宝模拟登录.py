from selenium import webdriver
import time
import json

import time
import json
from selenium import webdriver


def get_cookies():
    driver = webdriver.firefox()
    url = 'https://wenshu.court.gov.cn/'
    driver.get(url)  # 发送请求
    # 打开之后，手动登录一次
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
                    'domain': '.wfw.scu.edu.cn',
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