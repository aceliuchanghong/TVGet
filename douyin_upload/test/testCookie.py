# npx playwright install
# playwright codegen www.douyin.com --save-storage=cookie.json

from playwright.async_api import async_playwright
import os
import asyncio
import json
import time

from crawl.spiderDealer.Result import Result


async def upload(playwright, result):
    upload_url1 = "https://creator.douyin.com/creator-micro/content/upload"
    upload_url2 = "https://creator.douyin.com/creator-micro/content/publish?enter_from=publish_page"

    browser = await playwright.chromium.launch(headless=False)
    current_path = os.path.dirname(os.path.abspath(__file__))
    cookie_path = os.path.join(current_path, "cookie.json")

    if not os.path.exists(cookie_path) or os.path.getsize(cookie_path) == 0:
        raise FileNotFoundError("The cookie.json file is missing or empty.")
    try:
        with open(cookie_path, 'r', encoding='utf-8') as cookie_file:
            storage_state = json.load(cookie_file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error reading the cookie.json file: {e}")

    context = await browser.new_context(storage_state=storage_state)
    page = await context.new_page()

    await page.goto(upload_url1)
    await page.wait_for_url(upload_url1)

    print("a3")
    await page.locator(
        "label:has-text(\"为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
        result.anspath)
    print("a4")
    await page.wait_for_url(upload_url2)
    print("a5")
    # 标题
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[2]/input').fill(
        result.date + ":" + result.title)
    # 作品简介
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div').fill(
        result.describe)
    print("a6")

    # # 设置封面 成功了,但是需要选择区域,不如不选
    # await page.locator('//*[@id="root"]/div/div/div[2]/div[1]/div[7]/div/div[1]/div[1]/div[2]').click()
    # print("找到上传封面")
    # await page.locator('//*[@id="dialog-0"]/div/div/div/div/div[1]/div/div/div[2]').click()
    # print("上传封面")
    # await page.set_input_files('input[type="file"]', result.coverpath)

    # 选择合集
    try:
        # await page.locator('//*[@id="root"]/div/div/div[2]/div[1]/div[13]/div[2]/div[2]/div[1]/div/span')
        await page.locator('//*[@id="root"]/div/div/div[2]/div[1]/div[13]/div[2]/div[2]/div[1]/div/span/div').click()
        try:
            await page.locator('text=发言视频合集').click()
        except:
            print("选择不了合集")
    except:
        print("选择合集没找到")

    # 发布键
    try:
        # 等待页面可能需要的加载时间
        await asyncio.sleep(5)
        # 获取所有的消息文本
        msg = await page.locator('//*[@class="semi-toast-content-text"]').all_text_contents()
        # 检查消息中是否有"上传成功"
        upload_success = any(m == "上传成功" for m in msg)
        i = 0
        # 如果没有找到"上传成功"，则等待一段时间并重新检查
        while not upload_success and i < 10:
            await asyncio.sleep(1)  # 使用异步的sleep
            msg = await page.locator('//*[@class="semi-toast-content-text"]').all_text_contents()
            upload_success = any("上传成功" in m for m in msg)
            i += 1
        # 如果上传成功，点击按钮
        if upload_success:
            await page.locator(
                'xpath=//*[@id="root"]//div/button[@class="button--1SZwR primary--1AMXd fixed--3rEwh"]').click()
        else:
            print("上传没有成功")
    except Exception as e:
        print("发布时失败:", e)


async def main(result):
    async with async_playwright() as playwright:
        await upload(playwright, result)


# # Run the main function
# result = Result(
#     #     # name="毛宁",
#     #     # date="20231009",
#     #     # title="中方高度关注近来巴以冲突持续升级",
#     #     # poster="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/17602.images/v17602_b1696855238519.jpg",
#     #     # mp4name="中方高度关注巴以冲突持续升级-竖版.mp4",
#     #     # mp4url="https://svideo.mfa.gov.cn/masvod/public/2023/10/09/20231009_18b14740d6e_r1_1200k.mp4",
#     #     # mp4path="../../crawl/files/mp4/20231009_18b14740d6e_r1_1200k.mp4",
#     #     # mp3path="../../crawl/files/mp3/20231009_18b14740d6e_r1_1200k.mp3",
#     #     # srtpath="../../crawl/files/srt/20231009_18b14740d6e_r1_1200k.srt",
#     #     # coverpath="../../crawl/files/jpg/v17602_b1696855238519.jpg",
#     #     # anspath="../../crawl/files/mp4/20230411_1876fb0d819_r1_1200k.mp4",
#     #     # describe="中方关注巴以冲突，呼吁停火恢复和平，并推动政治解决。"
#     name="None",
#     date="20231101",
#     title="中美双方要切实“重回巴厘岛”，把两国元首的共识真正落到实处（2023年11月1日）",
#     poster="https://svideo.mfa.gov.cn/masvod/public/2023/11/01/18290.images/v18290_b1698853296445.jpg",
#     mp4name="视频二：中美双方要切实“重回巴厘岛”，把两国元首共识真正落到实处.mp4",
#     mp4url="https://svideo.mfa.gov.cn/masvod/public/2023/11/01/20231101_18b8b8bd814_r1_1200k.mp4",
#     mp4path="../../crawl/files/mp4/20231101_18b8b8bd814_r1_1200k.mp4",
#     mp3path="../../crawl/files/mp3/20231101_18b8b8bd814_r1_1200k.mp3",
#     srtpath="../../crawl/files/srt/20231101_18b8b8bd814_r1_1200k_utf-8.srt",
#     coverpath="../../crawl/files/publish/20231101.中美双方要切实“重回巴厘岛”，把两国元首的共识真正落到实处（2023年11月1日）/中美双方要切实“重回巴厘岛”，把两国元首的共识真正落到实处（2023年11月1日）.jpg",
#     anspath="../../crawl/files/publish/20231101.中美双方要切实“重回巴厘岛”，把两国元首的共识真正落到实处（2023年11月1日）/中美双方要切实“重回巴厘岛”，把两国元首的共识真正落到实处（2023年11月1日）.mp4",
#     describe="美中原则同意在旧金山举行首脑会谈，需切实落实共识。"
name="汪文斌",
date="20231106",
title="希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件",
poster="https://svideo.mfa.gov.cn/masvod/public/2023/11/06/18402.images/v18402_b1699276963856.jpg",
mp4name="希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件.mp4",
mp4url="https://svideo.mfa.gov.cn/masvod/public/2023/11/06/20231106_18ba4cc933b_r1_1200k.mp4",
mp4path="../../crawl/files/mp4/20231106_18ba4cc933b_r1_1200k.mp4",
mp3path="../../crawl/files/mp3/20231106_18ba4cc933b_r1_1200k.mp3",
srtpath="../../crawl/files/srt/20231106_18ba4cc933b_r1_1200k_utf-8.srt",
coverpath="../../crawl/files/publish/20231106.希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件/希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件.jpg",
anspath="../../crawl/files/publish/20231106.希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件/希望美方同中方相向而行，为两国地方和民间交往合作创造有利条件.mp4",
describe="习近平寄信希望中美友诚大会成为交流桥梁，推动关系健康发展。"
# )
# asyncio.run(main(result))
