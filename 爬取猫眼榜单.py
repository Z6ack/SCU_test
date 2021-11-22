from lxml import etree
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie':'HMACCOUNT_BFESS=1D8B36EF623B3FB0; BDUSS_BFESS=GttM1lYWVBBZXBtQm5LZ1Q4czNrUVJyaG9jREpQTFBNSzI1THQ0WGFoMEJRalpnRVFBQUFBJCQAAAAAAAAAAAEAAACEgcebAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG1DmABtQ5gU; BAIDUID_BFESS=38CE0126C34B31C1B515A735448A1EE9:FG=1; BDSFRCVID_BFESS=9MuOJexroG0YyxOHhIeAM0qTWFweG7bTDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR3aQ5rtKRTffjrnhPF3DlbQXP6-hnjy3bRkX4nvWnnzej6EDbQx3UKWbttf5q3RymJJ2-39LPO2hpRjyxv4y4Ldj4oxJpOJ-bCL0p5aHl51fbbvbURvW--g3-7fJU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoCvt-5rDHJTg5DTjhPrMWhQCWMT-MTryKKJwM4QCObnVbj5YDb_73PjfKx-fKHnRhlRNB-3iV-OxDUvnyxAZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPUWMJ9LUvftgcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtCvDqTrP-trf5DCShUFs55ctB2Q-XPoO3KJZJtQ-y-7zbtIIDhQnLM5f5mkf3fbgylRp8P3y0bb2DUA1y4vpBtQmJeTxoUJ2-KDVeh5Gqfo15-0ebPRiXPb9QgbfopQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hDvPKITD-tFO5eT22-usLe5C2hcHMPoosIJX2J7cy-kPbqouJnonQ2cf0l05KfbUoqRmXnJi0btQDPvxBf7pWDTm_q5TtUJMqIDzbMohqfLn5MOyKMniyIv9-pn5tpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjRDKICV-frb-C62aKDsoK37BhcqJ-ovQT3Z2JKwyM7AKRjutT6n-hQ55l0bHxbeWfvpXn-R0hbjJM7xWeJpaJ5nJq5nhMJmKTLVbML0qto7-P3y523ihn3vQpnbhhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQfl6h8pcN2b5oQT842q79BPvA5m6uoPjmQhQbeq06-lOUWfA3XpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvcyn3cShn6DMjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60ttJIj3e'

}

def get_sina_news_serach():
    result=[]
    for i in range(0,11):

      url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
      rs = requests.session()
      r = rs.get(url, headers=headers)
      r.encoding = 'utf-8'
      trees = etree.HTML(r.text)
      for j in range(0,11):
        data = []
        name = trees.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[{}]/a/img[2]/@alt'.format(j))
        actor  = trees.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[2]/text()'.format(j))
        for Actor in actor:
          Actor = re.sub('[ \n   \\\ n \ n 。 \']]', '', Actor)
          Actor = re.sub(' ', '', Actor)
          Actor = re.sub('\n', '', Actor)
        time = trees.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[1]/p[3]/text()'.format(j))
        for Time in time:
          Time = re.sub('[ \n   \\\ n \ n 。 \']]', '', Time)
          Time = re.sub(' ', '',Time)
        score1 = trees.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[2]/p/i[1]/text()'.format(j))
        score2 = trees.xpath('//*[@id="app"]/div/div/div[1]/dl/dd[{}]/div/div/div[2]/p/i[2]/text()'.format(j))
        data.append(name[0])
        data.append(Actor)
        data.append(Time)
        data.append(score1[0]+score2[0])
        print(i*10+j,data)
        time.sleep(3)


if __name__ == "__main__":

  get_sina_news_serach()

