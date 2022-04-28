import requests
url = 'https://www.sogou.com/'
response = requests.get(url=url)
print(response.text)
with open('./sogou.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

kw = input('输入 kw')
url = 'https://www.sogou.com/web'
with open(format('./sogoukw%s.html'%kw),'w',encoding='utf-8') as fp:

    fp.write(requests.get(url,params={
        'query':kw
    },headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}).text)