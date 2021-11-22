from tkinter import *
import urllib.request
import requests, re
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import pandas as pd
from imageio import imread
import matplotlib.pyplot as plt
import jieba


def getHtml(url):
    """获取url页面"""
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')

    return content

def cut_words(top_search):
    top_cut=[]
    for top in top_search:
        top_cut.extend(list(jieba.cut(top)))  #使用精确模式切割词汇
    return top_cut

def getComment(url):
    """解析HTML页面"""
    html = getHtml(url)
    soupComment = BeautifulSoup(html, 'html.parser')

    comments = soupComment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')

    return onePageComments


def getid(name):


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    }

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

def get_data():

    with open('电影评论.txt', 'w', encoding='utf-8') as f:
        sid=getid(_input.get())


        for page in range(5):  # 豆瓣爬取多页评论需要验证。
            url = 'https://movie.douban.com/subject/'+sid+'/comments?start=' + str(20*page) + '&limit=20&sort=new_score&status=P'


            for i in getComment(url):
                f.write(i)


    with open("电影评论.txt", "r", encoding='UTF-8') as fin1:


        all_words = cut_words(fin1)

        #定义停用词
        stop = ['的','你','了','将','为','例',' ','多','再','有','是','等','天','次','让','在','我','也','就','这样','啊','和','都','《','》','，','看','!','什么','怎么','这么','很','给','没有','不是','说'
        ,'不','吗','？','！' ,'?','。' ,'...' ,'电影','主','男','女','还','还是','又','就是','但','' ,'真个','那里','不知','两个','这么','那么','怎么','如果','是','的','这个','一个','这种','时候','什么','\n','一部','这部','没有',
        '还有','因为','只见','甚么','原来','不敢','如何','不曾','闻言','那怪','一声','出来','...','却说','片子','可以','不得','无法','这样','可能','最后','我们','东西',
        '现在','那个','所以','一直','也许','电影','它们','不能','这里','今日',"觉得",'is','感觉']
        words_cut = []
        for word in all_words:
            if word not in stop:
                words_cut.append(word)
        word_count = pd.Series(words_cut).value_counts()
        back_ground = imread("F:\\flower.jpg")
        wc = WordCloud(
                       font_path="C:\\Windows\\Fonts\\simhei.ttf", #设置字体
                       background_color="white",  #设置词云背景颜色
                       max_words=400,  #词云允许最大词汇数
                       mask=back_ground,  #词云形状
                       max_font_size=400,   #最大字体大小
                       random_state=90  #配色方案的种数
                      )
        wc1 = wc.fit_words(word_count)  #生成词云
        plt.figure()
        plt.imshow(wc1)
        plt.axis("off")
        #plt.get_current_fig_manager().full_screen_toggle()

        plt.show()
        wc.to_file("ciyun.png")

        print('succeed！\n')


app = Tk()
_input = Entry()
_input.pack()
app.title("电影评论关键词生成器")

screenwidth = app.winfo_screenwidth()
screenheight = app.winfo_screenheight()
dialog_width = 400
dialog_height = 170
# 前两个参数是窗口的大小，后面两个参数是窗口的位置
app.geometry(
    "%dx%d+%d+%d" % (dialog_width, dialog_height, (screenwidth - dialog_width) / 2, (screenheight - dialog_height) / 2))
btn = Button(text='查询', command=get_data,width=10)
btn.place(x=155, y=80)

btn.pack()


app.mainloop()


