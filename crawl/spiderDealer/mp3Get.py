from moviepy.editor import *
from crawl.spiderDealer.checkPath import check
import os


def mp423(mp4path, name=None):
    # Get file name
    output_file = mp4path.split('/')[-1].replace("mp4", "mp3")

    if name is not None:
        output_file = name
    # print(output_file)

    relative_path = '../../crawl/files/mp3/'
    check(relative_path)
    mp3path = relative_path + output_file
    if not os.path.exists(mp3path):
        try:
            video = VideoFileClip(mp4path)
            audio = video.audio
            audio.write_audiofile(mp3path)
        except Exception as e:
            print(f"mp423 函数发生错误：{str(e)}")
    print("mp3 get SUC")
    return mp3path
