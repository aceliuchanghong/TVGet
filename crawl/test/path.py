import os

# 获取当前脚本所在的路径
current_path = os.path.dirname(os.path.abspath(__file__))

print('当前路径:', current_path)

# 获取当前工程路径
project_path = os.path.dirname(os.path.abspath(__file__))

print('当前工程路径:', project_path)