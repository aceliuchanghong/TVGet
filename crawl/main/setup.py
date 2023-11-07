import time
import sys
import requests
from crawl.spiderDealer.sourceDeal import *
from crawl.test.process import create
from douyin_upload.test.testCookie import main
import asyncio


def testNet():
    proxyHost = "127.0.0.1"
    proxyPort = 10809
    proxies = {
        "http": f"http://{proxyHost}:{proxyPort}",
        "https": f"http://{proxyHost}:{proxyPort}"
    }

    url = "https://www.youtube.com/"

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        # print("连接成功")
        return True
    except requests.exceptions.RequestException as e:
        print(f"v2ray链接失效：{str(e)}")
        return False
    except Exception as e:
        print(f"v2ray链接失效：{str(e)}")
        return False


# 测试数据
url_list = [['https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202207/t20220711_10718477.shtml', 00]]
# cd .\douyin_upload\test
# playwright codegen www.douyin.com --save-storage=cookie.json

# url_list = run_every_day()
# url_list = run_once()


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
            # asyncio.run(main(result))
        except Exception as e:
            print("第" + str(i + 1) + "个:" + "create error:", e)
            print(url[0])
            print(url[1])
            continue
    print("********************END********************")
