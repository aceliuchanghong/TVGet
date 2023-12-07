from os.path import exists
from crawl.spiderDealer.checkPath import check
from readBook.PicResult import PicResult, PicInfo
import subprocess
import re
import json


def get_image_size(image_path):
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


def blur_image(input_image_path, output_image_path, blur_strength=5, width=1280, height=1707):
    picResult = PicResult()
    picInfo = get_image_size(input_image_path)
    if picInfo.width > picInfo.height:
        newHight = picInfo.height
        newWidth = newHight * width / height
    else:
        newWidth = picInfo.width
        newHight = newWidth * height / width
    try:
        # 判断是否需要调整图像尺寸
        if picInfo.width < width or picInfo.height < height:
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
        if not exists(output_image_path):
            subprocess.run(command, check=True)
        picResult.fix1path = output_image_path
        return picResult
    except Exception as e:
        print(e)
        picResult.describe = 'ERR:GAZZ'
        return picResult


# 待修改
def ficPic(picPath, width, height):
    picResult = PicResult()
    picInfo = get_image_size(picPath)
    if picInfo.width > picInfo.height:
        newHight = picInfo.height
        newWidth = newHight * width / height
    else:
        newWidth = picInfo.width
        newHight = newWidth * height / width
    try:
        # 判断是否需要调整图像尺寸
        if picInfo.width < width or picInfo.height < height:
            vf_filter = f'crop={newWidth}:{newHight}'
        else:
            vf_filter = f'crop={width}:{height}'

        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', picPath,  # 输入图片文件
            '-vf', vf_filter,
            '-y',  # 覆盖输出文件（如果已经存在）
            picPath  # 输出图片文件
        ]

        # 执行命令
        if not exists(picPath):
            subprocess.run(command, check=True)
        picResult.fix1path = picPath
        return picResult
    except Exception as e:
        print(e)
        picResult.describe = 'ERR:FIX'
        return picResult


# 待修改
def mergePic(smallPic, bigPic, smallPicCenterAxios):
    picResult = PicResult()
    try:
        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', smallPic,  # 输入图片文件
            '-i', bigPic,  # 输入图片文件
            '-filter_complex', 'overlay=0:0',
            '-y',  # 覆盖输出文件（如果已经存在）
            bigPic  # 输出图片文件
        ]

        # 执行命令
        if not exists(bigPic):
            subprocess.run(command, check=True)
        picResult.fix2path = bigPic
        return picResult
    except Exception as e:
        print(e)
        picResult.describe = 'ERR:MER'
        return picResult


pic_result = PicResult()
pic_result.name = "eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png"
pic_result.ext = "png"
pic_result.date = None
pic_result.keyword = None
pic_result.url = "https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png"
pic_result.downpath = "../crawl/files/redbook/original_pic/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png"
pic_result.bakpath = None
pic_result.fix1path = None
pic_result.fix2path = None
pic_result.fix3path = None
pic_result.anspath = None
pic_result.describe = "SUC"

picPathGazz = "../crawl/files/redbook/gazz_pic/"
check(picPathGazz)
# 定义输入输出文件路径
foreground_image = pic_result.downpath
background_image = 'basicPic/ipad_ok.png'
p1 = get_image_size(picPathGazz + "/" + "20231206225510.jpg")
p2 = get_image_size(foreground_image)
print(p1)
p3 = blur_image(foreground_image, picPathGazz + pic_result.name, 5)
print(p2)
