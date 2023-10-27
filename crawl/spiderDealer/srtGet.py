from crawl.spiderDealer.checkPath import check
import os
import sys
import openai
import io

from crawl.spiderDealer.srt2Txt import modify_subtitle

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def mp32srt(result, name=None):
    # Get file name
    mp3path = result.mp3path
    output_file = mp3path.split('/')[-1].replace("mp3", "srt")

    if name is not None:
        output_file = name
    # print(output_file)

    proxyHost = "127.0.0.1"
    proxyPort = 10809
    proxies = {
        "http": f"http://{proxyHost}:{proxyPort}",
        "https": f"http://{proxyHost}:{proxyPort}"
    }
    openai.proxy = proxies
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # print(openai.api_key)

    relative_path = '../../crawl/files/srt/'
    check(relative_path)
    realFilePath = relative_path + output_file
    if not os.path.exists(realFilePath):
        prompt = "这是一段关于中国外交部的发言稿,主要包括" + result.title
        # print(realFilePath, prompt)

        try:
            file = open(mp3path, "rb")
            transcript = openai.Audio.transcribe("whisper-1", file, response_format="srt",
                                                 prompt=prompt)
            with open(realFilePath, 'w', encoding='utf-8') as f:
                f.write(transcript)
            print("srt from gpt SUC")

        except Exception as e:
            print("Srt deal Error:", e)

    last_path = modify_subtitle(realFilePath, 15)
    print("srt modify SUC")

    return last_path
