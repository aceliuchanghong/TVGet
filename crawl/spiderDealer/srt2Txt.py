import os
import openai
import pysrt


def summarySrt(srtpath):
    with open(srtpath, "r", encoding='utf-8') as file:
        content = file.read()
        # print(content)
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.isdigit() or '-->' in line:
            continue
        cleaned_lines.append(line)

    # 将换行符替换为逗号
    result = ''.join(cleaned_lines)

    prompt = "总结以下内容为15个字以内的句子:" + result
    print("summary SUC")
    return response(prompt)


def response(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    proxyHost = "127.0.0.1"
    proxyPort = 10809

    proxies = {
        "http": f"http://{proxyHost}:{proxyPort}",
        "https": f"http://{proxyHost}:{proxyPort}"
    }
    openai.proxy = proxies

    completion = openai.ChatCompletion.create(
        model="gpt-4-0613",  # gpt-3.5-turbo gpt-4-0613
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    print("gpt ans SUC")
    return completion.choices[0].message.content


def modify_subtitle(srt_path, chars_per_line):
    subs = pysrt.open(srt_path, encoding='utf-8')

    for sub in subs:
        text = sub.text
        # print(text)
        new_text = ""

        # 将字幕文本分割成每行包含指定数量的字
        for i in range(0, len(text), chars_per_line):
            line = text[i:i + chars_per_line]
            new_text += line + "\n"

        sub.text = new_text.strip()
    last_srt_path = srt_path.replace(".srt", "_utf-8.srt")
    subs.save(last_srt_path, encoding='utf-8')

    return last_srt_path
