from crawl.spiderDealer.checkPath import check
from readBook import the_list
from readBook.deal_image_urls import deal_image
from readBook.deal_upload import start
import asyncio
import os
from readBook.image_utils import copy_file
from typing import List


def publish_xhs2(urls_list, re_run=False):
    for url in urls_list:
        # 尝试打开并读取文件内容
        try:
            with open('uploaded.log', 'r') as file:
                content = file.read()
                file.close()
                # 检查字符串是否在文件内容中
            if url in content:
                # print("OK,already uploaded")
                pass
            else:
                picResult = deal_image(url=url, re_run=re_run)
                if picResult.describe == "SUC":
                    is_success = asyncio.run(start(picResult, re_run))
                    # is_success = True
                    if is_success:
                        with open('uploaded.log', 'a+') as file:
                            file.seek(0)
                            file.write(f"{url}\n")
                            file.close()
                        words_image_path = "../crawl/files/redbook/pub_send_pics"
                        check(words_image_path)
                        copy_file(source_path=picResult.downpath,
                                  destination_path=words_image_path + "/" + picResult.fix12path + "." + picResult.name,
                                  re_run=re_run)
                        # print(words_image_path + "/" + picResult.fix12path + "." + picResult.name)
                    else:
                        print("ERR:上传失败")
                else:
                    print("ERR:文件处理失败")
        except Exception as e:
            print(f"Open file error occurred: {e}")


def publish_xhs(urls_list: List[str], re_run: bool = False):
    uploaded_log_path = 'uploaded.log'
    words_image_path = "../crawl/files/redbook/pub_send_pics"

    for url in urls_list:
        try:
            # 检查URL是否已经上传
            with open(uploaded_log_path, 'r') as file:
                if url in file.read():
                    continue

            picResult = deal_image(url=url, re_run=re_run)
            if picResult.describe == "SUC":
                is_success = asyncio.run(start(picResult, re_run))
                if is_success:
                    # 记录到日志文件
                    with open(uploaded_log_path, 'a') as file:
                        file.write(f"{url}\n")

                    destination_path = os.path.join(words_image_path, f"{picResult.fix12path}.{picResult.name}")
                    copy_file(source_path=picResult.downpath, destination_path=destination_path, re_run=re_run)
                else:
                    print("ERR:上传失败")
            else:
                print(picResult)
                print("ERR:文件处理失败")
        except FileNotFoundError:
            # 如果文件不存在，则创建并重新尝试
            open(uploaded_log_path, 'a').close()
        except Exception as e:
            print(f"Open file error occurred: {e}")


if __name__ == '__main__':
    publish_xhs(the_list.urls_list, True)
