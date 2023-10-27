from crawl.spiderDealer.sourceDeal import *
from crawl.test.process import create

url_list = run_every_day()
# url_list = run_once()
if len(url_list) == 0:
    print("url is none")
else:
    for url in url_list:
        create(url[0])
