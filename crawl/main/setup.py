import sys
from crawl.spiderDealer.net import testNet
from crawl.test.process import create
import asyncio

from douyin_upload.test.testCookie import start

# 测试数据
url_list = [['https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202207/t20220711_10718477.shtml', 00]]


# cd .\douyin_upload\test
# playwright codegen www.douyin.com --save-storage=cookie.json

def run(url_list):
    if len(url_list) == 0:
        print("url is none")
    else:
        if not testNet():
            sys.exit()
        print("********************START********************")
        for i, url in enumerate(url_list):
            try:
                print("第" + str(i + 1) + "个")
                result = create(url[0])
                print("###########获取result成功,准备上传###########")
                asyncio.run(start(result))
                print("###########" + result.date + ":" + result.title)
            except Exception as e:
                print("第" + str(i + 1) + "个:" + "create error:", e)
                print(url[0])
                print(url[1])
                continue
        print("********************END********************")
