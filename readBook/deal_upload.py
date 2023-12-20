from readBook.PicResult import PicResult
from playwright.async_api import async_playwright
import os
import json
import asyncio


async def upload_to_read_book(playwright, picResult, re_run):
    upload_url1 = "https://creator.xiaohongshu.com/creator/home"

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
    await asyncio.sleep(100)
    print("准备上传视频")
    await page.locator(
        "label:has-text(\"为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
        picResult.fix1path)


async def start(picresult, re_run):
    async with async_playwright() as playwright:
        await upload_to_read_book(playwright, picresult, re_run=re_run)


if __name__ == '__main__':
    picresult = PicResult()
    picresult.name = "stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.ext = "png"
    picresult.date = "20231220"
    picresult.keyword = "She possesses an ethereal beauty, a timeless elegance that whispers softly to the heart, yet echoes profoundly."
    picresult.url = "https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.downpath = "../crawl/files/redbook/original_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.bakpath = "../crawl/files/redbook/original_bak_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix1path = "../crawl/files/redbook/blur_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix2path = "../crawl/files/redbook/words_pic/4.andriod.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix3path = "../crawl/files/redbook/words_pic/4.iphone.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix4path = "../crawl/files/redbook/words_pic/4.ipad.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix5path = "../crawl/files/redbook/words_pic/4.laptop.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix6path = "../crawl/files/redbook/words_pic/words.model2.5.4.andriod.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix7path = "../crawl/files/redbook/words_pic/words.model2.5.4.iphone.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix8path = "../crawl/files/redbook/words_pic/words.model3.5.4.laptop.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix9path = "None"
    picresult.fix10path = "None"
    picresult.fix11path = "None"
    picresult.fix12path = "None"
    picresult.anspath = "None"
    picresult.describe = "SUC"

    if picresult.describe == "SUC":
        asyncio.run(start(picresult, False))
        # if bool_test:
        #     with open('../readBook/uploaded.log', 'w') as file:
        #         file.write(f"{testPicResult.url}\n")
        # else:
        #     print("ERR")
    else:
        print("??")
