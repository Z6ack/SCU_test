import requests
from lxml import etree



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

def get_baidu_more():

    for i in range(1):

        url = 'https://www.baidu.com/more/'

        rs = requests.session()
        r = rs.get(url, headers=headers)

        r.encoding = 'utf-8'
        trees = etree.HTML(r.text)

        data=[]
        for i in range(1, 9):
            Theclass = trees.xpath('//*[@id="content"]/h3[{}]/text()'.format(i))
            data.append(Theclass[0])
        #print(data)

        j=0
        for i in range(1,90):
            name = trees.xpath('//*[@id="content"]/div[{}]/div[2]/a/text()'.format(i))
            link = trees.xpath('//*[@id="content"]/div[{}]/div[2]/a/@href'.format(i))
            what = trees.xpath('//*[@id="content"]/div[{}]/div[2]/span/text()'.format(i))
            if(name==[]):
                print(data[j])
                j=j+1
                print(" ")
            else:
                print(name[0])
                print(link[0])
                print(what[0])
                print(" ")

get_baidu_more()
