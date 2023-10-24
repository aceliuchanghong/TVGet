import os


def check(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"创建目录：{path}")
    else:
        pass

