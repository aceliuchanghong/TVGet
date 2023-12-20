from crawl.spiderDealer.checkPath import check
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
                print("End,already uploaded")
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
                        print(words_image_path + "/" + picResult.fix12path + "." + picResult.name)
                    else:
                        print("上传失败")
                else:
                    print("文件处理失败")
        except Exception as e:
            print(f"Open file error occurred: {e}")


urls_list = [
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480579345125376/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_ad86dcb2-7673-40f0-b750-4336ddab27e4.png?ex=65936725&is=6580f225&hm=9555eed4a42654c8a55113ac0e9a0e52e9d234deab0155df6a717f578ee13deb&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480604624199751/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_b151993c-dec3-46c1-942f-81aa2cba0ca0.png?ex=6593672b&is=6580f22b&hm=684c60175ba522fcf6329592c5a72902a968444b16e50798b7538521f1135218&',

]
bak = [
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480585447854100/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d6d9e024-49b8-41f5-9368-461b08368578.png?ex=65936727&is=6580f227&hm=7c064ca70a170e09c5469f4dfe2a945e273750318df3c88fdabedba868135fc4&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480615005098035/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d1722e22-b247-49a9-9929-266a8c3ac3d9.png?ex=6593672e&is=6580f22e&hm=24aac05abf57c3414f220dfce028b314bd3e74c3e2aba79d54f2537ee5bde731&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473762148363/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png?ex=6580c028&is=656e4b28&hm=d56d745b0b31e781235b9488a5d65bd1cc67dcac84ea06884eb7bc2ca6f1eb17&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png?ex=657fdb',
]

if __name__ == '__main__':
    publish_xhs(urls_list, True)
