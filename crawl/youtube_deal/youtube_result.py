from crawl.spiderDealer.Result import Result
from crawl.youtube_deal.youtube_util import *
from datetime import datetime


def get_result(file_path):
    info = get_video_info(file_path)
    video_name = info['name']
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y%m%d')

    result = Result(date=formatted_date, title=video_name, coverpath="youtube", anspath=file_path,
                    describe="如妖精鬼魅般的完美琵琶演奏:" + video_name)

    return result


# test = '../../crawl/files/youtube/hitomi/00.mp4'
# print(get_result(test))
