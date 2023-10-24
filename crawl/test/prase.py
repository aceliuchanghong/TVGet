import requests

# Fetch the webpage content
url = "https://svideo.mfa.gov.cn/mas/openapi/pages.do?method=exPlay&appKey=gov&id=17603&autoPlay=false"
response = requests.get(url)
web_content = response.content.decode('utf-8')

print(web_content)
