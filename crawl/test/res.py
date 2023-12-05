import re

# 定义要匹配的字符串
url1 = "https://cdn.discordapp.com/attachments/1008049088324972657/1179093412490784890/CARD49_Process-GIF.gif?ex=65788750&is=65661250&hm=1c6917e5578620820e9a504d2e8ab8aa8b96f27f148a4be021241e48e7f1cca2&"
url2 = "https://cdn.discordapp.com/attachments/1038329663187062804/1181384573897158656/Geisha_3.png?ex=6580dd1f&is=656e681f&hm=f451a0d1875cb69a9335eec0afb5f50ae4f800d02c061168131b68eb95acda3f&"

# 编写正则表达式，匹配文件名
pattern = r"/([\w-]+)\.\w+\?"

# 使用正则表达式进行匹配
match1 = re.search(pattern, url1)
match2 = re.search(pattern, url2)

# 提取匹配到的文件名
if match1:
    filename1 = match1.group(1)
else:
    filename1 = "未找到匹配的文件名"

if match2:
    filename2 = match2.group(1)
else:
    filename2 = "未找到匹配的文件名"

# 输出结果
print("第一个链接的文件名是:", filename1)
print("第二个链接的文件名是:", filename2)
