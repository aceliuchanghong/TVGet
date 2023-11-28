from crawl.spiderDealer.checkPath import check
from youtube_util import *

output_path = "../../crawl/files/youtube/hitomi/out"
source_path = "../../crawl/files/youtube/hitomi"
already_path = "../../crawl/files/youtube/hitomi/already_cut"
check(output_path)
check(source_path)
check(already_path)


mp4_files = get_mp4_files(source_path)
for file in mp4_files:
    try:
        spilt_file_names = split_video(file, 30)
        for spilt_file_name in spilt_file_names:
            transfered_tiktok_path = tiktok(spilt_file_name)
            move_file(transfered_tiktok_path, output_path)
    except Exception as e:
        print(" error:", e)
for file in mp4_files:
    move_file(file, already_path)
