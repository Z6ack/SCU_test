from lxml import etree
from selenium import webdriver

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }

def get_baidu_translation():

    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=option)
    print("=" * 100)
    what=input("请输入翻译内容（支持中英互译）：")
    url = 'http://fanyi.baidu.com/#en/zh/{}'.format(what)
    driver.get(url)

    html = driver.page_source
    trees = etree.HTML(html)
    WHAT = trees.xpath('//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span/text()')

    print("翻译结果为："+WHAT[0])


if __name__ == "__main__":

    while(1):

        get_baidu_translation()
        b = input("输入0继续查询，输入1退出查询：")
        if(b=='1'):
            break
