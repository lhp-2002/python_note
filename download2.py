import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}

catalogueData = []
for value in range(3):
    values = value + 4
    # 章节目录解析
    # 请求内容的网址
    catalogueUrl = 'http://www.mianfeizhuishu.com/6200_692279/Page/'+ str(values) +'/'
    # 发送请求
    catalogueResponse = requests.get(catalogueUrl)
    # 防止乱码
    catalogueResponse.encoding = catalogueResponse.apparent_encoding
    # 获取到的数据
    catalogue_html_data = catalogueResponse.text
    # 使用正则匹配，获取自己想要的内容
    catalogueContent = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', catalogue_html_data)
    # 把改好的数据写入新的数组
    catalogueData.append(catalogueContent)

# 将分页的目录结合在一个数组中，方便管理
catalogueDataInfo = []
for infoValue in catalogueData:
    for infoKeyTu, infoValueTu in enumerate(infoValue):
        # 排除每页最新推荐章节
        if infoKeyTu >= 9:
            # 把处理好的数据，重新存入数组
            catalogueDataInfo.append(infoValueTu)

for catalogueKey, catalogueValue in enumerate(catalogueDataInfo):
    # 章节内容解析
    # 请求内容的网址
    url = 'http://www.mianfeizhuishu.com' + catalogueValue[0]
    # 发送请求
    response = requests.get(url, headers=headers, timeout=5)
    # 防止乱码
    response.encoding = response.apparent_encoding
    # 获取到的数据
    html_data = response.text
    # .*?  可以替代任意字符
    # re.S 允许匹配换行符
    content = re.findall('<p>(.*?)</p>', html_data)
    # 删除最后二位元素
    contentList = content[:-2]
    # 把标题加在文章最前面，在把数组连接成字符串并换行
    textContent = catalogueValue[1] + "\n" + "\n".join(contentList) + '\n\n'
    print(textContent)
    # 将内容写入txt文件中
    txt = open('开局斗破当配角.txt', mode='a', encoding='utf-8')
    txt.write(textContent)