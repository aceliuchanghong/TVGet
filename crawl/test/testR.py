from crawl.spiderDealer.Result import Result
from crawl.spiderDealer.coverDeal import dealPoster

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
    coverpath="../../crawl/files/jpg/v18138_b1698233754583.jpg",
    anspath=None,
    describe="中方关注巴以冲突，呼吁停火恢复和平，并推动政治解决。"
)

result.coverpath = dealPoster(result)
print(result)
