# npx playwright install
# playwright codegen www.toutiao.com --save-storage=cookie.json

from playwright.async_api import async_playwright
import os
import asyncio
import json
import time

from crawl.spiderDealer.Result import Result


async def upload(playwright, result):
    upload_url1 = "https://mp.toutiao.com/profile_v4/xigua/upload-video"

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
    print("a1")
    print("a2")
    await page.wait_for_url(upload_url1)

    print("a3")
    page.locator("div:has-text(\"点击上传或将文件拖入此区域\")")
    print("a4")
    await page.set_input_files('input[type="file"]', result.anspath)

    print("a5")
    # 视频越大间隔应越长
    time.sleep(3)
    # 标题
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[2]/input').fill('self.text')
    # 作品简介
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div').fill(
        'self.text #发言')
    print("a6")
    # await page.wait_for_url(upload_url2)
    print("a7")
    # 发布键
    # await page.locator('xpath=//*[@id="root"]//div/button[@class="button--1SZwR primary--1AMXd fixed--3rEwh"]').click()
    print("a8")
    # await page.wait_for_timeout(6000)
    time.sleep(20)
    # await context.storage_state(path=self.path + "\\cookie.json")
    # Close the page and context after the upload is done


async def main():
    async with async_playwright() as playwright:
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
            anspath="C:\\Users\\liuch\\AppData\\Roaming\\Tencent\\WeMeet\\Global\\Resource\\b9a13512ff6cea6c2df0276865fa3418\\1665669595.mp4",
            describe="中方关注巴以冲突，呼吁停火恢复和平，并推动政治解决。"
        )
        await upload(playwright, result)


# Run the main function
asyncio.run(main())
#
# 使用文本选择器:
# 如果上传区域的文本提示与 input 元素相关联，你可以尝试使用包含文本的选择器来定位 input 元素。例如：
#
# javascript
# Copy code
# await page.locator('text=点击上传或将文件拖入此区域').set_input_files(result.anspath);
# 使用 CSS 选择器:
# 如果你知道 input 元素的 CSS 类或 ID，你可以直接使用它。例如，如果 input 的类名是 .file-input：
#
# javascript
# Copy code
# await page.locator('.file-input').set_input_files(result.anspath);
# 使用 XPath:
# 如果 input 元素的位置固定，你可以使用 XPath 来定位。例如：
#
# javascript
# Copy code
# await page.locator('xpath=//input[@type="file"]').set_input_files(result.anspath);
# 触发点击事件:
# 如果 input 元素在点击某个区域后才会出现，你可能需要先触发点击事件。例如：
#
# javascript
# Copy code
# await page.click('div.upload-tip'); // 假设点击这个 div 会触发 input 出现
# await page.locator('input[type="file"]').set_input_files(result.anspath);