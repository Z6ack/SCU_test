from lxml import etree
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

def get_sina_news_serach():
    what = input("请输入你想查询的新浪新闻：")
    for i in range(1):
        url = 'https://search.sina.com.cn/?q={}&c=news&from=channel&range=all&size=10&dpc=0&ps=0&pf=0&page={}'.format(what,i)
        rs = requests.session()
        r = rs.get(url, headers=headers)
        r.encoding = 'utf-8'
        trees = etree.HTML(r.text)
        for j in range(4,22):
            title1 = trees.xpath('//*[@id="result"]/div[{}]/h2/a/text()[1]'.format(j))
            title2 = trees.xpath('//*[@id="result"]/div[{}]/h2/a/text()[2]'.format(j))
            if(title2==[]):
                print(what+title1[0])
            else:
                print(title1[0]+what+title2[0])
            Link = trees.xpath('//*[@id="result"]/div[{}]/h2/a/@href'.format(j))
            print(Link)
            From = trees.xpath('//*[@id="result"]/div[{}]/h2/span/text()'.format(j))
            print(From)
            comment = trees.xpath('//*[@id="result"]/div[{}]/div[2]/p/text()'.format(j))
            print(comment)
            From=trees.xpath('//*[@id="result"]/div[{}]/h2/span/text()'.format(j))
            print(' ')





get_sina_news_serach()