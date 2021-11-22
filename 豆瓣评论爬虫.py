from bs4 import BeautifulSoup
import requests
import re
import csv
from lxml import etree

def get_id():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; __yadk_uid=jzEoWO17iCvSuRyEtWKPKwMyMe254hG0; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __utmv=30149280.22496; __gads=ID=810d93bb78086141-2231882d95c4003d:T=1604624971:S=ALNI_MZBGDy2M9kYj9hpvHo36w4qc8rgkA; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1611419309.22.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmz=223695111.1611419320.20.17.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; dbcl2="224964001:TUiHbnT1naY"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1611422710%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E4%25B8%2580%25E6%25AD%25A5%25E4%25B9%258B%25E9%2581%25A5%22%5D; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1611422710; __utma=30149280.1886584236.1598363955.1611419309.1611422710.23; __utmc=30149280; __utma=223695111.742097452.1598363955.1611419320.1611422710.21; __utmb=223695111.0.10.1611422710; __utmc=223695111; ck=y0-X; _pk_id.100001.4cf6=e57cefa1643f0b82.1598363955.21.1611422973.1611420631.'
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; __yadk_uid=jzEoWO17iCvSuRyEtWKPKwMyMe254hG0; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __utmv=30149280.22496; __gads=ID=810d93bb78086141-2231882d95c4003d:T=1604624971:S=ALNI_MZBGDy2M9kYj9hpvHo36w4qc8rgkA; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; __utmz=30149280.1611419309.22.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utmz=223695111.1611419320.20.17.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; dbcl2="224964001:TUiHbnT1naY"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1611422710%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E4%25B8%2580%25E6%25AD%25A5%25E4%25B9%258B%25E9%2581%25A5%22%5D; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1611422710; __utma=30149280.1886584236.1598363955.1611419309.1611422710.23; __utmc=30149280; __utma=223695111.742097452.1598363955.1611419320.1611422710.21; __utmb=223695111.0.10.1611422710; __utmc=223695111; ck=y0-X; _pk_id.100001.4cf6=e57cefa1643f0b82.1598363955.21.1611422973.1611420631.'
    }

    results = []

    for i in range(25):
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(sid, str(
            i * 20))

        rs = requests.session()

        r = rs.get(url, headers=headers)
        r.encoding = 'utf-8'
        trees = etree.HTML(r.text)
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
            runningtime = re.sub('[\n \\\ n \ n  \']', '', runningtime)
        Showtime = trees.xpath('//*[@id="content"]/div/div[2]/div[1]/div/span/p[6]/text()')
        for showtime in Showtime:
            showtime = re.sub('[\n \\\ n \ n  \']', '', showtime)
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
            data.append(author)
            data.append(time)
            data.append(comment)
            data.append(vote)
            data.append(score)
            data.append(director)
            data.append(actor)
            data.append(kind)
            data.append(runningtime)
            data.append(where)
            data.append(showtime)
            results.append(data)

    return results


if __name__ == '__main__':
    with open("豆瓣短评.csv", "w", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([''])
        sid = get_id()
        results = get_comments(sid)
        for i in results:
            print(i)

        writer.writerows(results)



    print('succeed！\n')