from moviepy.editor import *
from crawl.spiderDealer.checkPath import check
import subprocess


def cutMp4(mp4path):
    output_file = mp4path.split('/')[-1]
    relative_path = '../../crawl/files/mp4_bak/'
    check(relative_path)
    if not os.path.exists(relative_path + output_file):
        video = VideoFileClip(mp4path)
        video = video.subclip(0, video.duration - 2)
        video.write_videofile(relative_path + output_file)
    # print("mp4 cut SUC")
    return relative_path + output_file


def srtAdd(result):
    relative_path = '../../crawl/files/ans/'
    check(relative_path)

    command = f'ffmpeg -y -i "{result.anspath}" -vf "subtitles={result.srtpath}:force_style=\'Fontsize=10\'" "{relative_path + result.mp4name}"'
    # print(command)
    if not os.path.exists(relative_path + result.mp4name):
        subprocess.call(command, shell=True)
    # print("srt add SUC")
    return relative_path + result.mp4name
