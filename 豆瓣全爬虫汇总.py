from bs4 import BeautifulSoup
import requests
import re
import csv
import time
import random


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __yadk_uid=Y173snZOafljbCRbb10kfVqGzLhMVf7q; douban-fav-remind=1; douban-profile-remind=1; _ga=GA1.2.1886584236.1598363955; __utmv=30149280.22496; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1628068360%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D16Y1j7xsEx0vmPjzPuCiJOsiL4LDdjt0Z8h0N93joZdHCIKVL5RQg04DTsBDv_9j%26wd%3D%26eqid%3Da77be2970004d3ab00000002610a5a06%22%5D; _pk_ses.100001.8cb4=*; __utmc=30149280; __utma=30149280.1886584236.1598363955.1621764470.1628068361.84; __utmz=30149280.1628068361.84.61.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="224964001:qLJoGcl0Dmw"; ck=Su3k; ap_v=0,6.0; __gads=ID=810d93bb78086141:T=1624792211:S=ALNI_Mbpf0SJrat6bHGJHnKr0cg7XdBfVQ; push_noty_num=0; push_doumail_num=0; _pk_id.100001.8cb4=d35eeff38e378ec6.1599987495.83.1628068408.1624792208.; __utmb=30149280.7.10.1628068361; ct=y'}





def get_single_id(name):
    movie_name = name
    params = {
        "q": movie_name
    }
    search_url = "https://www.douban.com/search"
    r = requests.get(search_url, params=params, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    first_movie_info = soup.find('a', {'class': 'nbg'})['onclick']
    pattern = re.compile('\d{4,}')
    sid = str(pattern.search(first_movie_info).group())

    return(sid)


def get_films_info(sid):
        results = []
        for i in range(1):
            # print("         正在爬取第{}页的评论,还有{}页".format(i+1,25-i))

            url = 'https://movie.douban.com/subject/{}/'.format(sid)

            rs = requests.session()
            r = rs.get(url, headers=headers)
            # random_sleep(1.5, 0.4)
            soup = BeautifulSoup(r.content, 'lxml')

            names = soup.find('span', {'property': 'v:itemreviewed'}).text
            info = soup.find('div', {'id': 'info'})
            Info = info.text
            # print(Info)

            Story = soup.find('span', {'property': 'v:summary'}).text
            story = re.sub('[  1\u3000\n]', '', Story)

            points = soup.find('strong', {'property': 'v:average'}).text

            vote_people = soup.find('span', {'property': 'v:votes'}).text

            short_comment_people = soup.find('a', {
                'href': 'https://movie.douban.com/subject/{}/comments?status=P'.format(sid)}).text

            comment_people = soup.find('a', {'href': 'reviews'}).text
            try:
                Where = re.search(r'制片国家/地区: (.*)', Info, re.M | re.I)
                where = Where.group(1)
            except:
                where = ''
            try:
                Director = re.search(r'导演: (.*)', Info, re.M | re.I)
                director = Director.group(1)
            except:
                director = ''
            try:
                Writer = re.search(r'编剧: (.*)', Info, re.M | re.I)
                writer = Writer.group(1)
            except:
                writer = ''
            try:
                Actor = re.search(r'主演: (.*)', Info, re.M | re.I)
                actor = Actor.group(1)
            except:
                actor = ''
            try:
                Kind = re.search(r'类型: (.*)', Info, re.M | re.I)
                kind = Kind.group(1)
            except:
                kind = ''
            try:
                Lang = re.search(r'语言: (.*)', Info, re.M | re.I)
                lang = Lang.group(1)
            except:
                lang = ''
            try:
                Runtime = re.search(r'片长: (.*)', Info, re.M | re.I)
                runtime = Runtime.group(1)
            except:
                runtime = ''
            try:
                Showtime = re.search(r'上映日期: (.*)', Info, re.M | re.I)
                showtime = Showtime.group(1)
            except:
                showtime = ''

            try:
                Othername = re.search(r'又名: (.*)', Info, re.M | re.I)
                othername = Othername.group(1)
            except:
                othername = ''

            datas = []
            datas.append(sid)
            datas.append(names)
            datas.append(story)
            datas.append(director)
            datas.append(writer)
            datas.append(actor)
            datas.append(kind)
            datas.append(where)
            datas.append(lang)
            datas.append(showtime)
            datas.append(runtime)
            datas.append(othername)
            datas.append(points)
            datas.append(vote_people)
            datas.append(short_comment_people)
            datas.append(comment_people)
            #print(datas)

            results.append(datas)
        return results


def get_the_file_comments(sid):
    def getthecomment(id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __yadk_uid=Y173snZOafljbCRbb10kfVqGzLhMVf7q; douban-fav-remind=1; douban-profile-remind=1; _ga=GA1.2.1886584236.1598363955; __utmv=30149280.22496; ct=y; push_doumail_num=0; push_noty_num=0; dbcl2="224964001:ZTkhlZL2cgo"; ck=Z9E6; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1620647394%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSlXndKoyoiQE052eRB1pgcFtfdf6zFwI29WvTWI2Koh57F2X5zYwpaxnGB1yfaGv%26wd%3D%26eqid%3Da8f7d9cd000079310000000260991de0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1886584236.1598363955.1620633771.1620647395.61; __utmc=30149280; __utmz=30149280.1620647395.61.49.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __gads=ID=810d93bb78086141:T=1620152452:S=ALNI_MY_5NoxPdng_qhjbqG3athSlAsqLg; __utmb=30149280.10.10.1620647395; _pk_id.100001.8cb4=d35eeff38e378ec6.1599987495.58.1620647977.1620636148.'}

        url = 'https://movie.douban.com/j/review/{}/full'.format(id)

        rs = requests.session()
        r = rs.get(url, headers=headers)
        r.encoding = 'utf-8'

        # pre = re.compile('>(.*?)<')
        # s1 = ''.join(pre.findall(r.text))
        sep = '},"html":"'
        rest = r.text.split(sep, 1)[1]
        # rest=re.sub('[\n]', '', rest)
        # rest=re.sub('[<br>]', '', rest)
        # rest=re.sub('[&nbsp;]', '', rest)
        # rest = re.sub('/', '', rest)
        # rest = re.sub('\\\\', '', rest)
        rest = re.sub('[\n <br> &nbsp; / \\\\]', '', rest)
        return rest
    results = []

    for i in range(1):
        #print("         正在爬取第{}页的评论,还有{}页".format(i+1,25-i))

        url = 'https://movie.douban.com/subject/{}/reviews'.format(sid)

        rs = requests.session()
        r = rs.get(url, headers=headers)
        #random_sleep(1.5, 0.4)
        soup = BeautifulSoup(r.content, 'lxml')

        all = soup.find_all('div', {'class': 'main review-item'})
        m=0;
        for every in all:
            m=m+1;
            id = every.find_all('div')[1]['id'][7:15]
            #print(id)
            comment=getthecomment(id)
            data = []

            info01 = every.find('header', {'class': 'main-hd'})
            author = info01.find('a',{'class':'name'}).text
            score = info01.find_all('span')[0]['class'][0][-2]
            times = info01.find('span', {'class': 'main-meta'}).text
            info02 = every.find('div', {'class': 'main-bd'})
            title = info02.find('h2').text
            action01 = info02.find('a',{'class':'action-btn up'})
            Useful = action01.find('span').text
            useful = re.sub('[\n ]', '', Useful)
            action02 = info02.find('a',{'class':'action-btn down'})
            Useless = action02.find('span').text
            useless = re.sub('[\n ]', '', Useless)
            Rely = info02.find('a',{'class':'reply'}).text


            data.append(sid)
            data.append(author)
            data.append(score)
            data.append(times)
            data.append(useful)
            data.append(useless)
            data.append(Rely)
            data.append(title)
            data.append(comment)
            print(data)
            results.append(data)


            if(m==10):
                break
    return results

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

    return results


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
        #print(url1)
        data.append(sid)
        data.append(url1)
        result.append(data)

    return result







def get_id_list():
    with open("id.txt", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.reader(csvfile)
        ID = []

        for Row in reader:
            ID.append(str(Row))
    return ID


def write_csv(result,name):
    with  open("{}.csv".format(name), "a", encoding="gb18030", newline="") as csvfile:
        writer = csv.writer(csvfile)
        print("         正在写入csv文件中")
        writer.writerows(result)



def random_sleep(mu, sigma):
    '''正态分布随机睡眠
    :param mu: 平均值
    :param sigma: 标准差，决定波动范围
    '''
    secs = random.normalvariate(mu, sigma)
    if secs <= 0:
        secs = mu  # 太小则重置为平均值
    time.sleep(secs)



def main():
    print_menu1()
    while True:
        # 获取用户输入
        try:
            num = int(input("请输入需要的操作："))
        except ValueError:
            # except Exception:
            print("输入错误，请重新输入（1.2.3）")
            continue
        except IndexError:
            print("请输入一个有效值：（1.2.3）")
            continue
        # 根据用户的数据执行相应的功能
        if num == 1:
            single()
            print_menu1()
        elif num == 2:
            more()
            print_menu1()
        elif num == 3:
            break
        else:
            print("输入错误")





def single():

    print_menu21()
    while True:
        # 获取用户输入
        try:
            num = int(input("请输入需要的操作："))
        except ValueError:
            # except Exception:
            print("输入错误，请重新输入（1.2.3.4.5.6）")
            continue
        except IndexError:
            print("请输入一个有效值：（1.2.3.4.5.6）")
            continue
        # 根据用户的数据执行相应的功能
        if num == 1:
            try:
                name=get_filmname()
                id=get_single_id(name)
                info=get_films_info(id)
                for i in info:
                    for j in i:
                        print(j)
            except:
                print('error')
            input()
            print_menu21()

        elif num == 2:
            try:
                name = get_filmname()
                id = get_single_id(name)
                com =get_the_file_comments(id)
                for i in com:
                        print(i)
            except:
                print('error')

            input()
            print_menu21()

        elif num == 3:
            try:
                name = get_filmname()
                id = get_single_id(name)
                com = get_comments(id)
                for i in com:
                        print(i)
            except:
                print('error')
            input()
            print_menu21()

        elif num == 4:
            try:
                name = get_filmname()
                id = get_single_id(name)
                pic =get_picture(id)
                print(pic)
            except:
                print('error')
            input()
            print_menu21()
        elif num == 5:
            print_menu21()
        elif num == 6:
            break
        else:
            print("输入错误")


def more():

    print_menu22()
    ID=get_id_list()
    while True:
        # 获取用户输入
        try:
            num = int(input("请输入需要的操作："))
        except ValueError:
            # except Exception:
            print("输入错误，请重新输入（1.2.3.4.5.6）")
            continue
        except IndexError:
            print("请输入一个有效值：（1.2.3.4.5.6）")
            continue
        if num <= 4:
            j = 1

            try:
                    if (num == 1):
                        with  open("电影信息.csv", "a", encoding="gb18030", newline="") as csvfile:
                         j = 1
                         for I in ID:
                            print("[INFO]爬取电影ID为{}".format(I))
                            i = str(I)
                            sid = re.sub("\D", "", i)
                            print("[INFO]正在爬取第{}部电影".format(j))
                            result = get_films_info(sid)
                            print(result)
                            random_sleep(0.8, 0.4)
                            j = j + 1
                            writer = csv.writer(csvfile)
                            print("正在写入csv文件中")
                            writer.writerows(result)
                    if (num == 2):
                        with  open("电影影评.csv", "a", encoding="gb18030", newline="") as csvfile:
                            j = 1
                            for I in ID:
                                print("[INFO]爬取电影ID为{}".format(I))
                                i = str(I)
                                sid = re.sub("\D", "", i)
                                print("[INFO]正在爬取第{}部电影".format(j))
                                result = get_the_file_comments(sid)
                                print(result)
                                random_sleep(0.8, 0.4)
                                j = j + 1
                                writer = csv.writer(csvfile)
                                print("正在写入csv文件中")
                                writer.writerows(result)
                    if (num == 3):
                        with  open("电影短评.csv", "a", encoding="gb18030", newline="") as csvfile:
                            j = 1
                            for I in ID:
                                print("[INFO]爬取电影ID为{}".format(I))
                                i = str(I)
                                sid = re.sub("\D", "", i)
                                print("[INFO]正在爬取第{}部电影".format(j))
                                result = get_comments(sid)
                                print(result)
                                random_sleep(0.8, 0.4)
                                j = j + 1
                                writer = csv.writer(csvfile)
                                print("正在写入csv文件中")
                                writer.writerows(result)
                    if (num == 4):
                        with  open("电影海报.csv", "a", encoding="gb18030", newline="") as csvfile:
                            j = 1
                            for I in ID:
                                print("[INFO]爬取电影ID为{}".format(I))
                                i = str(I)
                                sid = re.sub("\D", "", i)
                                print("[INFO]正在爬取第{}部电影".format(j))
                                result = get_picture(sid)
                                print(result)
                                random_sleep(0.8, 0.4)
                                j = j + 1
                                writer = csv.writer(csvfile)
                                print("正在写入csv文件中")
                                writer.writerows(result)
            except:
                print("[ERROR]:出错请检查".format(I))


                random_sleep(1.8, 0.4)
                j = j + 12

        elif num == 5:
            pass
        elif num == 6:
            break
        else:
            print("输入错误")



def print_menu1():

    print ("="*100)
    print ("1. 单部电影检索查看")
    print ("2. 多部电影检索查看并保存结果")
    print ("3. 退出系统")
    print("=" * 100)
    print ("****注意：操作2为将对应的txt文本中的所有id对应的电影相关进行获取，主要用于爬取大量数据                         ****")
    print ("****注意：操作3的工作量较为繁杂，不建议大量使用                                                         ****")
    print("=" * 100)

def print_menu21():

    print ("="*50)
    print ("1. 获取电影详细信息")
    print ("2. 获取电影影评及评论相关信息")
    print ("2. 获取电影短评及评论相关信息")
    print ("4. 获取电影海报")
    print ("5. 显示所有选项")
    print ("6. 退出系统")
    print("=" * 50)

def get_filmname():
    print("=" * 50)
    name=input('请输入你想要查询的电影名称:')
    print("=" * 50)
    return(name)


def print_menu22():

    print ("="*50)
    print ("1. 获取电影详细信息")
    print ("2. 获取电影影评及评论相关信息")
    print ("3. 获取电影短评及评论相关信息")
    print ("4. 获取电影海报")
    print ("5. 显示所有选项")
    print ("6. 退出系统")
    print("=" * 50)


if __name__ == "__main__":
    print("欢迎使用zack的豆瓣电影查询系统")
    main()

