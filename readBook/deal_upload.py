from readBook.PicResult import PicResult
from playwright.async_api import async_playwright
import os
import json
import asyncio


async def upload_to_read_book(playwright, picResult, re_run):
    upload_url1 = "https://creator.xiaohongshu.com/publish/publish"
    upload_url2 = "https://creator.xiaohongshu.com/publish/success?source&bind_status=not_bind"
    keywords = [
        "高清壁纸",
        "好想谈恋爱",
        "每日壁纸",
        "插画",
        "公主",
        "女王",
        "目标",
        "对象",
        "生活",
        "原创壁纸",
        "AI绘画",
        "AI插画",
        "iphone壁纸",
        "动漫壁纸",
        "ipad壁纸",
        "完美女孩",
        "美女",
        "可爱女孩",
        "恋爱日常",
        "我和他"
    ]

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

    try:
        await page.goto(upload_url1)
        # 确保页面已经加载完成
        await page.wait_for_url(upload_url1)
        print("准备上传图片,切换至上传图片界面")
        await page.locator('//*[@id="web"]/div/div[1]/div[1]/div[2]/span').click()
        # 点击上传按钮
        file_input_locator = page.locator('//*[@id="web"]/div/div[1]/div[2]/div[1]/div/input')
        await file_input_locator.wait_for(state="visible")
        print("开始上传图片")
        # 封面
        await file_input_locator.set_input_files(
            [picResult.fix7path, picResult.fix6path, picResult.fix8path, picResult.downpath])
        print("开始设置标题")
        await page.locator('//*[@id="web"]/div/div[2]/div[2]/div[2]/input').fill(
            picResult.fix12path + "|" + picResult.anspath + "|My BFFs")
        print("开始设置话题")
        for i in keywords:
            css_selector = ".topic-container"
            await page.locator('//*[@id="topicBtn"]/span').click()
            await page.locator('//*[@id="post-textarea"]').type(i)
            await asyncio.sleep(1.5)
            await page.press(css_selector, "Enter")
        print("开始设置地点")
        await page.locator('//*[@id="web"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/input').fill('上海')
        await asyncio.sleep(2)
        await page.locator('//*[@id="web"]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div/div/div[1]/ul/li[1]').click()
        await asyncio.sleep(2)
        print("开始发布")
        try:
            # 点击 等待页面跳转，这里设置了一个超时时间
            async with page.expect_navigation(timeout=3000):
                await page.locator('//*[@id="web"]/div/div[2]/div[2]/div[7]/button[1]/span').click()
                await asyncio.sleep(2)
            # 检查当前页面的 URL
            if page.url == upload_url2:
                print("发布成功")
                return True
            else:
                print("ERR:跳转错误")
                return False
        except Exception as e:
            # 如果超时或者有其他异常，输出异常信息
            print(f"ERR:发布失败 {e}")
            return False
    except Exception as e:
        print(f"Upload error occurred: {e}")
        return False


async def start(picresult, re_run):
    async with async_playwright() as playwright:
        isOK = await upload_to_read_book(playwright, picresult, re_run=re_run)
        return isOK


if __name__ == '__main__':
    picresult = PicResult()
    picresult.name = "stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.ext = "png"
    picresult.date = "20231220"
    picresult.keyword = "She possesses an ethereal beauty, a timeless elegance that whispers softly to the heart, yet echoes profoundly."
    picresult.url = "https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.downpath = "../crawl/files/redbook/original_pic/640.jpg"
    picresult.bakpath = "../crawl/files/redbook/original_bak_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix1path = "../crawl/files/redbook/blur_pic/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix2path = "../crawl/files/redbook/words_pic/4.andriod.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix3path = "../crawl/files/redbook/words_pic/4.iphone.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix4path = "../crawl/files/redbook/words_pic/4.ipad.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix5path = "../crawl/files/redbook/words_pic/4.laptop.stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png"
    picresult.fix6path = "../crawl/files/redbook/original_pic/640.jpg"
    picresult.fix7path = "../crawl/files/redbook/original_pic/640.jpg"
    picresult.fix8path = "../crawl/files/redbook/original_pic/640.jpg"
    picresult.fix9path = "None"
    picresult.fix10path = "None"
    picresult.fix11path = "None"
    picresult.fix12path = "ttt"
    picresult.anspath = "玉立花容月下生"
    picresult.describe = "SUC"

    if picresult.describe == "SUC":
        asyncio.run(start(picresult, False))
    else:
        print("??")
