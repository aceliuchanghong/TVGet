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


def parseUrlGetMp4(url):
    import requests
    import re
    from urllib.parse import urlparse, parse_qs
    import json
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,ja;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "JSESSIONID=B1A9D1995B753ECAEC6D3507F6492989; arialoadData=true; ariawapChangeViewPort=false",
        "Host": "svideo.mfa.gov.cn",
        "Origin": "https://svideo.mfa.gov.cn",
        "Referer": str(url),
        "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.get(url)
    html_content = response.content.decode('utf-8')
    pattern = r'flashvars\.prePlayUrl = "(.*?)";'
    match = re.search(pattern, html_content)

    if match:
        pre_play_url = match.group(1).replace("%26", "&")
        # print(pre_play_url)
    else:
        pre_play_url = None
        print("No mp4 match found.")

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if 'id' in query_params:
        id_value = query_params['id'][0]
        # print(id_value)
    else:
        id_value = None
        print("No id match found.")
    data = {
        "uid": -1, "uname": "", "eds": "",
        "json": {"masId": id_value, "isLive": 'false', "screen": "1920*1080", "player": "HTML5", "docId": 0, "eds": ""}

    }

    response = requests.post(pre_play_url, headers=headers, json=data)
    html_content = response.content.decode('utf-8')
    # print(html_content)
    data = json.loads(html_content)

    http_url = data["streamsMap"]["h"]["httpURL"]
    return http_url


url = 'https://svideo.mfa.gov.cn/mas/openapi/pages.do?method=exPlay&appKey=gov&id=17603&autoPlay=false'

print()

