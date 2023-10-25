# 网页内容保存成合适文档保存与本地response路径下面
from crawl.spiderDealer.checkPath import check

def getFile(url):
    import requests

    response = requests.get(url)
    html_content = response.content.decode('utf-8')
    # print(html_content)

    filename = url.split('/')[-1].split('.')[0] + '.html'
    # 将网页内容保存到本地文件
    basicpath = '../../crawl/files/response/'
    check(basicpath)

    file_path = '../../crawl/files/response/' + filename
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    # print('网页内容已保存到:', file_path)

    return filename


def parseUrlGetPic(url):
    import requests
    import re

    response = requests.get(url)
    html_content = response.content.decode('utf-8')

    pattern = r'https://svideo\.mfa\.gov\.cn/masvod/public/\d{4}/\d{2}/\d{2}/\d+\.images/v\d+_b\d+\.jpg'

    match = re.search(pattern, html_content)
    if match:
        result = match.group()
    else:
        result = None
        print("No pic match found.")

    return result
