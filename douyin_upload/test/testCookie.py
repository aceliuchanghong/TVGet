# npx playwright install
# playwright codegen www.douyin.com --save-storage=cookie.json

from playwright.async_api import async_playwright
import os
import asyncio
import json


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
    print("准备上传视频")
    await page.locator(
        "label:has-text(\"为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
        result.anspath)
    await page.wait_for_url(upload_url2)
    print("标题")
    # 标题
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[2]/input').fill(
        result.date + ":" + result.title)
    # 作品简介
    print("作品简介")
    await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[4]/div/div/div/div[1]/div').fill(
        result.describe)

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
            print("选择合集")
            await page.locator('text=发言视频合集').click()
        except:
            print("选择不了合集")
    except:
        print("选择合集没找到")

    # 发布键
    try:
        # 等待页面可能需要的加载时间
        await asyncio.sleep(10)
        # 点击按钮
        print("点击上传")
        await page.locator(
            'xpath=//*[@id="root"]//div/button[@class="button--1SZwR primary--1AMXd fixed--3rEwh"]').click()
        print("上传成功")
        await asyncio.sleep(1)
    except Exception as e:
        print("ERR:上传没有成功******************************************************************************************************")
        print("发布时失败:", e)


async def start(result):
    if "-横" in result.mp4name:
        print("视频:" + result.date + ":" + result.title + " ==>横版视频，跳过")
        return None
    async with async_playwright() as playwright:
        await upload(playwright, result)
