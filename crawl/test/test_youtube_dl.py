import sys

from pytube import YouTube
from crawl.spiderDealer.checkPath import check
import os
import socks
import socket

from crawl.spiderDealer.net import testNet


def download_youtube_video(url):
    # 设置代理
    proxy_host = '127.0.0.1'
    proxy_port = 10809
    socks.set_default_proxy(socks.HTTP, proxy_host, proxy_port)
    socket.socket = socks.socksocket

    try:
        output_path = "../../crawl/files/youtube/hitomi"
        check(output_path)
        # 创建 YouTube 对象
        yt = YouTube(url)
        video_name = yt.title

        if video_name.find("演奏") == -1:
            return

        new_file_path = output_path + "/" + video_name + ".mp4"
        if os.path.exists(new_file_path):
            print("File already exists:", new_file_path)
            return
        # 获取视频的最高质量的视频流
        stream = yt.streams.get_highest_resolution()
        # 开始下载
        stream.download(output_path=output_path)
        print("File SUC:", new_file_path)

    except Exception as e:
        print("download_youtube_video error:", e)
        print(url)
        return False


# url = 'https://www.youtube.com/watch?v=7lrm2PJxNUk&ab_channel=Arrow'
# download_youtube_video(url)

urls = ['https://www.youtube.com/watch?v=pSQteFmoVz0',
        'https://www.youtube.com/watch?v=XhwqyvZ8QqM',
        'https://www.youtube.com/watch?v=10tWnkBjNRI',
        'https://www.youtube.com/watch?v=jR69OHDlhSM',
        'https://www.youtube.com/watch?v=PHrIK5zkWHo',
        'https://www.youtube.com/watch?v=Hw10gDpm1fU',
        'https://www.youtube.com/watch?v=gvSmeFHppr4',
        'https://www.youtube.com/watch?v=UOj3EqBQxyk',
        'https://www.youtube.com/watch?v=Mif5IjpB8i4',
        'https://www.youtube.com/watch?v=iDxxEekbExw',
        'https://www.youtube.com/watch?v=eqbrqX1aoLs',
        'https://www.youtube.com/watch?v=FjtyzNw5vcw',
        'https://www.youtube.com/watch?v=pydK1LJ5TvU',
        'https://www.youtube.com/watch?v=_HXgMcKGnto',
        'https://www.youtube.com/watch?v=DpeeoknoTkk',
        'https://www.youtube.com/watch?v=ckWs7EyMWNI',
        'https://www.youtube.com/watch?v=-8zK9pMQo5Y',
        'https://www.youtube.com/watch?v=wIi1V464TCE',
        'https://www.youtube.com/watch?v=9IOMlbTAQ60',
        'https://www.youtube.com/watch?v=ojALe6ieI3g',
        'https://www.youtube.com/watch?v=_bPpMDOBT_8',
        'https://www.youtube.com/watch?v=d1rLHe7hqL8',
        'https://www.youtube.com/watch?v=H9o1XgjIUDs',
        'https://www.youtube.com/watch?v=el5ycmLNnr0',
        'https://www.youtube.com/watch?v=P-iOkgrcdCE',
        'https://www.youtube.com/watch?v=EL2ioOcB4Xg',
        'https://www.youtube.com/watch?v=ZInHgsLRmvk',
        'https://www.youtube.com/watch?v=1_yAQMeIgs0',
        'https://www.youtube.com/watch?v=_UZYwGDaBHI',
        'https://www.youtube.com/watch?v=7s03MaLNsgA',
        'https://www.youtube.com/watch?v=Eh8OfF5SLts',
        'https://www.youtube.com/watch?v=CFgXc2Os6PQ',
        'https://www.youtube.com/watch?v=RgErSuu0DJo',
        'https://www.youtube.com/watch?v=pfhLi6sS_g4',
        'https://www.youtube.com/watch?v=ST3Q5tg9XPA',
        'https://www.youtube.com/watch?v=UthKeP9u3mw',
        'https://www.youtube.com/watch?v=v3aH1DKJZpg',
        'https://www.youtube.com/watch?v=8ItMhuro63w',
        'https://www.youtube.com/watch?v=X9Ykp71tdmU',
        'https://www.youtube.com/watch?v=B-bTuiGks2s',
        'https://www.youtube.com/watch?v=5TG9tGORQ34',
        'https://www.youtube.com/watch?v=6Nz6xJYVKeM',
        'https://www.youtube.com/watch?v=xXwH4HXuc_k',
        'https://www.youtube.com/watch?v=8zFRPIXmSd0',
        'https://www.youtube.com/watch?v=X1761hxeyME',
        'https://www.youtube.com/watch?v=MDNwHmguBwg',
        'https://www.youtube.com/watch?v=p8UdDhBVf5A',
        'https://www.youtube.com/watch?v=UYp-Fbl9OWg',
        'https://www.youtube.com/watch?v=LoTAFvoqkoA',
        'https://www.youtube.com/watch?v=8Uq87DU_FLs',
        'https://www.youtube.com/watch?v=NpgOAeQ0lWs',
        'https://www.youtube.com/watch?v=r83n_2C3nWg',
        'https://www.youtube.com/watch?v=CjTkbTRIwuM',
        'https://www.youtube.com/watch?v=_fDAT-8OI9g',
        'https://www.youtube.com/watch?v=YHkeByw8jfc',
        'https://www.youtube.com/watch?v=vEYSSNqWXCI',
        'https://www.youtube.com/watch?v=eRlo3WNH7a0',
        'https://www.youtube.com/watch?v=iD-5ttadahE',
        'https://www.youtube.com/watch?v=I9UyAFa3BH8',
        'https://www.youtube.com/watch?v=NbSRrha0b1o',
        'https://www.youtube.com/watch?v=2Ec3STz2LEQ', ]

if not testNet():
    sys.exit()
for url in urls:
    download_youtube_video(url)
