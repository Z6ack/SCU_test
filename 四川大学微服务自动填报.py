import requests
import  re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie':'Hm_lvt_48b682d4885d22a90111e46b972e3268=1637418063; UUkey=169b741a5f6334e302746919ff63bf84; eai-sess=h8th8dt001a2piu36s86klfn82; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1637418155'
}

def get_post():
    url = 'https://wfw.scu.edu.cn/ncov/wap/default/index'
    rs = requests.session()
    r = rs.get(url, headers=headers)
    try:
        info = re.findall(r'.*?oldInfo: (.*),.*?', r.text)
    except:
        print("[ERROR]:Cookie已过期，请手动更新")
        return 0
    data = eval(info[0])
    try:
        Return =requests.post('https://wfw.scu.edu.cn/ncov/wap/default/save', headers=headers, data=data)
        Return=Return.json()
        print("[INFO]:今日填报结果："+Return['m'])
    except:
        print("[ERROR]:填写内容已改动，本次请手动填报")

if __name__ == "__main__":
    print("="*500)
    print("[INFO]:欢迎使用一体化自动填报程序\n[INFO]:请载手动添加cookie后再次载入本程序\n[INFO]:如以添加请忽视")
    get_post()
    print("=" * 500)