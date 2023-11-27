from playwright._impl._api_structures import ProxySettings
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    proxy_host = '127.0.0.1'
    proxy_port = 10809

    proxy = ProxySettings(server=f'http://{proxy_host}:{proxy_port}')
    browser = playwright.chromium.launch(headless=False, proxy=proxy)
    context = browser.new_context()
    page = context.new_page()

    # 访问YouTube并获取Cookie
    page.goto('https://www.youtube.com')

    # 增加等待时间，例如等待15秒钟
    page.wait_for_timeout(15000)


    cookies = context.cookies()
    print(cookies)

    # 关闭浏览器
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
