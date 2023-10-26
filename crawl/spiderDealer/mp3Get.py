from moviepy.editor import *
from crawl.spiderDealer.checkPath import check


def mp423(mp4path, name=None):
    video = VideoFileClip(mp4path)
    # Get file name
    output_file = mp4path.split('/')[-1].replace("mp4", "mp3")

    if name is not None:
        output_file = name
    # print(output_file)

    audio = video.audio
    relative_path = '../../crawl/files/mp3/'
    check(relative_path)
    mp3path = relative_path + output_file
    audio.write_audiofile(mp3path)
    print("mp3 get SUC")
    return mp3path
