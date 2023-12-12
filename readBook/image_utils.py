import os
import shutil
from os.path import exists
from crawl.spiderDealer.checkPath import check
from readBook.PicResult import PicResult, PicInfo
import subprocess
import re
import json


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


def cut_image(input_image_path, output_image_path, width, height, center_coords=(0, 0), re_run=False):
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


if __name__ == '__main__':
    pic_result = PicResult()
    pic_result.name = "eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png"
    pic_result.ext = "png"
    pic_result.date = None
    pic_result.keyword = None
    pic_result.url = "https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png"
    pic_result.downpath = "../crawl/files/redbook/original_pic/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png"
    pic_result.bakpath = None
    pic_result.fix1path = "../crawl/files/redbook/blur_pic/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png",
    pic_result.fix2path = "../crawl/files/redbook/resize_pic/0.3eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png",
    pic_result.fix3path = "../crawl/files/redbook/resize_pic/5.0eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png"
    pic_result.anspath = None
    pic_result.describe = "SUC"

    # picPathGazz = "../crawl/files/redbook/blur_pic/"
    # check(picPathGazz)
    # print(get_image_size(pic_result))
    # print(blur_bg_image(pic_result, picPathGazz + pic_result.name, 5, 1280, 1707))
    # print(blur_bg_image(pic_result, picPathGazz + pic_result.name, 5, 1280, 1707))
    # print(resize_image_proportionally(pic_result, 0.5))
    # print(merge_images(pic_result, "../crawl/files/redbook/original_pic/image.png"))
    print(put_words_on_image("../crawl/files/redbook/original_pic/image.png 厉害", pic_result))
    # print(get_image_size(pic_result.fix3path))
