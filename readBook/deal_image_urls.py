from readBook.download_images import *
from datetime import datetime
from readBook.image_utils import *

# 优化函数,其中参数,逻辑按照我这个,将保持原有逻辑不变，对代码进行优化。优化的重点将放在减少重复代码、提高代码的可读性和维护性上,给出完整具体的代码

urls_list = [
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480579345125376/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_ad86dcb2-7673-40f0-b750-4336ddab27e4.png?ex=65936725&is=6580f225&hm=9555eed4a42654c8a55113ac0e9a0e52e9d234deab0155df6a717f578ee13deb&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480604624199751/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_b151993c-dec3-46c1-942f-81aa2cba0ca0.png?ex=6593672b&is=6580f22b&hm=684c60175ba522fcf6329592c5a72902a968444b16e50798b7538521f1135218&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480585447854100/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d6d9e024-49b8-41f5-9368-461b08368578.png?ex=65936727&is=6580f227&hm=7c064ca70a170e09c5469f4dfe2a945e273750318df3c88fdabedba868135fc4&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480615005098035/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d1722e22-b247-49a9-9929-266a8c3ac3d9.png?ex=6593672e&is=6580f22e&hm=24aac05abf57c3414f220dfce028b314bd3e74c3e2aba79d54f2537ee5bde731&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473762148363/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png?ex=6580c028&is=656e4b28&hm=d56d745b0b31e781235b9488a5d65bd1cc67dcac84ea06884eb7bc2ca6f1eb17&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png?ex=657fdb',

]


def deal_image(
        url='https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
        picPath=None, re_run=False):
    picResult = PicResult()
    proxy_host = '127.0.0.1'
    proxy_port = 10809
    proxies = {
        'http': f'http://{proxy_host}:{proxy_port}',
        'https': f'http://{proxy_host}:{proxy_port}'
    }

    original_pic_path = '../crawl/files/redbook/original_pic'
    check(original_pic_path)
    original_pic_bak_path = '../crawl/files/redbook/original_bak_pic'
    check(original_pic_bak_path)
    blur_pic_path = "../crawl/files/redbook/blur_pic"
    check(blur_pic_path)
    source_pic_path = "../readBook/basicPic"
    check(source_pic_path)
    fix_pic_path = "../crawl/files/redbook/fix_pic"
    check(fix_pic_path)
    words_image_path = "../crawl/files/redbook/words_pic"
    check(words_image_path)
    the_andriod_image = "andriod_ok.png"
    the_iphone_image = "iphone_ok.png"
    the_ipad_image = "ipad_ok.png"
    the_laptop_image = "huawei_laptop_ok.png"
    andriod_image = source_pic_path + "/" + the_andriod_image
    iphone_image = source_pic_path + "/" + the_iphone_image
    ipad_image = source_pic_path + "/" + the_ipad_image
    laptop_image = source_pic_path + "/" + the_laptop_image

    if url is not None and len(url) > 10:
        # 获取url
        try:
            pattern_url = r'\?.*'
            clean_url = re.sub(pattern_url, '', url)
            picResult.url = clean_url
        except Exception as e:
            picResult.describe = "ERR:url_re"
            print(e)
            return picResult

        # 使用正则表达式提取文件名
        try:
            pattern_name = r"/([\w.-]+)\.[a-z]{3}\?"
            match = re.search(pattern_name, url)
            if match:
                match_ext = re.search(r'\.(gif|png|jpg)\?', url)
                picResult.ext = match_ext.group(1)
                picResult.keyword = match.group(1)
                picResult.name = match.group(1) + "." + picResult.ext
                picResult.date = datetime.now().strftime("%Y%m%d")
        except Exception as e:
            picResult.describe = "ERR:files"
            print(e)
            return picResult

        try:
            if picPath is not None:
                picResult.downpath = picPath
                picResult.ext = picPath.split(".")[-1]
                picResult.name = picPath.split("/")[-1]
            else:
                picResult.downpath = download(picResult.url, name=picResult.name, path=original_pic_path,
                                              proxies=proxies,
                                              re_run=re_run)
            picResult.bakpath = copy_file(picResult.downpath, original_pic_bak_path + "/" + picResult.name,
                                          re_run=re_run)
            # 0.背景图片模糊
            picResult.fix1path = blur_bg_image(picResult.downpath, blur_pic_path + "/" + picResult.name,
                                               re_run=re_run)
            # 1.填充安卓图片==>组合到图片
            picResult.fix2path = fill_image(input_image_path=andriod_image, background_image_path=picResult.downpath,
                                            center_coords=(0, 0), re_run=re_run)

            center_coords = calculate_center_coords(picResult.fix2path, 4.5, 5.5)
            picResult.fix2path = put_words_on_image(words=datetime.now().strftime("%H"),
                                                    input_image_path=picResult.fix2path,
                                                    output_image_path=words_image_path + "/1.andriod." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix2path, 2.3, 4.7)
            picResult.fix2path = put_words_on_image(words=":", input_image_path=picResult.fix2path,
                                                    output_image_path=words_image_path + "/2.andriod." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix2path, 1.9, 5.5)
            picResult.fix2path = put_words_on_image(words=datetime.now().strftime("%M"),
                                                    input_image_path=picResult.fix2path,
                                                    output_image_path=words_image_path + "/3.andriod." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix2path, 3.2, 3.5)
            picResult.fix2path = put_words_on_image(words=datetime.now().strftime("%Y年%m月%d日"),
                                                    input_image_path=picResult.fix2path,
                                                    output_image_path=words_image_path + "/4.andriod." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=28,
                                                    center_coords=center_coords, re_run=re_run)

            # 2.填充iPhone图片==>组合到图片
            picResult.fix3path = fill_image(input_image_path=iphone_image, background_image_path=picResult.downpath,
                                            center_coords=(0, 0), re_run=re_run, debug=False)

            center_coords = calculate_center_coords(picResult.fix3path, 4.5, 5.5)
            picResult.fix3path = put_words_on_image(words=datetime.now().strftime("%H"),
                                                    input_image_path=picResult.fix3path,
                                                    output_image_path=words_image_path + "/1.iphone." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix3path, 2.3, 4.7)
            picResult.fix3path = put_words_on_image(words=":", input_image_path=picResult.fix3path,
                                                    output_image_path=words_image_path + "/2.iphone." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix3path, 1.9, 5.5)
            picResult.fix3path = put_words_on_image(words=datetime.now().strftime("%M"),
                                                    input_image_path=picResult.fix3path,
                                                    output_image_path=words_image_path + "/3.iphone." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix3path, 3.2, 3.5)
            picResult.fix3path = put_words_on_image(words=datetime.now().strftime("%Y年%m月%d日"),
                                                    input_image_path=picResult.fix3path,
                                                    output_image_path=words_image_path + "/4.iphone." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=28,
                                                    center_coords=center_coords, re_run=re_run)

            # 3.填充平板图片==>组合到图片
            picResult.fix4path = fill_image(input_image_path=ipad_image, background_image_path=picResult.downpath,
                                            center_coords=(0, 0), re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix4path, 2.8, 5.5)
            picResult.fix4path = put_words_on_image(words=datetime.now().strftime("%H"),
                                                    input_image_path=picResult.fix4path,
                                                    output_image_path=words_image_path + "/1.ipad." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix4path, 2.15, 4.7)
            picResult.fix4path = put_words_on_image(words=":", input_image_path=picResult.fix4path,
                                                    output_image_path=words_image_path + "/2.ipad." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix4path, 1.98, 5.5)
            picResult.fix4path = put_words_on_image(words=datetime.now().strftime("%M"),
                                                    input_image_path=picResult.fix4path,
                                                    output_image_path=words_image_path + "/3.ipad." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=130,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix4path, 2.5, 3.2)
            picResult.fix4path = put_words_on_image(words=datetime.now().strftime("%Y年%m月%d日"),
                                                    input_image_path=picResult.fix4path,
                                                    output_image_path=words_image_path + "/4.ipad." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=28,
                                                    center_coords=center_coords, re_run=re_run)

            # 4.填充电脑图片==>组合到图片
            picResult.fix5path = fill_image(input_image_path=laptop_image, background_image_path=picResult.downpath,
                                            center_coords=(0, 0), re_run=re_run)

            center_coords = calculate_center_coords(picResult.fix5path, 6, 1.6)
            picResult.fix5path = put_words_on_image(words=datetime.now().strftime("%H"),
                                                    input_image_path=picResult.fix5path,
                                                    output_image_path=words_image_path + "/1.laptop." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=110,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix5path, 3.8, 1.5)
            picResult.fix5path = put_words_on_image(words=":", input_image_path=picResult.fix5path,
                                                    output_image_path=words_image_path + "/2.laptop." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=110,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix5path, 3.33, 1.6)
            picResult.fix5path = put_words_on_image(words=datetime.now().strftime("%M"),
                                                    input_image_path=picResult.fix5path,
                                                    output_image_path=words_image_path + "/3.laptop." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=110,
                                                    center_coords=center_coords, re_run=re_run)
            center_coords = calculate_center_coords(picResult.fix5path, 4.95, 1.27)
            picResult.fix5path = put_words_on_image(words=datetime.now().strftime("%Y年%m月%d日"),
                                                    input_image_path=picResult.fix5path,
                                                    output_image_path=words_image_path + "/4.laptop." + picResult.name,
                                                    fontcolor="ffffff", fontfile="my.ttf", fontsize=25,
                                                    center_coords=center_coords, re_run=re_run)

            # 5.成品
            # 5.1.单独安卓在中间
            # picResult.fix6path = fill_image_model1(input_image_path_left=picResult.fix2path,
            #                                        input_image_path_right=picResult.fix3path,
            #                                        background_image_path=picResult.fix1path, re_run=re_run)
            picResult.fix6path, mmm = fill_image_model2(input_image_path=picResult.fix2path,
                                                        background_image_path=picResult.fix1path,
                                                        x_shift_ratio=0.65,
                                                        re_run=re_run)
            # 5.2.单独iphone手机,右边文字
            picResult.fix7path, picResult.keyword = fill_image_model2(input_image_path=picResult.fix3path,
                                                                      background_image_path=picResult.fix1path,
                                                                      x_shift_ratio=-0.65,
                                                                      re_run=re_run)
            # 5.3.上面ipad,下面laptop
            picResult.fix8path = fill_image_model3(input_image_path_up=picResult.fix4path,
                                                   input_image_path_down=picResult.fix5path,
                                                   background_image_path=picResult.fix1path,
                                                   words=picResult.keyword,
                                                   re_run=re_run)
            picResult.anspath = get_gpt_response2(
                "给我一段形容女子美丽的中文句子,要求文雅,字数在10个子以内,最好是7字诗句,不要最后一个标点",
                picResult.fix8path, re_run)
        except Exception as e:
            picResult.describe = "ERR:deal"
            print(e)
            return picResult

        picResult.describe = "SUC"
        return picResult
    else:
        picResult.describe = "ERR:url"
        return picResult


if __name__ == '__main__':
    for url in urls_list:
        picResult = deal_image(url=url, re_run=False)
        print(picResult.to_clazz())
        # picResult = deal_image(
        #     picPath='../crawl/files/redbook/original_pic/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png',
        #     re_run=False)
        # print(picResult)
        break
