from crawl.spiderDealer.checkPath import check
from crawl.spiderDealer.fileDownload import download
import re

urls_list = [
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181108336666619944/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png?ex=657fdbdb&is=656d66db&hm=964e641959d644d62e12d30ef86a5f655f73437a8862508c14371d6144cf4cb4&'
]

proxy_host = '127.0.0.1'
proxy_port = 10809
proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_host}:{proxy_port}'
}
path = '../crawl/files/redbook/original_pic'
check(path)

for url in urls_list:
    # 使用正则表达式提取文件名
    pattern = r'\/([^\/]+)\.png'
    match = re.search(pattern, url)
    if match:
        filename = match.group(1) + ".png"
        # print("提取到的文件名是：", filename)
    else:
        print("未找到匹配的文件名！")
        break
    pattern2 = r'\?.*'
    clean_url = re.sub(pattern2, '', url)
    download(fileUrl=clean_url, name=filename, path=path, proxies=proxies)
