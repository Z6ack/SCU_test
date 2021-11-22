import requests
from bs4 import BeautifulSoup
import re


def get_type_movie(id):
    url_1 = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id={}:{}&action=&start=0&limit={}'
    url_2 = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=10:0'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie': 'll="118282"; bid=Lmd2_GV0fPU; _vwo_uuid_v2=D5E30EF9DDF921DEA6B93ED820A9E708D|89659bac52ff0db762259e613146c871; __yadk_uid=Y173snZOafljbCRbb10kfVqGzLhMVf7q; douban-fav-remind=1; douban-profile-remind=1; _ga=GA1.2.1886584236.1598363955; __utmv=30149280.22496; ct=y; push_doumail_num=0; push_noty_num=0; dbcl2="224964001:ZTkhlZL2cgo"; ck=Z9E6; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1620647394%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DSlXndKoyoiQE052eRB1pgcFtfdf6zFwI29WvTWI2Koh57F2X5zYwpaxnGB1yfaGv%26wd%3D%26eqid%3Da8f7d9cd000079310000000260991de0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1886584236.1598363955.1620633771.1620647395.61; __utmc=30149280; __utmz=30149280.1620647395.61.49.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; __gads=ID=810d93bb78086141:T=1620152452:S=ALNI_MY_5NoxPdng_qhjbqG3athSlAsqLg; __utmb=30149280.10.10.1620647395; _pk_id.100001.8cb4=d35eeff38e378ec6.1599987495.58.1620647977.1620636148.'}

    first = []
    j = 1
    for i in range(9, 0, -1):
        r = requests.get(url_1.format(id, i*10, i*10-10, 1), headers=header)
        first.append(r.json()[0]['rank'] - j)
        j = r.json()[0]['rank']
    r = requests.get(url_2.format(id), headers=header)
    count = r.json()['total']-1
    first.append(count)
    with open('id.txt', "a+") as f:
        for i in range(10, 0, -1):
            r = requests.get(url_1.format(id, i*10, i*10-10, first[10-i]), headers=header)
            for j in r.json():
                f.write(str(j['id'])+"\n")
            print(len(r.json()))


if __name__ == '__main__':
    for i in [30]:#
        get_type_movie(i)
 #[3,5,13,15]