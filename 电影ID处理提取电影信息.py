from lxml import etree
import requests
import re
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}



def get_films(sid):

    film = []

    url = 'https://movie.douban.com/subject/{}/comments?status=P'.format(sid)

    rs = requests.session()

    r = rs.get(url, headers=headers)
    r.encoding = 'utf-8'
    trees = etree.HTML(r.text)
    Names = trees.xpath('//*[@id="content"]/h1/text()')
    for names in Names:
            names = re.sub('[\n \\\ n \ n 。 \']]', '', names)
            names = names[:-3]
    Director = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[1]/a/text()')
    for director in Director:
            director = re.sub('[\n \\\ n \ n  \']]', '', director)
    Actor = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[2]/a[1]/text()')
    for actor in  Actor:
            actor = re.sub('[\n \\\ n \ n  \']]', '',actor)
    Kind = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[3]/text()')
    for kind in Kind:
            kind = re.sub('[\n \\\ n \ n  \']', '', kind)
    Where = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[4]/text()')
    for where in Where:
            where= re.sub('[\n \\\ n \ n  \']', '', where)
    Runningtime = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[5]/text()')
    for runningtime in Runningtime:
            runningtime = re.sub('[\n \\\ n \ n 分钟  \']', '', runningtime)
    Showtime = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[6]/text()')
    for showtime in Showtime:
            showtime = re.sub('[\n \\\ n \ n  \']', '', showtime)

    datas = []
    datas.append(names)
    datas.append(sid)
    datas.append(director)
    datas.append(actor)
    datas.append(kind)
    datas.append(runningtime)
    datas.append(where)
    datas.append(showtime)
    film.append(datas)

    with open("电影信息1.csv", "a", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(film)




    return 0





with open("电影ID.txt", "r", encoding="utf-8", newline="") as csvfile:
    reader = csv.reader(csvfile)
    ID=[]
    id=[]
    for Row in reader:
        ID.append(str(Row))

    print(ID)
    j=1
    for I in ID:
        #print(I)
        print("正在获取第{}部电影".format(j))
        i=str(I)
        sid = re.sub("\D", "", i)
        print(sid)
        get_films(sid)
        time.sleep(1)

        j+=1