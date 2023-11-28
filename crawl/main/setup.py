import sys
from crawl.spiderDealer.net import testNet
from crawl.test.process import create
import asyncio
from douyin_upload.test.testCookie import start
from crawl.youtube_deal.youtube_util import *
from crawl.youtube_deal.youtube_result import get_result


def run(url_list):
    if len(url_list) == 0:
        print("url is none")
    else:
        if not testNet():
            sys.exit()
        print("\n********************START********************")
        for i, url in enumerate(url_list):
            try:
                print("第" + str(i + 1) + "个")
                result = create(url[0])
                print("###########获取result成功,准备上传###########")
                asyncio.run(start(result))
                print("###########" + result.date + ":" + result.title)
            except Exception as e:
                with open('../main/' + 'special' + '.txt', 'r+') as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for line in lines:
                        should_delete = any(item[0] in line for item in url_list)
                        if not should_delete:
                            file.write(line)
                with open('../main/' + 'ans' + '.txt', 'r+') as file:
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for line in lines:
                        should_delete = any(item[0] in line for item in url_list)
                        if not should_delete:
                            file.write(line)
                print("第" + str(i + 1) + "个:" + "create error:", e)
                print(url[0])
                print(url[1])
                continue
        print("********************END********************")


def run_youtube(output_path, nums=2):
    if not os.listdir(output_path):
        print(output_path + "下面没视频")
    else:
        publish_path = "../../crawl/files/youtube/hitomi/publish"
        print("********************START********************")
        files = get_mp4_files(output_path)
        for i in range(len(files)):
            try:
                if nums > i and os.path.getsize(files[i]) > 1024 * 1024:
                    print("###########开始上传###########")
                    result = get_result(files[i])
                    print("###########" + result.date + ":" + result.title)
                    asyncio.run(start(result))
                    move_file(files[i], publish_path + "/" + os.path.basename(files[i]))
                else:
                    break
            except Exception as e:
                print("第" + str(i + 1) + "个:" + "上传 error:", e)
                continue
        print("********************END********************")
