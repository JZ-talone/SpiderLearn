# re bs4 xpath 四种解析 xpath最通用
# 58二手房
import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
response = requests.get(url='https://sh.58.com/ershoufang/', headers=header).text

with open(format('./58.html'),'w',encoding='utf-8') as fp:
    fp.write(response)

tree = etree.HTML(response)
pro_list = tree.xpath('//div[@class="property"]')
fp = open('./58data.txt','w',encoding='utf-8')
for pro in pro_list:
    item = {
        'detailUrl':pro.xpath('./a/@href'),
        'picUrl':pro.xpath('./a/div[@class="property-image"]/img/@data-src'),
        'title':pro.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0],# 注意xpath的index从1开始！
        'price':''.join(pro.xpath('./a/div[2]/div[2]/p[1]//text()'))
    }
    fp.write(str(item))
