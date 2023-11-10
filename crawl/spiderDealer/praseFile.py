# 如lxml或xml.etree.ElementTree来解析XML或HTML文档，并使用XPath表达式来提取需要的值。
from crawl.spiderDealer.Result import Result
from crawl.spiderDealer.urlFileGet import parseUrlGetPic, parseUrlGetMp4
from crawl.spiderDealer.checkPath import check
from lxml import etree

def parse(fileName):
    try:
        basicpath = "../../crawl/files/response/"
        check(basicpath)
        filepath = "../../crawl/files/response/" + fileName
        # 打开文件并读取内容
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用lxml库解析HTML内容
        tree = etree.HTML(content)
        # 使用XPath表达式提取需要的值
        alltitle = tree.xpath('/html/body/div[4]/div[2]/div/div[1]/h1/text()')
        try:
            mp4urlstart = tree.xpath('/html/body/div[4]/div[2]/div/div[2]/div/p[1]/iframe/@src')[0]
            mp4name = tree.xpath('/html/body/div[4]/div[2]/div/div[2]/div/p[1]/iframe/@name')[0]
        except:
            try:
                mp4urlstart = tree.xpath('/html/body/div[4]/div[2]/div/div[2]/div/p[2]/iframe/@src')[0]
                mp4name = tree.xpath('/html/body/div[4]/div[2]/div/div[2]/div/p[2]/iframe/@name')[0]
            except Exception as e:
                print("prase mp4 error")
                # print(result)
                print(e)
                return None
        # print(alltitle[0])
        if "：" in alltitle[0]:
            name = alltitle[0].split("：")[0]
            title = alltitle[0].split("：")[1].split("（")[0]
        else:
            name = None
            title = alltitle[0]
        date = fileName.split("_")[0][1:]
        poster = parseUrlGetPic(mp4urlstart)
        mp4url = parseUrlGetMp4(mp4urlstart)

        result = Result(name, date, title, poster, mp4name, mp4url)
        print("prase file suc")
        return result
    except Exception as e:
        print("prase file error")
        # print(result)
        print(e)
        return None
