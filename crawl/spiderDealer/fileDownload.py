from crawl.spiderDealer.checkPath import check
import requests


def download(fileUrl, name=None):
    try:
        # Download file
        response = requests.get(fileUrl, stream=True)
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
        # Write file
        with open(filePath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        # Return file path
        print("download SUC")
        return filePath
    except Exception as e:
        print(e)
        return None
