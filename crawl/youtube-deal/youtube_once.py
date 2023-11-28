from youtube_util import *

output_path = "../../crawl/files/youtube/hitomi/out"
publish_path = "../../crawl/files/youtube/hitomi/publish"
source_path = "../../crawl/files/youtube/hitomi"

check(output_path)
check(publish_path)
check(source_path)

# 获取 source_path 下面的视频,切分成 30 秒一段,然后对每个视频做切割,移动到 output_path 下面
mp4_files = get_mp4_files(source_path)
for file in mp4_files:
    spilt_file_names = split_video(file, 30)
    for spilt_file_name in spilt_file_names:
        transfered_tiktok_path = tiktok(spilt_file_name)
        move_file(transfered_tiktok_path, output_path)
