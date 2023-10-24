# 网页内容保存成合适文档保存与本地response路径下面

headers = {
    "Accept-Ranges": "bytes",
    "Age": 1,
    "Content-Length": "89476",
    "Content-Type": "application/javascript;charset=UTF-8",
    "Date": "Tue, 24 Oct 2023 08:02:48 GMT",
    "ETag": 'W/"89476-1688848266000"',
    "Last-Modified": "Sat, 08 Jul 2023 20:31:06 GMT",
    "Server": "waf/4.34.8-0.el7",
    "X-Via": "1.1 wj46:7 (Cdn Cache Server V2.0), 1.1 PS-WNZ-01XOo49:9 (Cdn Cache Server V2.0), 1.1 PS-000-01EAx68:20 (Cdn Cache Server V2.0)",
    "X-Ws-Request-Id": "65377a28_PS-000-01irE70_46702-44057"
}


def getFile(url, headers=headers):
    import requests

    response = requests.get(url)
    html_content = response.content.decode('utf-8')
    # print(html_content)

    filename = url.split('/')[-1].split('.')[0] + '.html'
    # 将网页内容保存到本地文件
    file_path = '../../crawl/files/response/' + filename
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    # print('网页内容已保存到:', file_path)

    return filename


def parseUrlGetPic(url, headers=headers):
    import requests
    import re

    response = requests.get(url)
    html_content = response.content.decode('utf-8')
    print(html_content)

    pattern = r'https://svideo\.mfa\.gov\.cn/masvod/public/\d{4}/\d{2}/\d{2}/\d+\.images/v\d+_b\d+\.jpg'

    match = re.search(pattern, html_content)
    if match:
        result = match.group()
        # print(result)
    else:
        print("No match found.")

    return result
