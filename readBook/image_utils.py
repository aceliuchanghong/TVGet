import os
import shutil
from os.path import exists
from crawl.spiderDealer.checkPath import check
from readBook.PicResult import PicResult, PicInfo
import subprocess
import re
import json
from PIL import Image


def get_image_size(picPath):
    image_path = picPath
    # 构建ffprobe命令
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'json',
        image_path
    ]
    picInfo = PicInfo()
    match = r'([^/]+)\.(png|jpg|jpeg|gif|bmp)$'
    if re.search(match, image_path):
        picInfo.name = re.search(match, image_path).group(1)
        picInfo.ext = re.search(match, image_path).group(2)
    try:
        # 运行ffprobe命令
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 解析输出结果
        if result.returncode == 0:
            output = result.stdout
            info = json.loads(output)
            width = info['streams'][0]['width']
            height = info['streams'][0]['height']
            picInfo.width = width
            picInfo.height = height
            return picInfo
        else:
            raise Exception('ffprobe error: ' + result.stderr.decode('utf-8'))
    except Exception as e:
        print(e)
        return picInfo


def blur_bg_image(input_image_path, output_image_path, blur_strength=5, width=1280, height=1707, re_run=False):
    picInfo = get_image_size(input_image_path)
    try:
        # 判断是否需要调整图像尺寸
        if picInfo.width < width or picInfo.height < height:
            if picInfo.width >= picInfo.height:
                newHight = picInfo.height
                newWidth = newHight * width / height
            else:
                newWidth = picInfo.width
                newHight = newWidth * height / width
            vf_filter = f'boxblur={blur_strength},crop={newWidth}:{newHight}'
        else:
            vf_filter = f'boxblur={blur_strength},crop={width}:{height}'

        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', input_image_path,  # 输入图片文件
            '-vf', vf_filter,
            '-y',  # 覆盖输出文件（如果已经存在）
            output_image_path  # 输出图片文件
        ]

        # 执行命令
        if not exists(output_image_path) or re_run:
            subprocess.run(command, check=True)
        return output_image_path
    except Exception as e:
        print(e)
        return "ERR:BLUR"


def resize_image_proportionally(input_image_path, output_image_path, scale_factor=0.5, re_run=False):
    try:
        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', input_image_path,  # 输入图片文件
            '-vf', f'scale=iw*{scale_factor}:ih*{scale_factor}',
            '-y',  # 覆盖输出文件（如果已经存在）
            output_image_path  # 输出图片文件
        ]
        # 执行命令
        if not exists(output_image_path) or re_run:
            subprocess.run(command, check=True)
        return output_image_path
    except Exception as e:
        print(e)
        return "ERR:resize"


def merge_images(input_image_path, output_image_path, background_image, smallPicCenterAxes=(0, 0), re_run=False):
    try:
        picinfo = get_image_size(input_image_path)
        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', background_image,  # 输入图片文件
            '-i', input_image_path,  # 输入图片文件
            '-filter_complex',
            f'[1]scale={picinfo.width}:{picinfo.height}[small];[0][small]overlay={smallPicCenterAxes[0]}:{smallPicCenterAxes[1]}',
            '-y',  # 覆盖输出文件（如果已经存在）
            output_image_path  # 输出图片文件
        ]

        # 执行命令
        if not exists(output_image_path) or re_run:
            subprocess.run(command, check=True)
        return output_image_path
    except Exception as e:
        print(e)
        return "ERR:merge"


def cut_image2(input_image_path, output_image_path, width, height, center_coords=(0, 0), re_run=False):
    try:
        # 计算剪切区域的起始点
        start_x = center_coords[0] - width // 2
        start_y = center_coords[1] - height // 2

        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', input_image_path,  # 输入图片文件
            '-filter_complex',
            f'crop={width}:{height}:{start_x}:{start_y}',  # 剪切区域和起始点
            '-y',  # 覆盖输出文件（如果已经存在）
            output_image_path  # 输出图片文件
        ]

        # 执行命令
        if not exists(output_image_path) or re_run:
            subprocess.run(command, check=True)
        return output_image_path
    except Exception as e:
        print(e)
        return "ERR:cut"


def put_words_on_image(words, input_image_path, output_image_path, center_coords=(0, 0), re_run=False):
    try:
        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', input_image_path,  # 输入图片文件
            '-vf',
            f'drawtext=fontfile=my.ttf:text={words}:fontcolor=black:fontsize=24:x={center_coords[0]}:y={center_coords[1]}',
            '-y',  # 覆盖输出文件（如果已经存在）
            output_image_path  # 输出图片文件
        ]
        # 执行命令
        if not exists(output_image_path) or re_run:
            subprocess.run(command, check=True)
        return output_image_path
    except Exception as e:
        print(e)
        return "ERR:WORDS"


def copy_file(source_path, destination_path, re_run=False):
    if os.path.exists(destination_path) and not re_run:
        return destination_path
    elif not os.path.exists(source_path):
        print("目标文件不存在:" + source_path)
        return "ERR:copy_file"
    else:
        shutil.copy(source_path, destination_path)
        return destination_path


def cut_image(input_image_path, output_image_path, width, height, center_coords=(0, 0), re_run=False):
    try:
        # 打开输入图片
        with Image.open(input_image_path) as img:
            img_width, img_height = img.size

            # 计算裁剪区域的起始点
            start_x = center_coords[0]
            start_y = center_coords[1]

            # 确保裁剪区域不会超出图片的边界
            end_x = min(start_x + width, img_width)
            end_y = min(start_y + height, img_height)

            # 裁剪图片
            crop_area = (start_x, start_y, end_x, end_y)
            cropped_img = img.crop(crop_area)

            # 如果输出路径不存在或者指定了重新运行，则保存裁剪后的图片
            if not os.path.exists(output_image_path) or re_run:
                cropped_img.save(output_image_path)

        return output_image_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return "ERR:cut"


def fill_image(input_image_path, background_image, output_image_path, width=0, height=0, center_coords=(0, 0),
               re_run=False):
    try:
        # 打开输入图片
        with Image.open(input_image_path) as img:
            img_width, img_height = img.size

            # 计算填充区域的起始点
            start_x = center_coords[0] - width // 2
            start_y = center_coords[1] - height // 2

            # 确保填充区域不会超出图片的边界
            end_x = min(start_x + width, img_width)
            end_y = min(start_y + height, img_height)

            # 计算填充区域的大小
            fill_width = end_x - start_x
            fill_height = end_y - start_y

            # 打开背景图片
            with Image.open(background_image) as bg_img:
                # 如果背景图片的大小和填充区域的大小不一致，则调整背景图片的大小
                if bg_img.size != (fill_width, fill_height):
                    bg_img = bg_img.resize((fill_width, fill_height))

                # 将输入图片粘贴到背景图片中
                bg_img.paste(img, (start_x, start_y))

                # 如果输出路径不存在或者指定了重新运行，则保存填充后的图片
                if not os.path.exists(output_image_path) or re_run:
                    bg_img.save(output_image_path)

        return output_image_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return "ERR:fill"


if __name__ == '__main__':
    picresult = PicResult()
    picresult.name = "stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.ext = "png"
    picresult.date = "20231213"
    picresult.keyword = "stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8"
    picresult.url = "https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.downpath = "../crawl/files/redbook/original_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.bakpath = "../crawl/files/redbook/original_bak_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix1path = "../crawl/files/redbook/blur_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix2path = "../crawl/files/redbook/fix_pic/fix_merge_android.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix3path = "../crawl/files/redbook/fix_pic/fix_cut_android_cut.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.anspath = "None"
    picresult.describe = "SUC"

    print(picresult)