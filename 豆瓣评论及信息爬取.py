from bs4 import BeautifulSoup
import requests
import re
import csv
from lxml import etree


def get_id():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    }
    movie_name = str(input("please input the name of movie:"))

    params = {
        "q": movie_name
    }

    search_url = "https://www.douban.com/search"
    r = requests.get(search_url, params=params, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')
    first_movie_info = soup.find('a', {'class': 'nbg'})['onclick']
    pattern = re.compile('\d{4,}')

    sid = str(pattern.search(first_movie_info).group())

    return (sid)


def get_comments(sid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __utmv=30149280.22496; __gads=ID=810d93bb78086141-2231882d95c4003d:T=1604624971:S=ALNI_MZBGDy2M9kYj9hpvHo36w4qc8rgkA; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; douban-profile-remind=1; ap_v=0,6.0; __utma=30149280.1886584236.1598363955.1611481312.1612259964.27; __utmc=30149280; __utmz=30149280.1612259964.27.24.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="224964001:SjEAlUsWSbw"; ck=86pM; __utmb=30149280.30.10.1612259964'
    }

    results = []

    for i in range(26):
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(sid, str(i*20))

        rs = requests.session()
        r = rs.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        all = soup.find_all('div', {'class': 'comment'})
        for every in all:
            data = []
            comment = every.find('span', {'class': 'short'}).text
            vote = every.find('span', {'class': 'votes vote-count'}).text
            info = every.find('span', {'class': 'comment-info'})
            author = info.find('a').text
            score = info.find_all('span')[1]['class'][0][-2]
            time = info.find('span', {'class': 'comment-time'})['title']
            data.append(sid)
            data.append(author)
            data.append(time)
            data.append(comment)
            data.append(vote)
            data.append(score)
            results.append(data)
    return results

def get_films(sid):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        }
    film = []

    for i in range(1):
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(sid, str(
            i * 20))

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

    return film

if __name__ == '__main__':
    sid = get_id()
    results = get_comments(sid)
    film =get_films(sid)
    with open("电影短评.csv", "a", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(results)

    with open("电影信息.csv", "a", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerows(film)

    print('succeed！\n')
