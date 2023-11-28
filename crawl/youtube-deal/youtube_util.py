import shutil
import subprocess

from crawl.spiderDealer.checkPath import check
import os


def get_mp4_files(directory):
    # 获取目录中的所有条目
    entries = os.listdir(directory)

    # 过滤出所有的.mp4文件
    mp4_files = [directory + "/" + file for file in entries if
                 file.lower().endswith('.mp4') and os.path.isfile(os.path.join(directory, file))]

    return mp4_files


def get_video_info(video_path):
    command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size', '-of',
               'default=noprint_wrappers=1:nokey=1', video_path]
    output = subprocess.check_output(command).decode('utf-8').strip().split('\n')
    duration = float(output[0])
    size = int(output[1])

    video_name = os.path.splitext(os.path.basename(video_path))[0]

    video_info = {
        'name': video_name,
        'duration': duration,
        'size': size,
        'path': video_path
    }
    return video_info


def split_video(video_path, duration):
    output_dir = os.path.dirname(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    command = ['ffmpeg', '-i', video_path, '-c', 'copy', '-segment_time', str(duration), '-f', 'segment',
               '-reset_timestamps', '1', '-map', '0', os.path.join(output_dir, f'{video_name}_%03d.mp4')]
    subprocess.run(command)

    split_files = []
    for file in os.listdir(output_dir):
        if file.startswith(f'{video_name}_') and file.endswith('.mp4'):
            split_files.append(output_dir + "/" + file)

    return split_files


def copy_file(source_path, destination_path):
    video_name = os.path.splitext(os.path.basename(source_path))[0]
    if os.path.exists(destination_path + "/" + video_name + ".mp4"):
        print("copy File already exists in the destination.")
    elif not os.path.exists(source_path):
        print("copy Source file does not exist.")
    else:
        shutil.copy(source_path, destination_path)
        # print("File copied successfully.")


def move_file(source_path, destination_path):
    video_name = os.path.splitext(os.path.basename(source_path))[0]
    if os.path.exists(destination_path + "/" + video_name + ".mp4"):
        print("move File already exists in the destination.")
        os.remove(source_path)
    elif not os.path.exists(source_path):
        print("move Source file does not exist.")
    else:
        shutil.move(source_path, destination_path)
        # print("File moved successfully.")


def tiktok(video_path):
    # TikTok 建议的分辨率为 1080x1920
    target_width = 1080
    target_height = 1920
    # 黄金分割比例点
    golden_ratio_point = 1 / (1 + 1.618)

    # 获取视频的宽度和高度
    ffprobe_command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'csv=p=0', video_path
    ]
    process = subprocess.run(ffprobe_command, stdout=subprocess.PIPE, text=True)
    output = process.stdout
    video_width, video_height = map(int, output.split(','))

    # 计算裁剪起始点
    crop_x = int(video_width * golden_ratio_point)
    # 确保裁剪的宽度不会超出视频宽度
    crop_width = min(video_width - crop_x, int(video_height * target_width / target_height))

    video_info = get_video_info(video_path)

    ffmpeg_command = [
        'ffmpeg',
        '-y',  # 覆盖输出文件
        '-i', video_path,  # 输入文件
        '-vf', f'crop={crop_width}:{video_height}:{crop_x}:0,scale={target_width}:{target_height}',  # 裁剪并缩放
        '-preset', 'veryfast',  # 编码速度
        '-crf', '28',  # 视频质量
        video_info['path'] + ".transform.mp4"  # 输出文件
    ]
    # 执行 FFmpeg 命令
    subprocess.run(ffmpeg_command, check=True)
    # 检查文件是否创建
    if os.path.isfile(video_info['path'] + ".transform.mp4"):
        print("视频已转换并保存为:" + video_info['path'] + ".transform.mp4")
    return video_info['path'] + ".transform.mp4"

# output_path = "../../crawl/files/youtube/hitomi/out"
# publish_path = "../../crawl/files/youtube/hitomi/publish"
# source_path = "../../crawl/files/youtube/hitomi"
# test_path = "../../crawl/files/youtube/hitomi/test"
# test2_path = "../../crawl/files/youtube/hitomi/test2"
#
# check(test_path)
# check(output_path)
# check(publish_path)
# check(test2_path)
#
# mp4_files = get_mp4_files(test_path)
# for file in mp4_files:
#     video_info = get_video_info(file)
#     video_name = video_info['name']
#     video_length = video_info['duration']
#     video_size = video_info['size']
#     video_path = video_info['path']
#     print(video_name, "###", video_length, "###", video_size, "###", video_path)
#     spilt_file_names = split_video(file, 30)
#     for spilt_file_name in spilt_file_names:
#         move_file(spilt_file_name, test2_path + "/" + os.path.basename(spilt_file_name))
#     break
#
# test_file = "../../crawl/files/youtube/hitomi/test2/00_000.mp4"
# tiktok(test_file)
