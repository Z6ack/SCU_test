from bs4 import BeautifulSoup
import requests
import re
import time
import csv


def get_id(movie_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    }


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

if __name__ == '__main__':
    with open("电影清单.txt", "r", encoding="utf-8", newline="") as csvfile:
        reader = csv.reader(csvfile)
        data =[]
        for Row in reader:
            for row in Row:
                row = re.sub('[\n \\\ n \ n  \']]', '', row)
            movie_name=str(row)
            d =get_id(movie_name)
            time.sleep(1)
            print(d)
            data.append(str(d))

        print(data)

    with open("电影ID.txt","w",encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for line in data:
            csvfile.write(line + '\n')

