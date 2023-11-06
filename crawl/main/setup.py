from crawl.spiderDealer.sourceDeal import *
from crawl.test.process import create
from douyin_upload.test.testCookie import main
import asyncio

url_list = run_every_day()
# url_list = run_once()
# url_list = [['https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231010_11158948.shtml', 00]]
if len(url_list) == 0:
    print("url is none")
else:
    for i, url in enumerate(url_list):
        try:
            # cd .\douyin_upload\test
            # playwright codegen www.douyin.com --save-storage=cookie.json
            print(i)
            result = create(url[0])
            # asyncio.run(main(result))
        except Exception as e:
            print("create error:", e)
            print(url[0])
            print(url[1])
            continue
