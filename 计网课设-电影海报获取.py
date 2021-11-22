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


def get_picture(sid):
    result = []
    data =[]
    for i in range(1):
        # print("         正在爬取第{}页的评论,还有{}页".format(i+1,25-i))

        url = 'https://movie.douban.com/subject/{}/'.format(sid)

        rs = requests.session()
        r = rs.get(url, headers=headers)
        # random_sleep(1.5, 0.4)
        soup = BeautifulSoup(r.content, 'lxml')
        mainpic = soup.find('div', {'id': 'mainpic'})
        img = mainpic.find('img', {'rel': 'v:image'})
        Img = str(img)
        sep0 = '/public/p'
        pid = Img.split(sep0, 1)[1]
        sep1 = '.jpg"'
        pid = pid.split(sep1, 1)[0]
        #print(pid)
        url1 ='https://img9.doubanio.com/view/photo/l/public/p{}.webp'.format(pid)
        print(url1)
        data.append(sid)
        data.append(url1)
        result.append(data)
        with  open("计网课设电影海报链接.csv", "a", encoding="gb18030", newline="") as csvfile:
            writer = csv.writer(csvfile)
            print("         正在写入csv文件中")
            writer.writerows(result)


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
        print("[INFO]正在爬取第{}部电影，获取失败电影数目为{}".format(j, M))
        try:
            get_picture(sid)
        except:
            print("[ERROR]{}无法获取".format(I))
            error.append(sid)
            M = M + 1;
            # print("[ERROR]获取失败电影数目为{}".format(M))
        print(error)

        random_sleep(1.8, 0.4)
        j = j + 1
