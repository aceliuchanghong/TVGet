import os


def check(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass
    except Exception as e:
        print(f"创建目录发生错误：{str(e)}")
