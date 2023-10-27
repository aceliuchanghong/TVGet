from crawl.spiderDealer.sourceDeal import *
from crawl.test.process import create

url_list = run_every_day()
# url_list = run_once()
# url_list = [['https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231010_11158948.shtml', 00]]
if len(url_list) == 0:
    print("url is none")
else:
    for url in url_list:
        try:
            create(url[0])
        except Exception as e:
            print("create error:", e)
            print(url[0])
            print(url[1])
            continue
