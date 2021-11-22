from lxml import etree
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

def get_hero():
    for i in range(1,10):
        data=[]
        url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js'.format(i)
        rs = requests.session()
        r = rs.get(url, headers=headers)
        #print(r.text)
        m = r.text
        M = json.loads(m)
        #print(M)
        M1 = M["hero"]
        M2 =M['spells']
        #print(M2)

        data.append(M1['name'])
        data.append(M1['title'])
        data.append(M1['roles'])
        data.append(M1['shortBio'])
        data.append(M1['allytips'])
        data.append(M1['enemytips'])
        print("=" * 300)
        print('[英雄代号]：')
        print(M1['name'])
        print("=" * 300)
        print('[英雄名称]：')
        print(M1['title'])
        print("=" * 300)
        print('[英雄类型]：')
        print(M1['roles'])
        print("=" * 300)
        print('[英雄简介]：')
        print(M1['shortBio'])
        print("=" * 300)
        print('[使用技巧]：')
        print(M1['allytips'])
        print("=" * 300)
        print('[应对技巧]：')
        print(M1['enemytips'])
        for k in M2:
                print("=" * 300)
                print("=" * 300)
                data0=[]
                #print(k)
                data0.append(k['spellKey'])
                data0.append(k['name'])
                data0.append(k['description'])

                print('[技能键位]：')
                print(k['spellKey'])

                print('[技能名称]：')
                print(k['name'])

                print('[技能简介]：')
                print(k['description'])
        print("="*300)
        print("="*300)
                #print(data0)

if __name__ == "__main__":

    get_hero()