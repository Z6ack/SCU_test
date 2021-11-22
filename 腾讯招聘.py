from lxml import etree
from bs4 import BeautifulSoup
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'cookie':'_ga=GA1.2.741549489.1600008709; pgv_pvi=8093896704; pgv_pvid=378075616; _gcl_au=1.1.1666053754.1630843983; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100011930117%22%2C%22first_id%22%3A%22e22e55959d05db4ed0929acd767433c8%40devS%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E8%85%BE%E8%AE%AF%E4%BA%91%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_utm_medium%22%3A%22cpd%22%7D%2C%22%24device_id%22%3A%2217868f4b2442e6-0dbd0c103fbeda-5771031-1327104-17868f4b24578c%22%7D; loading=agree; UserCookie=b5e8696d89c9be7cc87d70e96edd126db7eb028fdd9de3cd81f85e53c10ccf0c; IsLogin=1'
}

def get_txzp():
    for c in range(1,11):
        url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1631625383162&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(c)
        rs = requests.session()
        r = rs.get(url, headers=headers)
        r.encoding = 'utf-8'
        #soup = BeautifulSoup(r.content, 'lxml')
        #trees = etree.HTML(r.text)
        m=r.text
        M=json.loads(m)
        M1=M["Data"]

        M2=M1['Posts']

        for i in M2:
            print("="*300)
            data=[]
            #print(i)
            #print(i['RecruitPostName']+' '+i['CountryName']+' '+i['LocationName']+' '+i['BGName']+' '+i['ProductName']+' '+i[ 'CategoryName']+' '+i['Responsibility']+' '+i['LastUpdateTime']+' '+i['PostURL'])
            data.append(i['RecruitPostName'])
            data.append(i['CountryName'])
            data.append(i['LocationName'])
            data.append(i['BGName'])
            data.append(i['ProductName'])
            data.append(i[ 'CategoryName'])
            data.append(i['Responsibility'])
            data.append(i['LastUpdateTime'])
            data.append(i['PostURL'])

            for j in data:

                print(j)

if __name__ == "__main__":
    get_txzp()

