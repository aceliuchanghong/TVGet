import shutil
import subprocess

from crawl.spiderDealer.checkPath import check
import os


def get_mp4_files(source_path):
    mp4_files = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(".mp4"):
                mp4_files.append(source_path + "/" + file)
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
        'size': size
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
            split_files.append(os.path.join(output_dir, file))

    return split_files


def copy_file(source_path, destination_path):
    if os.path.exists(destination_path):
        print("File already exists in the destination.")
    elif not os.path.exists(source_path):
        print("Source file does not exist.")
    else:
        shutil.copy(source_path, destination_path)
        print("File copied successfully.")


def move_file(source_path, destination_path):
    if os.path.exists(destination_path):
        print("File already exists in the destination.")
    elif not os.path.exists(source_path):
        print("Source file does not exist.")
    else:
        shutil.move(source_path, destination_path)
        print("File moved successfully.")


output_path = "../../crawl/files/youtube/hitomi/out"
publish_path = "../../crawl/files/youtube/hitomi/publish"
source_path = "../../crawl/files/youtube/hitomi"
test_path = "../../crawl/files/youtube/hitomi/test"
test2_path = "../../crawl/files/youtube/hitomi/test2"

check(test_path)
check(output_path)
check(publish_path)
check(test2_path)

mp4_files = get_mp4_files(test_path)
for file in mp4_files:
    video_info = get_video_info(file)
    video_name = video_info['name']
    video_length = video_info['duration']
    video_size = video_info['size']
    print(video_name, "###", video_length, "###", video_size)
    spilt_file_names = split_video(file, 20)
    for spilt_file_name in spilt_file_names:
        move_file(spilt_file_name, test2_path + "/" + os.path.basename(spilt_file_name))
    break
