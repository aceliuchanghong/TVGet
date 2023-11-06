from playwright.sync_api import sync_playwright

def upload_video(video_path, title, description):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 设置headless=False可以看到浏览器操作
        page = browser.new_page()
        page.goto('https://www.youtube.com/upload')

        # 登录过程（根据实际情况编写）
        # page.fill('input[name="login"]', 'your_username')
        # page.fill('input[name="password"]', 'your_password')
        # page.click('button[type="submit"]')

        # 等待页面加载并选择视频文件上传
        page.set_input_files('input[type="file"]', video_path)

        # 填写视频标题和描述
        page.fill('textarea[aria-label="Title"]', title)
        page.fill('textarea[aria-label="Description"]', description)

        # 发布视频
        page.click('button:has-text("Publish")')

        # 等待视频上传完成
        page.wait_for_selector('text=Video published')

        browser.close()

# 使用函数上传视频
upload_video('/path/to/your/video.mp4', 'Your Video Title', 'Your video description.')
