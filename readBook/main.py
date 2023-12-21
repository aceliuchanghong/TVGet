from crawl.spiderDealer.checkPath import check
from readBook.deal_image_urls import deal_image
from readBook.deal_upload import start
import asyncio

from readBook.image_utils import copy_file


def publish_xhs(urls_list, re_run=False):
    for url in urls_list:
        # 尝试打开并读取文件内容
        try:
            with open('uploaded.log', 'r') as file:
                content = file.read()
                file.close()
                # 检查字符串是否在文件内容中
            if url in content:
                print("OK,already uploaded")
            else:
                picResult = deal_image(url=url, re_run=re_run)
                if picResult.describe == "SUC":
                    is_success = asyncio.run(start(picResult, re_run))
                    # is_success = True
                    if is_success:
                        with open('uploaded.log', 'a+') as file:
                            file.seek(0)
                            content = file.read()
                            file.write(f"{url}\n")
                            file.close()
                        words_image_path = "../crawl/files/redbook/pub_send_pics"
                        check(words_image_path)
                        copy_file(source_path=picResult.downpath,
                                  destination_path=words_image_path + "/" + picResult.fix12path + "." + picResult.name,
                                  re_run=re_run)
                        print(words_image_path + "/" + picResult.fix12path + "." + picResult.name)
                    else:
                        print("ERR:上传失败")
                else:
                    print("ERR:文件处理失败")
        except Exception as e:
            print(f"Open file error occurred: {e}")


not_girl = [
    'https://cdn.discordapp.com/attachments/1083132446805073920/1187244052819751013/0_1.png?ex=65962e30&is=6583b930&hm=cdadf206f886741a641b69005bd84116c60d37b1315bac69d91496dc189a0d96&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1176736624311279677/digitaldaydreamdesign_moon_trees_stars_light_blue_light_pink_1_dbc470f7-a030-44ca-9f04-864b05bb78ae.png?ex=6594de61&is=65826961&hm=60b7842a3830d170d1e8e5d89ad8fe69abbcf7e92358da4ba5aa1b08d61daca0&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1176736623711502356/digitaldaydreamdesign_moon_trees_stars_light_blue_light_pink_0_dbc470f7-a030-44ca-9f04-864b05bb78ae.png?ex=6594de61&is=65826961&hm=9776cb17b0e212c263a83401cb6184557856d32b3db05ccd4f4716e8318e3a8e&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1176736624864923689/digitaldaydreamdesign_moon_trees_stars_light_blue_light_pink_2_dbc470f7-a030-44ca-9f04-864b05bb78ae.png?ex=6594de62&is=65826962&hm=05b21f52d73b8d74c827f23c5c33d75637c4074cc0bdfdfeb5b357537d92b247&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1176736625594736791/digitaldaydreamdesign_moon_trees_stars_light_blue_light_pink_3_dbc470f7-a030-44ca-9f04-864b05bb78ae.png?ex=6594de62&is=65826962&hm=2ef6e7e9ed9dfd392e3ec7197569a451e5261a58c69007ad396ec92900b244f9&',
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
]
bak = [
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186747255726805002/0_2.png?ex=65945f82&is=6581ea82&hm=7dcf2acceee2627957c8aaa3b855441b479e87d06b846d5fcf44344fd479bcd7&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186737376219910155/yohanlibertto_In_the_beginning_God_created_the_heavens_and_the__91cc23ac-d329-4648-b401-90914d82ff72.png?ex=6594564f&is=6581e14f&hm=5f70012ae86b1a377db8ff22fb3f03231f8b3edc3d17e23e243abad17337baab&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186737377004224573/yohanlibertto_In_the_beginning_God_created_the_heavens_and_the__dba6b70d-29f5-4450-9786-d96353b32a1a.png?ex=6594564f&is=6581e14f&hm=5295b63f33334d3ff965c742e1a45931daf97ee8d801d0101da45a1928798dee&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186671383875432639/0_2.png?ex=659418d9&is=6581a3d9&hm=3188a1fb4aba02f0e36c2a91c19d1f63436f95ea0192b00231a582d521d7724c&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186636398233653308/kittenhugs_Classic_Disney_art_featuring_a_anthro_female_deep_pu_669a3f29-a379-4515-b39f-dcbd8937ba21.png?ex=6593f843&is=65818343&hm=67574990edd2e94e555f32993cb2971d6331193a92ed3559cf9a82f2607c69b1&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1187128598860140685/razeristaken_Nishizumi_Maho_from_Girls_und_Panzer_German_milita_9474beef-ee4f-4ff0-9ee7-cb5d9f2c0f84.png?ex=6595c2a9&is=65834da9&hm=7aafab50299dae5cf70969b6b4c7d437c928dde69bfd2cf48cc5654f302361c6&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1187174499888664768/Hand_0_6acbe5f6-de21-4a9d-80a7-ea2ed504e0d1.png?ex=6595ed69&is=65837869&hm=e1895b731df257fa28621ef45df255f35f0f5f928eb784b637ad2c311baa81ea&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1187175350267019264/liquidus00_1998s_screencap_by_Shoji_Kawamori_Link_in_his_iconic_86689fa8-c8c8-4a53-b83d-6225ea6fb3d8.png?ex=6595ee34&is=65837934&hm=98958c5d0e84f37c8cd69d43a8ee2a438786b6a755b9dbadc6629aa83a787ef0&',
    'https://cdn.discordapp.com/attachments/1064028865741197413/1187073971930267859/i.p.ishipyards_Envision_a_dungeons_and_dragons_high_elf_female__a08b7410-7d99-44bb-911f-3a212508a27a.png?ex=65958fc9&is=65831ac9&hm=380cc0000a098c6794997b0dd4c434fd85cdba9aeee2afea76d1460f117135f1&',
    'https://cdn.discordapp.com/attachments/1064028865741197413/1187073996873797702/i.p.ishipyards_Envision_a_dungeons_and_dragons_high_elf_female__80717091-7e60-4087-9706-d5504baa6254.png?ex=65958fcf&is=65831acf&hm=de1d2d365620214c0ba7a068847d581b83924f25d6dd16c18548af25b2ea0f18&',
    'https://cdn.discordapp.com/attachments/1064028865741197413/1187074017602060468/i.p.ishipyards_Envision_a_dungeons_and_dragons_high_elf_female__0ef834ca-0223-4459-b7df-54681cb64d6a.png?ex=65958fd4&is=65831ad4&hm=78bef046f719bc4d4bc3591ffd593707c82437c08f8f1a8db4e252c7d8bc636a&',
    'https://cdn.discordapp.com/attachments/1123710007335211078/1181810968938942524/grnkrby_Drama_Anime_opening_a_svelte_Latina_warm_olive_skin_tha_450cacfe-f12c-465c-ad55-7cad69415cbc.png?ex=6594df3b&is=65826a3b&hm=b1c25fe79f32fa5f0bbaf9d71dc0a36e56b1aff989779feeb695d3469588d205&',
    'https://cdn.discordapp.com/attachments/1123710007335211078/1181810969568104468/grnkrby_Drama_Anime_opening_a_Latina_wearing_dress_with_intrica_ff12514f-0966-4dab-a2d2-02d16c1162b8.png?ex=6594df3c&is=65826a3c&hm=abf90ba248271c6726b14960d58ffc281d5eb7cb869a2667f8a95cda430d18b9&',
    'https://cdn.discordapp.com/attachments/1123710007335211078/1181811042532208682/grnkrby_Japanese_Light_Novel_art_flat_colors_a_svelte_Latina_ac_9442e2f9-75ef-471a-bc8b-f258ce0ea5db.png?ex=6594df4d&is=65826a4d&hm=f9dbdb56531ee5c2322a9907d3f5dcd6c67ea77458b459fe217d7b8d348d8192&',
    'https://cdn.discordapp.com/attachments/1123710007335211078/1181811042922274899/grnkrby_Japanese_Light_Novel_art_this_Latina_wearing_a_green_dr_e0f81c1b-5384-41c3-b132-6d2149a3a7f8.png?ex=6594df4d&is=65826a4d&hm=bb479528601157c1e44e8cace405798cf763d03927d0d9f1d8fc47e1bcafe6c6&',
    'https://cdn.discordapp.com/attachments/1125522435257683968/1170478200892166267/grnkrby_Pin-up_poster_of_a_Latina_anime_woman_short_shes_wearin_d00bebf7-34db-4c1e-af26-6166508358f6.png?ex=65908ec5&is=657e19c5&hm=1681e261c90c4f442937598365c0cf036a56bbb1bd873ec367c6a59409f32f18&',
    'https://cdn.discordapp.com/attachments/1125522435257683968/1170478575179268286/grnkrby_Pin-up_poster_of_a_Latina_anime_woman_olive_skin_short__806343b1-546f-4459-9f35-93980560a6b3.png?ex=65908f1e&is=657e1a1e&hm=28fe2a718e8573be4163c4426e4de3f6126643245b842a77b055b07c43aff465&',
    'https://cdn.discordapp.com/attachments/995431274267279440/1187248536362958939/zhenaretofty_Hyukas_style_a_couple_cutechibisweet_full_bodyswee_0bb3a549-13d6-4029-b9a8-0bb5aad08197.png?ex=6596325d&is=6583bd5d&hm=893efaf7bfecab00629d250cb849f70cf4b4822f01bc675aaec41d91a34eaae3&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1187250748988330064/zhenaretofty_Hyukas_style_a_couple_cutechibisweet_full_bodyswee_8b34f5e8-a067-420f-92c5-aec1e3ef6d7e.png?ex=6596346c&is=6583bf6c&hm=feb21369180ad09e2c39446f5853e89377df50f96b4c3b1d09d59c7e048610ca&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1187250749504241734/zhenaretofty_Hyukas_style_a_couple_cutechibisweet_full_bodyswee_8b34f5e8-a067-420f-92c5-aec1e3ef6d7e.png?ex=6596346c&is=6583bf6c&hm=096de7c4326ff8c21e17e00b67b5976675824db560d68e9f09bd9c71598cf767&',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]
urls_list = [
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473258827908/stevenbills_silky._flowing._Smokey._Gloomy._sharp._cenobite._h_a2b8dcc2-9016-4093-a25c-3fb62ce17cd8.png?ex=6580c028&is=656e4b28&hm=5af62b9613c1a769c14fe8d7a2e30850c91f5e24c5bb9e5cb54c64a191f7d303&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480579345125376/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_ad86dcb2-7673-40f0-b750-4336ddab27e4.png?ex=65936725&is=6580f225&hm=9555eed4a42654c8a55113ac0e9a0e52e9d234deab0155df6a717f578ee13deb&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480604624199751/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_b151993c-dec3-46c1-942f-81aa2cba0ca0.png?ex=6593672b&is=6580f22b&hm=684c60175ba522fcf6329592c5a72902a968444b16e50798b7538521f1135218&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480585447854100/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d6d9e024-49b8-41f5-9368-461b08368578.png?ex=65936727&is=6580f227&hm=7c064ca70a170e09c5469f4dfe2a945e273750318df3c88fdabedba868135fc4&',
    'https://cdn.discordapp.com/attachments/941582479117127680/1186480615005098035/lawrence_aceliuchanghong_a_lanky_blonde_with_a_kazoo_in_a_churc_d1722e22-b247-49a9-9929-266a8c3ac3d9.png?ex=6593672e&is=6580f22e&hm=24aac05abf57c3414f220dfce028b314bd3e74c3e2aba79d54f2537ee5bde731&',
    'https://cdn.discordapp.com/attachments/951197655021797436/1181316240761950298/grnkrby_A_technological_computer_screen_coded_in_old_programmin_e5cbf877-dda1-44ff-8caf-db3d88de1f9f.png?ex=657fdb',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1181353473762148363/stevenbills_silky._Following._Smoke._Gloomy._sharp._cenobite.__a4dd1bd1-1b50-4363-b769-4b6d0c4c6684.png?ex=6580c028&is=656e4b28&hm=d56d745b0b31e781235b9488a5d65bd1cc67dcac84ea06884eb7bc2ca6f1eb17&',
    'https://cdn.discordapp.com/attachments/1081612977897226280/1171721620646264852/lawrence_aceliuchanghong_variations_0_ab921d2e-c282-4c80-8a6a-8cd4ce338a20.png?ex=659514cb&is=65829fcb&hm=642795ac60c14ea080adccf54e7320dcbbdb32c0866089847c3afd0ed548ec1f&',
    'https://cdn.discordapp.com/attachments/1083132446805073920/1187227528184725625/0_1_69.webp?ex=65961ecc&is=6583a9cc&hm=d56a9dbb9c69aa582699af93ec299fdf43844f301c7d58e229ef76e07085499a&',
    'https://cdn.discordapp.com/attachments/1054958023698825266/1186753093648535632/intoward_A_Hyperrealistic_beautiful_vampire_girl_made_of_fire_m_582e2bf2-7a02-4ff0-b3fe-6cfa653e0c33.png?ex=659464f2&is=6581eff2&hm=da8463a5c968a995f1c5999a241b70283b523cb1a25510f1dfd479ef6776f69e&',

]

if __name__ == '__main__':
    publish_xhs(urls_list, False)
