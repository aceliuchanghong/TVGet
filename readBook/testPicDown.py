from crawl.spiderDealer.checkPath import check
from crawl.spiderDealer.fileDownload import download
import re

from readBook.PicResult import PicResult

urls_list = [
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181366776353804399/croakie_black_woman_afro_portrait_cartoon__gel_plate_Lithograph_4c9ee6a3-41bd-47ce-9974-2ae9ec4dc0fb.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181108336666619944/eggon_a_production_still_from_1987_of_a_live-action_Yoshitaka__62c47ec4-54b2-43ce-8556-d6bcde4fd4cb.png?ex=657fdbdb&is=656d66db&hm=964e641959d644d62e12d30ef86a5f655f73437a8862508c14371d6144cf4cb4&',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181114698293313588/eggon_a_still_from_a_1987_Yoshitaka_Amano_anime_pirates_approa_1b3e75d4-2022-46c0-b957-1d5b659116b4.png?ex=657fe1c8&is=656d6cc8&hm=95ce0b84ff100d10541018bc89a19d6b43e92ecc884560412cf89f2c0057c0cd&',
    'https://cdn.discordapp.com/attachments/1038329663187062804/1181384573897158656/Geisha_3.png?ex=6580dd1f&is=656e681f&hm=f451a0d1875cb69a9335eec0afb5f50ae4f800d02c061168131b68eb95acda3f&',
    'https://cdn.discordapp.com/attachments/1008049088324972657/1179093412490784890/CARD49_Process-GIF.gif?ex=65788750&is=65661250&hm=1c6917e5578620820e9a504d2e8ab8aa8b96f27f148a4be021241e48e7f1cca2&',
    'https://cdn.discordapp.com/attachments/1008049088324972657/1180927252389703800/grnkrby_A_mechanical_assistant_jellyfish_its_tendrils_providing_004d21f8-9fff-4d31-a80f-58b5aa80439b.png?ex=657f3335&is=656cbe35&hm=140083e6e0f785f490df01f0b01cca6c719cd15a917b1ef98edda227414f21a1&',
    'https://cdn.discordapp.com/attachments/1008049109338443829/1180696531746181250/6C63B755-C291-4650-9EAD-F1FE101F3B04.jpg?ex=657e5c55&is=656be755&hm=64394b7e161f9fdad2e26ae5d619c4113a0dbb597762a8afff996a5f9dec7b68&',
    'https://cdn.discordapp.com/attachments/1008049109338443829/1180696533914619959/0446D7AB-5488-44B0-8E73-6B910227C4D1.jpg?ex=657e5c55&is=656be755&hm=0ea0fc0ee6fca5256ae3033ff5b4e4edf71a897de3c1d91cdb7d17c47e236933&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181436253292466397/croakie_catgirl_bubble__gel_plate_Lithograph_monochrome_pink_an_27dd7d43-ba1c-42c6-8f14-f9f8fcaa5712.png?ex=65810d40&is=656e9840&hm=d9caa358b79ab2e06288cd930c1c8bd8c9daa7599df8d01b5ad3024ee1f4e0c4&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181436252738813952/croakie_catgirl_bubble__gel_plate_Lithograph_monochrome_pink_an_601a9f27-afae-4e37-9adf-acadfcd19714.png?ex=65810d40&is=656e9840&hm=952b0b07231a36bec297e2b6095c844a9f06b9b0203c13a39c0b76d8ef941deb&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181436252248092733/croakie_catgirl_bubble_letters__gel_plate_Lithograph_monochrome_555a97b8-e9ba-4e1d-b3f9-ab6358fb0733.png?ex=65810d40&is=656e9840&hm=9eafc5c87dd2a0c7b056431803cd50977c33b9a70700b2cf1a8a2bf024673a8b&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181436251757350962/croakie_catgirl_bubble_letters__gel_plate_Lithograph_monochrome_1c06aed0-0302-411e-8765-8eeb6c1f799e.png?ex=65810d40&is=656e9840&hm=c4ef1a4b5543ee337107d1d2e33ad3b4cc63cbfa3d17331eb5289d80d8da14a5&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181436251140796446/croakie_catgirl_bubble_letters__gel_plate_Lithograph_monochrome_21c040a1-f6b2-444e-ac7b-d078c1061fae.png?ex=65810d40&is=656e9840&hm=9db7020eb18a32cda57f8c74d8e9ff25fb53f9333a99b3cad9b9967606215102&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181457006238892062/kittenhugs_detailed_Digital_Painting_inspired_by_anime_and_Leag_5c820721-7e76-48a5-9cae-9013af27816e.png?ex=65812094&is=656eab94&hm=781687a23d77f768012ecab780e07c3d50f2814d0f2f180d7a41a96d316f6e8c&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181457850028003458/kittenhugs_detailed_Digital_Painting_inspired_by_anime_and_Leag_948fde7a-e8f6-4634-a932-b47ba1d8467b.png?ex=6581215d&is=656eac5d&hm=fb53155fc8d5bc2d51e238d66f5b24e9da3fb6c43fc171872fb867b90c87a109&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181458520059695167/kittenhugs_detailed_Digital_Painting_inspired_by_anime_and_Leag_62549bac-f99a-45b1-8253-1918fae0f33d.png?ex=658121fd&is=656eacfd&hm=70a66a52d45d2f93c6bfcd4bcd3fb5c32b485dc7ded33a65ae423ebefe5041a6&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181458520495898685/kittenhugs_None_170dffdc-0312-43bf-9da1-b5db44a171d6.png?ex=658121fd&is=656eacfd&hm=b4a783df8cf3a50d45de341f21d66fb81fdd07bd7c496bc63daf541156b56e57&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181459730422575194/kittenhugs_a_man_in_black_and_pink_with_a_sword_in_the_style_of_48d0dfa0-1d70-4d50-832a-2a5cb2f877f9.png?ex=6581231e&is=656eae1e&hm=8e4b77261babc4c2c594c6d793f6887f8e1d74577932cc45e92398b6760ef7ae&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181459730917511208/kittenhugs_a_man_in_black_and_pink_with_a_sword_in_the_style_of_6f909015-7b9e-4f39-bd97-4ecd708d1a37.png?ex=6581231e&is=656eae1e&hm=26dba5551d787448701207eac2885793b9c9b789fab4a1988bed219927782de3&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181459731412430878/kittenhugs_a_man_in_black_and_pink_with_a_sword_in_the_style_of_ab50ab7f-b1c2-43b7-99c9-566e8242e918.png?ex=6581231e&is=656eae1e&hm=20e32624eacde1d9d0718e0ebfc2807c2f5f30e599bc2998ae90e33e74333519&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181460053841170492/eklektos_shadows_across_glowing_eyes_mysterious_aesthetic_flash_598e2c85-f43e-408f-a05f-8283c318fbfd.png?ex=6581236b&is=656eae6b&hm=16672ef93cd9f4dd9fbf2938ebfd663efc79ff0cf58d303c3d6f0eb5164b866b&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181470339390263306/fudgyvmp_handsome_long_haired_French_man_dark_blond_ponytail_sv_8acb1277-1173-44bb-9c70-dc9c07f6532d.png?ex=65812cff&is=656eb7ff&hm=3b5535df819a2756d121b463c40c0180020ba1d699a054d8648adbc73d4e33e3&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181470339918725160/fudgyvmp_handsome_long_haired_French_man_dark_blond_ponytail_sv_97a7f643-f20c-4943-b9e7-ec450b8dfce7.png?ex=65812cff&is=656eb7ff&hm=9930872b80ddc4c6f222f381453ac297d4791d7a8ae9e69105a601a7f3467efe&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181519729622523914/scarletbobjoe_the_character_is_flying_and_there_are_star_atop_i_3c425fde-5886-47a4-80cc-526d97a21fd7-3.png?ex=65815aff&is=656ee5ff&hm=74a1dd1c232d7a375a0b02e715b2156d52d6572e89996112df2e5add8444fd6c&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181519703571697694/scarletbobjoe_dark_red_pony_with_subtle_dark_purple_markings_wa_aa166ca6-3493-4e33-a273-44d335599ced.png?ex=65815af8&is=656ee5f8&hm=b0844356bd1c1f611053bca968d7d27f7a9a5d237dfe51691c9d45fea9faa33f&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181480772973101137/stepbro0693_death_knight_battles_dragon_undead_magic_5ed91a84-18a3-4e78-b623-48f1fdaa0ae1.png?ex=658136b7&is=656ec1b7&hm=25b34f2bca9453de468860f94c2153183417b9fab64f0c641fe08c0c6472c3a6&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181435420471463946/image.png?ex=65810c7a&is=656e977a&hm=cb3a01b7f50889c71b2d4b56bd14d9f2f17e5d69cfba20e6ca732c5b66b040aa&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181394899539591208/vortexphantom_female_wood_elf_perfect_body_shes_sticking_her_to_8fcad485-10f3-4355-9182-6906ceb43345.png?ex=6580e6bd&is=656e71bd&hm=10d6e006283065c350a30c29e0e2f6a19a8368eed9e286a87c0950c68a6f6c19&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181394898784632872/vortexphantom_female_wood_elf_perfect_body_shes_sticking_her_to_c4e135ad-0162-4e16-ac60-c5ba16e07504.png?ex=6580e6bd&is=656e71bd&hm=5f351c8177be51839a5593d6a250550125cc05b8f71ab958d808aeba30fa5b1a&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181370472705830933/0_1.png?ex=6580cffd&is=656e5afd&hm=8e315d6ed77d65d535d8332bf315b9e8e4fa63e5ef057e613c23f8418b78703e&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353472680009849/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_161b488c-00b5-407f-a690-d32b4101fefe.png?ex=6580c028&is=656e4b28&hm=226f64bfd605903ee5af4cd28894b127005add56405023782d83b5fbd4b5d99d&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473762148363/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png?ex=6580c028&is=656e4b28&hm=d56d745b0b31e781235b9488a5d65bd1cc67dcac84ea06884eb7bc2ca6f1eb17&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353474248679587/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__6a417923-6ee3-4775-87a5-5027bd49110c.png?ex=6580c028&is=656e4b28&hm=87d7d5a6f60506db97725ef030f6ad43be87f787f9e7afa57aafa150b02c152f&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353474739417168/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite._9a0cea48-989b-42d0-87f9-9aa380859a25.png?ex=6580c028&is=656e4b28&hm=a8eaa557a166f8658e7f2033745ce96fe1e47dccd25c4d6a6cba627d1158f7a9&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353475192406089/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite._b6480c04-a39b-481b-9071-1aca86e66d3d.png?ex=6580c028&is=656e4b28&hm=e339b84d97b03cbfdc70e29e88e80da76dfaee31542bb47c8b8e678fbe00f38c&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353479848083526/stevenbills_silky._Following._Smoke._Gloomy._Horror_4890c6af-e6d9-479a-9eae-8fbb0a176caa.png?ex=6580c02a&is=656e4b2a&hm=c61bcd5367388cf33752813ba0740a9ef4dd0ab4d5940c5e8ce41dd8b93a181c&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181342115570131004/image.png?ex=6580b594&is=656e4094&hm=1c773417cc703d3141152b656446e29b1cad5cf6abf5abfd0a4beef458c11acb&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181796931173888060/scarletbobjoe_the_unicorn_in_purple_wears_the_floral_decoration_c7392af6-576e-4f6e-bce9-e9d2360fe45f.png?ex=65825d29&is=656fe829&hm=280e3bd1bdfb8d2da02bd5d573ea6c9744019bb024bd8aee086f21a031dae496&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181798754043564123/scarletbobjoe_an_adorable_unicorn_horse_with_long_brown_hair_in_8436cafb-cbcf-4094-88b7-2f815ba1620b.png?ex=65825edb&is=656fe9db&hm=ce9aafecc5acb376fc6e091d4b4a8d5f855211da260183d591b58fe4d5975928&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181798769151455322/scarletbobjoe_the_unicorn_has_light_blue_hair_and_white_flowers_71abd865-4f65-44f9-86df-045cafb0300d.png?ex=65825edf&is=656fe9df&hm=38da6b4fd51567ffd8c1cca7d2deb20863ceb1c0f44136d42901bec25f380c09&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181798948403433633/scarletbobjoe_Subtlety_coloured_pony__full_body_stars_sparkles__38b3208e-45ef-4e29-ad57-78cc5a515f9c.png?ex=65825f0a&is=656fea0a&hm=f0043c004396b2c46b258b8bcbf3ce4e87ac63cdfacdc9beb2e2aadf96751521&',
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
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    ''

]


def getRedBookPic2(urls_list, path=None):
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
            pattern1 = r"/([\w.-]+)\.[a-z]{3}\?"
            match = re.search(pattern1, url)
            if match:
                match_ext = re.search(r'\.(gif|png|jpg)\?', url)
                if match_ext:
                    file_ext_1 = match_ext.group(1)
                    filename = match.group(1) + "." + file_ext_1
                else:
                    print("后缀未匹配到！")
                    if (len(err_list) > 0):
                        print("未下载的图片链接：")
                        print(err_list)
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


def getRedBookPic(url):
    proxy_host = '127.0.0.1'
    proxy_port = 10809
    proxies = {
        'http': f'http://{proxy_host}:{proxy_port}',
        'https': f'http://{proxy_host}:{proxy_port}'
    }
    path = '../crawl/files/redbook/original_pic'
    check(path)
    picResult = PicResult()

    if url is not None and len(url) > 0:
        # 使用正则表达式提取文件名
        pattern1 = r"/([\w.-]+)\.[a-z]{3}\?"
        match = re.search(pattern1, url)
        if match:
            match_ext = re.search(r'\.(gif|png|jpg)\?', url)
            if match_ext:
                file_ext_1 = match_ext.group(1)
                filename = match.group(1) + "." + file_ext_1

                pattern2 = r'\?.*'
                clean_url = re.sub(pattern2, '', url)
                filePath = download(fileUrl=clean_url, name=filename, path=path, proxies=proxies)
                picResult.url = clean_url
                picResult.name = filename
                picResult.ext = file_ext_1
                picResult.downpath = filePath
                picResult.describe = "SUC"
                return picResult
            else:
                # print("后缀未匹配到！未下载的图片链接：")
                # print(url)
                picResult.url = url
                picResult.describe = "ERR:EXT"
                return picResult
        else:
            # print("未找到匹配的文件名！")
            picResult.url = url
            picResult.describe = "ERR:URL"
            return picResult
    else:
        picResult.describe = "ERR:NULL URL"
        return picResult


if __name__ == '__main__':
    picResult = getRedBookPic(urls_list[1])
    print(picResult)
