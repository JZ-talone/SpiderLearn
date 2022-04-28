import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'
start = 0
response = requests.get(url=url, params={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}).json()
fp = open(format('./doubanmovie.json'), 'w', encoding='utf-8')
json.dump(response, fp=fp, ensure_ascii=False)
