from crawl.spiderDealer.Result import Result
from crawl.spiderDealer.coverDeal import dealPoster
from crawl.spiderDealer.fileDownload import download
from crawl.spiderDealer.mp3Get import mp423
from crawl.spiderDealer.mp4Deal import *
from crawl.spiderDealer.praseFile import parse
from crawl.spiderDealer.srtGet import mp32srt
from crawl.spiderDealer.urlFileGet import getFile
from crawl.spiderDealer.srt2Txt import summarySrt
import shutil

url = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158313.shtml'
url2 = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158311.shtml'


def create(url):
    if len(url) <= 10:
        print("url is None")
        return
    filename = getFile(url)
    result = parse(filename)
    if "-横" in result.mp4name:
        print("视频:" + result.date + "-" + result.title + " 横版视频，跳过")
        return result
    result.coverpath = download(result.poster)
    result.mp4path = download(result.mp4url)

    result.mp3path = mp423(result.mp4path)

    result.srtpath = mp32srt(result)
    result.describe = summarySrt(result.srtpath)

    result.anspath = cutMp4(result.mp4path)
    result.anspath = srtAdd(result)
    result.coverpath = dealPoster(result)

    des = "../../crawl/files/publish/" + result.date + "." + result.title + "/"
    check(des)

    shutil.move(result.anspath, des + result.title + ".mp4")
    result.anspath = des + result.title + ".mp4"
    shutil.move(result.coverpath, des + result.title + ".jpg")
    result.coverpath = des + result.title + ".jpg"
    with open(des + result.title + '.txt', 'w') as file:
        file.write(str(result))
    # print(result.title + " create suc")

    print(result)
    return result

# result = Result(
#     name="毛宁",
#     date="20231009",
#     title="中方高度关注近来巴以冲突持续升级",
#     poster="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/17602.images/v17602_b1696855238519.jpg",
#     mp4name="中方高度关注巴以冲突持续升级-竖版.mp4",
#     mp4url="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/20231009_18b14740d6e_r1_1200k.mp4",
#     mp4path="../../crawl/files/mp4/20231009_18b14740d6e_r1_1200k.mp4",
#     mp3path="../../crawl/files/mp3/20231009_18b14740d6e_r1_1200k.mp3",
#     srtpath="../../crawl/files/srt/20231009_18b14740d6e_r1_1200k.srt",
#     coverpath="../../crawl/files/jpg/v17602_b1696855238519.jpg",
#     anspath=None,
#     describe="中方关注巴以冲突，呼吁停火恢复和平，并推动政治解决。"
# )
# print(str(result))
