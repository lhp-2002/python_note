import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}


# 请求内容的网址
catalogueUrl = 'https://youyouxs.com/xs_383853/zj_15000729'
# 发送请求
catalogueResponse = requests.get(catalogueUrl, headers=headers)
# 获取到的数据
catalogue_html_data = catalogueResponse.text
# 使用正则匹配，获取自己想要的内容
catalogueContent = re.findall('href="(.*?)">下一页</a>', catalogue_html_data)
if not catalogueContent :
    catalogueContent = re.findall('href="(.*?)">下一章</a>', catalogue_html_data)

UrlConText1 = catalogueContent[0]

count = 0

while count < 200:
    catalogueUrl2 = 'https://youyouxs.com' + str(UrlConText1)
    catalogueResponse2 = requests.get(catalogueUrl2, headers=headers)
    catalogue_html_data2 = catalogueResponse2.text
    catalogueContent2 = re.findall('href="(.*?)">下一页</a>', catalogue_html_data2)
    if not catalogueContent2 :
        catalogueContent2 = re.findall('href="(.*?)">下一章</a>', catalogue_html_data2)

    UrlConText1 = catalogueContent2[0]

    content = re.findall('<p>(.*?)</p>', catalogue_html_data2)

    # 删除第一个元素
    content.pop(0)
    # 把标题加在文章最前面，在把数组连接成字符串并换行
    textContent = "\n".join(content) + '\n\n'
    print(textContent)
    # 将内容写入txt文件中
    txt = open(' 遮天：我王腾真没大帝之姿.txt', mode='a', encoding='utf-8')
    txt.write(textContent)

    count += 1

exit()