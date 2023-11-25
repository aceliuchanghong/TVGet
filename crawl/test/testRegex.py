# 读取文件Hitomi-file,用正则提取/watch?v=vEYSSNqWXCI&amp 之中的vEYSSNqWXCI,并且拼接https://www.youtube.com/watch?v=
import re

# 定义一个空集合来存储独特的视频ID
unique_video_ids = set()
# 读取文件内容
with open('Hitomi-file', 'r', encoding='utf-8') as file:
    content = file.read()

# 正则表达式匹配/watch?v=和&amp之间的内容
pattern = re.compile(r'/watch\?v=(.*?)&amp')

matches = pattern.findall(content)

# 将找到的视频ID添加到集合中以确保它们是独一无二的
unique_video_ids.update(matches)

# 生成独特的完整YouTube URL
youtube_urls = [f'https://www.youtube.com/watch?v={video_id}' for video_id in unique_video_ids]
print(len(youtube_urls))
# 打印所有独特的YouTube URL
for url in youtube_urls:
    print(url)

