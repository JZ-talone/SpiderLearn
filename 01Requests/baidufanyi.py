import json

import requests

kw = input('输入 kw')
url = 'https://fanyi.baidu.com/sug'
response = requests.post(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
                         , data={'kw': kw})
dic_obj = response.json()

fp = open(format('./百度翻译%s.json' % kw), 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
