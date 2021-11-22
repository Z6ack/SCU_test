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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __yadk_uid=Y173snZOafljbCRbb10kfVqGzLhMVf7q; douban-fav-remind=1; douban-profile-remind=1; _ga=GA1.2.1886584236.1598363955; __utmv=30149280.22496; ct=y; push_doumail_num=0; push_noty_num=0; dbcl2="224964001:ZTkhlZL2cgo"; ck=Z9E6; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1620647394%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSlXndKoyoiQE052eRB1pgcFtfdf6zFwI29WvTWI2Koh57F2X5zYwpaxnGB1yfaGv%26wd%3D%26eqid%3Da8f7d9cd000079310000000260991de0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1886584236.1598363955.1620633771.1620647395.61; __utmc=30149280; __utmz=30149280.1620647395.61.49.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __gads=ID=810d93bb78086141:T=1620152452:S=ALNI_MY_5NoxPdng_qhjbqG3athSlAsqLg; __utmb=30149280.10.10.1620647395; _pk_id.100001.8cb4=d35eeff38e378ec6.1599987495.58.1620647977.1620636148.'}


def get_comments(sid):
    import time


    results = []

    for i in range(1):
        #print("[INFO]正在爬取第{}页的评论,还有{}页".format(i+1,24-i))

        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(sid, 40)

        rs = requests.session()
        r = rs.get(url, headers=headers)
        #random_sleep(1.5, 0.4)
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

        with  open("计网课设-电影短评.csv", "a", encoding="gb18030", newline="") as csvfile:
                writer = csv.writer(csvfile)
                print("[SUCC]正在写入csv文件中")
                writer.writerows(results)

            # print("获取成功")
    return 0

with open("id.txt", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.reader(csvfile)
        ID = []
        id = []
        error = []
        for Row in reader:
            ID.append(str(Row))

# print(ID)
j = 1
M = 0
for I in ID:
            print("[INFO]爬取电影ID为{}".format(I))
            i = str(I)
            sid = re.sub("\D", "", i)
            print("[INFO]正在爬取第{}部电影".format(j, M))
            get_comments(sid)

            random_sleep(0.5, 0.2)
            j = j + 1
