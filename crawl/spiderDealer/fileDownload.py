from crawl.spiderDealer.checkPath import check
import requests
import os


def download(fileUrl, name=None, path=None, proxies=None, re_run=False):
    try:
        # Get file name
        fileName = fileUrl.split('/')[-1]
        if name is not None:
            fileName = name

        # Get file extension
        fileExtension = fileUrl.split('.')[-1]

        relative_path = '../../crawl/files/'
        check(relative_path + fileExtension)

        # Get file path
        filePath = relative_path + fileExtension + '/' + fileName
        if path is not None:
            filePath = path + '/' + fileName
        if not os.path.exists(filePath) or re_run:
            # Write file
            # Download file
            response = requests.get(fileUrl, stream=True, proxies=proxies)
            with open(filePath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            # Return file path
            print("download " + fileExtension + " suc")
        return filePath
    except Exception as e:
        print(e)
        return "ERR:download"
