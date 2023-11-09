import requests
from crawl.spiderDealer.checkPath import check
import re
from urllib.parse import urljoin
from lxml import etree


def get_html_url_list():
    url_template = "https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/index_{}.shtml"

    param = 1
    valid_urls = []
    index_0 = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/index.shtml'
    valid_urls.append(index_0)
    while True:
        url = url_template.format(param)
        response = requests.get(url, allow_redirects=False)
        if response.status_code != 200:
            # 无法访问到有效的网页，参数的最大值为前一个值
            max_param = param - 1
            # print(max_param)
            break
        valid_urls.append(url)
        param += 1
    return valid_urls


def get_ans_url_list(url):
    base = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/'
    valid_ans_urls = []
    response = requests.get(url)
    html_content = response.content.decode('utf-8')
    tree = etree.HTML(html_content)
    # 大的div '/html/body/div[4]/div[2]/div[2]/div/div[2]'
    # 具体链接对应的块 '/html/body/div[4]/div[2]/div[2]/div/div[2]/ul[1]/li[2]'
    # 具体链接 /html/body/div[4]/div[2]/div[2]/div/div[2]/ul[1]/li[1]/a/@href
    # html_url_content = tree.xpath('/html/body/div[4]/div[2]/div[2]/div/div[2]/ul[1]/li[1]/a/@href')
    # html_word_content = tree.xpath('/html/body/div[4]/div[2]/div[2]/div/div[2]/ul[1]/li[1]/a/text()')
    html_url_content2 = tree.xpath('/html/body/div[4]/div[2]/div[2]/div/div[2]//@href')
    html_word_content2 = tree.xpath('/html/body/div[4]/div[2]/div[2]/div/div[2]//a/text()')
    ans = [list(item) for item in zip(html_url_content2, html_word_content2)]
    for i in ans:
        i[0] = urljoin(base, i[0])
        valid_ans_urls.append(i)
    return valid_ans_urls


def run_once():
    all_url = []
    all_html = get_html_url_list()
    # print(all_html)
    for url in all_html:
        ans = get_ans_url_list(url)
        # print(ans)
        all_url.extend(ans)
    # 持久化列表到文件
    with open('../main/ans.txt', 'w') as file:
        for item in all_url:
            file.write(f"{item[0]},{item[1]}\n")
    return all_url


# def run_every_day(always_new, filename='ans'):
#     ans = get_ans_url_list(always_new)
#     appended_elements = []
#     with open('../main/' + filename + '.txt', 'a+') as file:
#         file.seek(0)  # 将文件指针移到文件开头
#         existing_elements = set(line.strip().split(',', 1)[0] for line in file)
#
#         for element in ans:
#             element_str = f"{element[0]},{element[1]}"
#             if element[0] not in existing_elements:
#                 # print(element_str)
#                 file.write(f"{element_str}\n")
#                 appended_elements.append(element)
#
#     return appended_elements


def run_every_day(always_new, nums=1, filename='ans'):
    try:
        ans = get_ans_url_list(always_new)
        appended_elements = []
        with open('../main/' + filename + '.txt', 'a+') as file:
            file.seek(0)  # 将文件指针移到文件开头
            existing_elements = set(line.strip().split(',', 1)[0] for line in file)

            for element in ans:
                element_str = f"{element[0]},{element[1]}"
                if element[0] not in existing_elements and len(appended_elements) < nums:
                    file.write(f"{element_str}\n")
                    appended_elements.append(element)
        return appended_elements
    except Exception as e:
        print(f"An error occurred in run_every_day: {e}")


def testUrl(param):
    url_template = "https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/index_{}.shtml"
    url = url_template.format(param)
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        return False
    return True


def run_specific(page_num, nums):
    try:
        # 判断文件是否仍然是最新的
        need_run = False
        with open('../main/html.url.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                match = re.search(r'index_(\d+).shtml', last_line)
                if match:
                    max_page_num_in_file = match.group(1)
                    if testUrl(int(max_page_num_in_file) + 1):
                        need_run = True
                else:
                    print("No number found before 'shtml' in the URL.")
            else:
                print("The file is empty.")
        if need_run:
            print("获取链接中...")
            with open('../main/html.url.txt', 'w') as file:
                all_html = get_html_url_list()
                for url in all_html:
                    file.write(f"{url}\n")
    except Exception as e:
        print(f"An error occurred1: {e}")
    try:
        # 上传对应page_num的nums个未上传的视频
        urls_list = []
        with open('../main/html.url.txt', 'r') as file:
            for line in file:
                urls_list.append(line.strip())
        if page_num > len(urls_list):
            print("The page number is too large.")
            return
        this_url_elements = run_every_day(urls_list[len(urls_list) - page_num], nums, 'special')
        return this_url_elements
    except Exception as e:
        print(f"An error occurred2: {e}")
