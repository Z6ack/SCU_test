from bs4 import BeautifulSoup
import requests
import re
import csv
import time
import random

def random_sleep(mu, sigma):
    '''正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __utmv=30149280.22496; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; __gads=ID=810d93bb78086141-22022a2d0fc60059:T=1613551710:RT=1613551710:S=ALNI_MYYosJrECVrNYBce5zOjq_h-aZSJQ; __utma=30149280.1886584236.1598363955.1613571128.1613619986.33; __utmc=30149280; __utmz=30149280.1613619986.33.30.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __utmb=30149280.4.10.1613619986; ct=y; dbcl2="228363246:pJBiFD3wGz0"; ck=TWTl'   }

def get_comments(sid):
    import time


    results = []

    for i in range(26):
        print("         正在爬取第{}页的评论,还有{}页".format(i+1,25-i))

        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(sid, str(
            i * 20))

        rs = requests.session()
        r = rs.get(url, headers=headers)
        random_sleep(1.5, 0.4)
        soup = BeautifulSoup(r.content, 'lxml')

        all = soup.find_all('div', {'class': 'comment'})
        for every in all:
            data = []
            comment = every.find('span', {'class': 'short'}).text
            vote = every.find('span', {'class': 'votes vote-count'}).text
            info = every.find('span', {'class': 'comment-info'})
            author = info.find('a').text
            score = info.find_all('span')[1]['class'][0][-2]
            times = info.find('span', {'class': 'comment-time'})['title']
            data.append(sid)
            data.append(author)
            data.append(times)
            data.append(comment)
            data.append(vote)
            data.append(score)
            results.append(data)
            print(data)




    with open("电影短评1.csv", "a", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)
        print("         正在写入csv文件中")
        writer.writerows(results)

    print("     本电影爬取完成，下一部!!!!")




    return 0


with open("电影ID.txt", "r", encoding="utf-8", newline="") as csvfile:
    reader = csv.reader(csvfile)
    ID=[]
    id=[]
    for Row in reader:
        ID.append(str(Row))

    #print(ID)
    j=1
    for I in ID:
        print("正在获取第{}部电影".format(j))
        print("爬取电影ID为{}".format(I))
        i=str(I)
        sid = re.sub("\D", "", i)
        print("正在爬取第{}部电影".format(j))
        get_comments(sid)
        random_sleep(1.5, 0.4)
        j=j+1
