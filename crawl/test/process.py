# 发送HTTP请求获取网页内容
from crawl.spiderDealer.fileDownload import download
from crawl.spiderDealer.praseFile import parse
from crawl.spiderDealer.urlFileGet import getFile

url = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158313.shtml'
url2 = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158311.shtml'

filename = getFile(url2)
result = parse(filename)
download(result.poster)
download(result.mp4url)
print(result)
