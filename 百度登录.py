import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://passport.csdn.net/login?code=public")


driver.find_element_by_link_text("账号密码登录").click()
time.sleep(2)


login_usename = driver.find_element_by_name("all")
login_usename.send_keys('13682505196')

login_passwd = driver.find_element_by_name("pwd")
login_passwd.send_keys('A13682505196a')

time.sleep(4)

driver.find_element_by_class("btn btn-primary").click()
