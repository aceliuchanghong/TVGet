import sys
from crawl.main.setup import run
from crawl.spiderDealer.sourceDeal import run_specific

try:
    # 上传倒数第几页数的视频
    page_num = 2
    # 此次视频上传数量
    nums = 1
    run(run_specific(page_num, nums))
except Exception as e:
    print("main error:", e)
    sys.exit()
