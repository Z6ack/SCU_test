import requests
import re
import csv

# username = ''
# password = ''

def get_post(username,password):
    info = {
        'username': username,
        'password': password
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
    print('[INFO]:正在进行Cookie获取')
    rs = requests.session()
    url_cookie='https://wfw.scu.edu.cn/a_scu/api/sso/check'
    r = rs.post(url_cookie, data=info, headers=headers, timeout=3).json()
    if(r['m']=='操作成功'):
        print('[INFO]:Cookie获取成功')
    else:
        print('[ERROR]:Cookie获取失败，请检查密码账号是否正确以及网络情况')
        return 0

    url_put= 'https://wfw.scu.edu.cn/ncov/wap/default/index'
    r1 = rs.get(url_put, headers=headers)
    info = re.findall(r'.*?oldInfo: (.*),.*?', r1.text)
    data = eval(info[0])
    #print(data)
    try:
        print('[INFO]:正在进行填报')
        url_post='https://wfw.scu.edu.cn/ncov/wap/default/save'
        Return = rs.post(url=url_post, headers=headers, data=data)
        Return = Return.json()
        print("[INFO]:今日填报结果：" + Return['m'])

    except:
        print("[ERROR]:填写失败或填写内容已改动，本次请手动填报")


def info():
    try:
        print('[INFO]:正在进行信息读取')
        with open("info.txt", "r", encoding="utf-8", newline="") as csvfile:
            reader = csv.reader(csvfile)
            info = []
            for Row in reader:
                info.append(Row)
    except:
        print('[ERROR]:读取信息失败')
        return 0
    if(info==None):
        print('[ERROR]:信息未成功写入，请重新写入')
        return 0
    print('[INFO]:信息读取成功')
    return info


if __name__ == "__main__":
    print("=" * 500)
    print("[INFO]:欢迎使用zack一体化自动填报程序")
    info=info()
    get_post(info[0],info[1])
    print("=" * 500)
