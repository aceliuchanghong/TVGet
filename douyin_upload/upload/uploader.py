# -*- coding: utf-8 -*-
from playwright.async_api import Playwright, async_playwright
import time
import datetime
import requests
from xml.etree import ElementTree
import wave
import os
import asyncio


class Uploader():
    async def up(self, playwright: Playwright) -> None:
        # 上传视频
        browser = await playwright.chromium.launch(headless=False)

        context = await browser.new_context(storage_state=self.path + "\\cookie.json")

        page = await context.new_page()

        await page.goto("https://creator.douyin.com/creator-micro/content/upload")

        await page.locator("button:has-text(\"发布视频\")").click()
        await page.wait_for_url("https://creator.douyin.com/creator-micro/content/upload")

        await page.locator(
            "label:has-text(\"点击上传 或直接将视频文件拖入此区域为了更好的观看体验和平台安全，平台将对上传的视频预审。超过40秒的视频建议上传横版视频\")").set_input_files(
            "temps.mp4")

        await page.wait_for_url("https://creator.douyin.com/creator-micro/content/publish")
        time.sleep(20)

        await page.locator('xpath=//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div').fill(
            self.text)
        # 视频越大间隔应越长
        time.sleep(30)
        await page.locator(
            'xpath=//*[@id="root"]//div/button[@class="button--1SZwR primary--1AMXd fixed--3rEwh"]').click()
        await page.wait_for_timeout(6000)

        await context.storage_state(path=self.path + "\\cookie.json")
        await context.close()
        await browser.close()

    async def main(self):
        async with async_playwright() as playwright:
            await self.up(playwright)
