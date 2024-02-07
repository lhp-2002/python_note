import requests
import re
# 章节目录解析
# 请求内容的网址
catalogueUrl = 'http://www.xsbiquge.la/book/36039/'
# 发送请求
catalogueResponse = requests.get(catalogueUrl)
# 获取到的数据
catalogue_html_data = catalogueResponse.text
# 使用正则匹配，获取自己想要的内容
catalogueContent = re.findall('<a href="/book/36039/(.*?).html">', catalogue_html_data)
# 获取所有目录地址和内容
for catalogueKey, catalogueValue in enumerate(catalogueContent):
# 把不需要的章节去除  511对应494章节
    if catalogueKey > 511:
        # 章节内容解析
        # 请求内容的网址
        url = 'http://www.xsbiquge.la/book/36039/'+  catalogueValue +'.html'
        # 发送请求
        response = requests.get(url)
        # 获取到的数据
        html_data = response.text
        # .*?  可以替代任意字符
        titleContent = re.findall('<title>(.*?)_都重生了谁谈恋爱啊_都市小说_新笔趣阁</title>', html_data)[0]
        # re.S 允许匹配换行符
        content = re.findall('<p class="content_detail">(.*?)</p>', html_data, re.S)
        # 第一条数据标题
        contentData = [titleContent]
        # 过滤特殊符号，换行，空格等
        for value in content:
        # 把指定内容替换成空
            a = value.replace('\r\n', '')
        # 删除字符串前后的空格
            b = a.strip()
        # 把改好的数据写入新的数组
            contentData.append(b)
        # 删除数组最后一条数据
        contentData.pop()
        # 把数组以换行的形式连接成字符串，在内容后面加二个换行
        textContent = "\n".join(contentData) + '\n\n'
        print(textContent)
        # 将内容写入txt文件中
        txt = open('都重生了谁谈恋爱啊.txt', mode='a', encoding='utf-8')
        txt.write(textContent)

exit()