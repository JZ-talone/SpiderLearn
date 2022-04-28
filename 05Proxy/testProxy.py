# 快代理
# 西祠代理
# www.goubanjia.com
import requests

url = 'http://2022.ip138.com/'

with open('./ip.html', 'w', encoding='utf-8') as fp:
    # proxies = {
    #     "http": "http://ip:端口号"
    #             "https":"https://ip:端口号"
    # }
    # request.get(url, proxies=proxies)

    # proxies = {
    #     "http": "http://username:password@ip:端口号"
    #             "https": "https://username:password@ip:端口号"
    # }
    # request.get(url, proxies=proxies)

    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    },proxies={
        "https":'https://hpc96:2352@180.100.216.253:3037'
    })
    text = response.text
    fp.write(text)
