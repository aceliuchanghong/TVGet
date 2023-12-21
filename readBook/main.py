from crawl.spiderDealer.checkPath import check
from readBook import the_list
from readBook.deal_image_urls import deal_image
from readBook.deal_upload import start
import asyncio
from readBook.image_utils import copy_file


def publish_xhs(urls_list, re_run=False):
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
                            content = file.read()
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


if __name__ == '__main__':
    publish_xhs(the_list.urls_list, True)
