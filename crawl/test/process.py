from crawl.spiderDealer.Result import Result
from crawl.spiderDealer.fileDownload import download
from crawl.spiderDealer.mergeMp4 import merge_video_with_subtitles
from crawl.spiderDealer.mp3Get import mp423
from crawl.spiderDealer.praseFile import parse
from crawl.spiderDealer.srtGet import mp32srt
from crawl.spiderDealer.urlFileGet import getFile
from crawl.spiderDealer.srt2Txt import summarySrt

url = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158313.shtml'
url2 = 'https://www.fmprc.gov.cn/web/sp_683685/wjbfyrlxjzh_683691/202310/t20231009_11158311.shtml'

# filename = getFile(url2)
# result = parse(filename)
# result.coverpath = download(result.poster)
# result.mp4path = download(result.mp4url)
#
# result.mp3path = mp423(result.mp4path)
#
# result.srtpath = mp32srt(result)
# result.describe = summarySrt(result.srtpath)

result = Result(
    name="毛宁",
    date="20231009",
    title="中方高度关注近来巴以冲突持续升级",
    poster="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/17602.images/v17602_b1696855238519.jpg",
    mp4name="中方高度关注巴以冲突持续升级-竖版.mp4",
    mp4url="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/20231009_18b14740d6e_r1_1200k.mp4",
    mp4path="../../crawl/files/mp4/20231009_18b14740d6e_r1_1200k.mp4",
    mp3path="../../crawl/files/mp3/20231009_18b14740d6e_r1_1200k.mp3",
    srtpath="../../crawl/files/srt/20231009_18b14740d6e_r1_1200k.srt",
    coverpath="../../crawl/files/jpg/v17602_b1696855238519.jpg",
    anspath=None,
    describe="中方关注巴以冲突，呼吁停火恢复和平，并推动政治解决。"
)

merge_video_with_subtitles(result.mp4path, result.srtpath, result.mp4name)

print(result)
