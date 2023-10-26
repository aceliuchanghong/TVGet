from PIL import Image, ImageDraw, ImageFont
import re

from crawl.spiderDealer.checkPath import check


def dealPoster(result):
    poster_path = result.coverpath
    fileName = result.title + '.jpg'
    # 打开原始图片
    image = Image.open(poster_path)

    # 创建绘图对象
    draw = ImageDraw.Draw(image)

    # 设置字体样式和大小
    font = ImageFont.truetype('../ttf/my0.ttf', 100)  # 请将'font.ttf'替换为你的字体文件路径

    # 设置文本内容和位置
    text = result.describe
    text = re.sub(r'([，。、！？])', r'\1\n', text)
    text_position = (50, 1000)

    # 设置文本颜色
    text_color = (255, 0, 0)  # 使用RGB颜色值，这里是红色

    # 在图片上绘制文本
    draw.text(text_position, text, font=font, fill=text_color)

    # 保存修改后的图片
    cover_path = '../../crawl/files/jpeg/'
    check(cover_path)
    image.save(cover_path + fileName)
    print("cover file suc")

    return cover_path + fileName
