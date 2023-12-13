from readBook.download_images import *
from datetime import datetime
from readBook.image_utils import *

urls_list = [
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473762148363/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png?ex=6580c028&is=656e4b28&hm=d56d745b0b31e781235b9488a5d65bd1cc67dcac84ea06884eb7bc2ca6f1eb17&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png?ex=657fdb',
]


def deal_image(url, re_run=False):
    picResult = PicResult()
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
        resize_image_path = "../crawl/files/redbook/resize_pic"
        check(resize_image_path)
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

        try:
            picResult.downpath = download(picResult.url, name=picResult.name, path=original_pic_path, proxies=proxies,
                                          re_run=re_run)
            picResult.bakpath = copy_file(picResult.downpath, original_pic_bak_path + "/" + picResult.name,
                                          re_run=re_run)
            # 背景图片模糊
            picResult.fix1path = blur_bg_image(picResult.downpath, blur_pic_path + "/" + picResult.name,
                                               re_run=re_run)
            # 1.填充安卓图片==>组合到图片
            """以下可以,但是,太复杂了,且不可复用,所以写个函数
            
            """
            # # 下载的图片A作为底片,调整手机B等大小适配A
            # the_image_info = get_image_size(picResult.downpath)
            # the_phone_info = get_image_size(andriod_image)
            #
            # # 获取放缩比例
            # if the_image_info.width >= the_image_info.height:
            #     scale_factor = round(the_image_info.height / the_phone_info.height, 2)
            # else:
            #     scale_factor = round(the_image_info.width / the_phone_info.width, 2)
            # # x轴位置
            # xAxis = the_phone_info.width * (1 - 0.818)
            # # y轴位置
            # # yAxis = the_phone_info.height * (1 - 0.618)
            # # 调整机型图片比例
            # new_andriod_image = resize_image_proportionally(andriod_image,
            #                                                 resize_image_path + "/" + the_image_info.name + "." + the_image_info.ext,
            #                                                 scale_factor,
            #                                                 re_run=re_run)
            #
            # # 组合图片
            # picResult.fix2path = merge_images(new_andriod_image, fix_pic_path + "/fix_merge_android." + picResult.name,
            #                                   picResult.downpath, smallPicCenterAxes=(xAxis, 0), re_run=re_run)
            # # 裁剪图片
            # fix_cut_info = get_image_size(new_andriod_image)
            # picResult.fix3path = cut_image(picResult.fix2path, fix_pic_path + "/fix_cut_android_cut." + picResult.name,
            #                                fix_cut_info.width, fix_cut_info.height, center_coords=(xAxis, 0),
            #                                re_run=re_run)
            picResult.fix2path = fill_image(input_image_path=andriod_image, background_image=picResult.downpath,
                                            output_image_path=fix_pic_path + "/fix_android." + picResult.name,
                                            center_coords=(0, 0), re_run=re_run)
            # 2.填充iPhone图片==>组合到图片

            # 3.填充平板图片==>组合到图片

            # 4.填充电脑图片==>组合到图片

            # 5.填充成品文字

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
        picResult = deal_image(url, False)
        print(picResult.to_clazz())
        break
