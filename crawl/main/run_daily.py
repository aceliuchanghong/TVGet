import sys
from crawl.main.setup import run
from crawl.spiderDealer.sourceDeal import run_every_day

always_new = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/index.shtml'

try:
    run(run_every_day(always_new))
except Exception as e:
    print("main error:", e)
    sys.exit()
