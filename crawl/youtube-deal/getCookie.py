from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    proxy_host = '127.0.0.1'
    proxy_port = 10809

    browser = playwright.chromium.launch(headless=False,proxy=f'http://{proxy_host}:{proxy_port}')
    context = browser.new_context(proxy={
        'server': f'http://{proxy_host}:{proxy_port}',
        'username': 'your_username',  # 如果需要身份验证，请提供用户名和密码
        'password': 'your_password'
    })
    page = context.new_page()

    # 访问YouTube并获取Cookie
    page.goto('https://www.youtube.com')
    cookies = context.cookies()
    print(cookies)

    # 关闭浏览器
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
