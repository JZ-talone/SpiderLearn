# https://chromedriver.storage.googleapis.com/index.html 驱动地址
# 驱动程序和浏览器版本映射关系

from lxml import etree
from selenium import webdriver

bro = webdriver.Chrome()

bro.get('https://pic.netbian.com/4kmeinv')

page_source = bro.page_source
tree = etree.HTML(page_source)
with open(format('./4k.html'), 'w', encoding='utf-8') as fp:
    fp.write(page_source)

pro_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
for pro in pro_list:
    picUrl = 'https://pic.netbian.com' + pro.xpath('./a/img/@src')[0]
    picName = pro.xpath('./a/b/text()')[0]
    # 转码
    # picName = picName.encode('iso-8859-1').decode('gbk')
    print(picName, picUrl)

bro.quit()
