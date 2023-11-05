# npx playwright install
# playwright codegen www.douyin.com --save-storage=cookie.json

from playwright.async_api import async_playwright
import os
import asyncio
import json
import time

async def upload(playwright):
    upload_url1 = "https://creator.douyin.com/creator-micro/content/upload"
    upload_url2 = "https://creator.douyin.com/creator-micro/content/publish?enter_from=publish_page"

    browser = await playwright.chromium.launch(headless=False)
    current_path = os.path.dirname(os.path.abspath(__file__))
    cookie_path = os.path.join(current_path, "cookie.json")

    # Check if the cookie.json file exists and is not empty
    if not os.path.exists(cookie_path) or os.path.getsize(cookie_path) == 0:
        raise FileNotFoundError("The cookie.json file is missing or empty.")

    # Try to read the cookie.json file and parse it as JSON
    try:
        with open(cookie_path, 'r',encoding='utf-8') as cookie_file:
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
    await page.locator(
        "label:has-text(\"为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
        "../../crawl/files/mp4/20230411_1876fb0d819_r1_1200k.mp4")
    # Add your upload logic here
    print("a4")
    await page.wait_for_url(upload_url2)
    print("a5")
    # 视频越大间隔应越长
    time.sleep(3)
    # 标题
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[2]/input').fill('self.text')
    # 作品简介
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div').fill('self.text #发言')
    print("a6")
    await page.wait_for_url(upload_url2)
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
        await upload(playwright)

# Run the main function
asyncio.run(main())
