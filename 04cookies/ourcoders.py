import requests

login_url = 'https://ourcoders.com/user/login/'
url = 'https://ourcoders.com/user/emailsetting/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    # 'Cookie': 'PHPSESSID=3s3s2l1ovg5srhe9h7isop1a03; _ga=GA1.2.611817349.1651160591; _gid=GA1.2.232136302.1651160591; TINY4COCOA_USERID=60396; TINY4COCOA_SESSION=80345d185f97656172d24b169fcdbf46; _gat=1'
}


# 登录操作用session 登录后的所有请求都用session 会自动携带cookies

session = requests.session()

response = session.post(login_url, headers=headers, data={
    'name': 'talone',
    'password': 'qwerasdf1234',
    'submit': '登录'
})

response = session.get(url, headers=headers)
response = response.text
with  open('ourcoders.html', 'w', encoding='utf-8') as fp:
    fp.write(response)
