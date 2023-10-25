from moviepy.editor import *
from crawl.spiderDealer.checkPath import check
import subprocess


def cutMp4(mp4path):
    output_file = mp4path.split('/')[-1]
    relative_path = '../../crawl/files/mp4_bak/'
    check(relative_path)
    video = VideoFileClip(mp4path)
    video = video.subclip(0, video.duration - 2)
    video.write_videofile(relative_path + output_file)
    return relative_path + output_file


def srtAdd(result):
    relative_path = '../../crawl/files/ans/'
    check(relative_path)

    command = f'ffmpeg -y -i "{result.anspath}" -vf "subtitles={result.srtpath}:charenc=GBK" "{relative_path + result.mp4name}"'
    # print(command)
    subprocess.call(command, shell=True)
    return relative_path + result.mp4name
