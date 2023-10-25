# -*- coding: utf-8 -*-

import subprocess
import io
import sys

from crawl.spiderDealer.checkPath import check

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def merge_video_with_subtitles(video_path, subtitles_path, output_path):
    anspath = '../../crawl/files/ans/'
    check(anspath)
    command = f'../ffmpeg/bin/ffmpeg -i "{video_path}" -vf "subtitles={subtitles_path}:charenc=GBK" "{anspath + output_path}"'
    print(command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

