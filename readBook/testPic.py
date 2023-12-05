from crawl.spiderDealer.checkPath import check
from crawl.spiderDealer.fileDownload import download
import re

urls_list = [
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181108336666619944/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png?ex=657fdbdb&is=656d66db&hm=964e641959d644d62e12d30ef86a5f655f73437a8862508c14371d6144cf4cb4&',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181114698293313588/eggon_a_still_from_a_1987_Yoshitaka_Amano_anime_pirates_approa_1b3e75d4-2022-46c0-b957-1d5b659116b4.png?ex=657fe1c8&is=656d6cc8&hm=95ce0b84ff100d10541018bc89a19d6b43e92ecc884560412cf89f2c0057c0cd&',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181384573897158656/Geisha_3.png?ex=6580dd1f&is=656e681f&hm=f451a0d1875cb69a9335eec0afb5f50ae4f800d02c061168131b68eb95acda3f&',
    'https://cdn.discordapp.com/attachments/1008049088324972657/1179093412490784890/CARD49_Process-GIF.gif?ex=65788750&is=65661250&hm=1c6917e5578620820e9a504d2e8ab8aa8b96f27f148a4be021241e48e7f1cca2&',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''
]


def getRedBookPic(urls_list, path=None):
    proxy_host = '127.0.0.1'
    proxy_port = 10809
    proxies = {
        'http': f'http://{proxy_host}:{proxy_port}',
        'https': f'http://{proxy_host}:{proxy_port}'
    }
    path = '../crawl/files/redbook/original_pic'
    check(path)

    err_list = []
    for url in urls_list:
        if url is not None and len(url) > 0:
            # 使用正则表达式提取文件名
            pattern1 = r"/([\w-]+)\.\w+\?"
            match = re.search(pattern1, url)
            if match:
                match_ext = re.search(r'\.(gif|png)\?', url)
                if match_ext:
                    file_ext_1 = match_ext.group(1)
                    filename = match.group(1) + "." + file_ext_1
                else:
                    print("后缀未匹配到！")
                    break
            else:
                # print("未找到匹配的文件名！")
                # print("#" + url + "#")
                err_list.append(url)
                continue
            pattern2 = r'\?.*'
            clean_url = re.sub(pattern2, '', url)
            download(fileUrl=clean_url, name=filename, path=path, proxies=proxies)
    if (len(err_list) > 0):
        print("未下载的图片链接：")
        print(err_list)


if __name__ == '__main__':
    getRedBookPic(urls_list)
