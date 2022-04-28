# re bs4 xpath 四种解析 xpath最通用
# download 4k图片
import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
for i in range(1,10):
    response = requests.get(url='https://pic.netbian.com/4kmeinv/index_%s.html'%i, headers=header)
    # response.encoding = 'utf-8'
    response = response.text

    with open(format('./4k.html'), 'w', encoding='utf-8') as fp:
        fp.write(response)

    tree = etree.HTML(response)
    pro_list = tree.xpath('//ul[@class="clearfix"]/li')
    for pro in pro_list:
        picUrl = 'https://pic.netbian.com' + pro.xpath('./a/img/@src')[0]
        picName = pro.xpath('./a/b/text()')[0]
        picName = picName.encode('iso-8859-1').decode('gbk')
        print(picName, picUrl)
        with open('./4k/picName%s.jpg' % picName, 'wb') as fp:
            fp.write(requests.get(url=picUrl, headers=header).content)
