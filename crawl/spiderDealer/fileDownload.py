from crawl.spiderDealer.checkPath import check
def download(fileUrl):
    import requests
    try:
        # Download file
        response = requests.get(fileUrl, stream=True)
        # Get file name
        fileName = fileUrl.split('/')[-1]
        # Get file extension
        fileExtension = fileUrl.split('.')[-1]

        relative_path = '../../crawl/files/'
        check(relative_path + fileExtension)

        # Get file path
        filePath = relative_path + fileExtension + '/' + fileName
        # Write file
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        # Return file path
        return filePath
    except Exception as e:
        print(e)
        return None


# url = 'https://svideo.mfa.gov.cn/masvod/public/2023/10/09/20231009_18b1474a8fa_r1_1200k.mp4'
# print(download('https://svideo.mfa.gov.cn/masvod/public/2023/10/09/17603.images/v17603_b1696855283735.jpg'))
# download(url)
