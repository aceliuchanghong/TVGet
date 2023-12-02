import sys
from crawl.main.setup import run_youtube

output_path = "../../crawl/files/youtube/hitomi/out"

try:
    # 此次视频上传数量
    nums = 5
    run_youtube(output_path, nums)
except Exception as e:
    print("main error:", e)
    sys.exit()
