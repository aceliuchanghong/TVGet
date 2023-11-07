import requests


def testNet():
    proxyHost = "127.0.0.1"
    proxyPort = 10809
    proxies = {
        "http": f"http://{proxyHost}:{proxyPort}",
        "https": f"http://{proxyHost}:{proxyPort}"
    }

    url = "https://www.youtube.com/"

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        # print("连接成功")
        return True
    except requests.exceptions.RequestException as e:
        print(f"v2ray链接失效：{str(e)}")
        return False
    except Exception as e:
        print(f"v2ray链接失效：{str(e)}")
        return False
