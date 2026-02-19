init python:
    renpy.music.register_channel("heartbeat", mixer="sfx", loop=True)



transform check_ui_hidden_and_animate:

    xalign 0.5 yalign 0.96


    parallel:
        linear 1.2 alpha 0.2
        linear 1.2 alpha 0.8
        repeat
    parallel:
        function check_ui_hidden_func
        pause 0.2
        repeat

init python:
    def check_ui_hidden_func(trans, st, at):
        try:
            if getattr(store, "ui_hidden", False):
                trans.alpha = 0.0
        
        
        except:
            pass
        return 0

image ctc_triangle:
    Text("▼", size=30, color="#ffffff")
    xalign 0.5 yalign 0.96
    check_ui_hidden_and_animate



define adv = Character(None,
    ctc="ctc_triangle",
    ctc_position="fixed"
)


define narrator = Character(None,
    ctc="ctc_triangle",
    ctc_position="fixed"
)



default user_name = "开拓者"
default sex = "female"
default reverse_sex = "male"

define Unknown_Khaos = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Khaos", voice_tag="Khaos")
define Khaos = Character('卡厄斯', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Khaos", voice_tag="Khaos")
define Fake_Khaos = Character('卡厄斯（？）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Khaos", voice_tag="Khaos")
define Phainon = Character('白厄', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Phainon", voice_tag="Phainon")
define Phainonyoung = Character('白厄', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Phainonyoung", voice_tag="Phainonyoung")
define Cyrene = Character('昔涟', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Cyrene", voice_tag="Cyrene")



define Cipher = Character('赛飞儿', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Cipher", voice_tag="Cipher")
define Cerydra = Character('刻律德菈', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Cerydra", voice_tag="Cerydra")
define Unknown_Cerydra = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Cerydra", voice_tag="Cerydra")
define Unknown_CerydraBlack = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="CerydraBlack", voice_tag="CerydraBlack")
define Castorice = Character('遐蝶', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Castorice", voice_tag="Castorice")

define Cerydra_shadow = Character('□□□□', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Cerydra", voice_tag="Cerydra")
define CerydraBlack = Character('刻律德菈', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="CerydraBlack", voice_tag="CerydraBlack")

init python:
    style.ruby_text.size = 14
    style.ruby_text.yoffset = -25 


define CerydraBlack_shadow = Character('■■■■', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="CerydraBlack", voice_tag="CerydraBlack")
define CerydraBlack_shadow_destruction = Character('■■■■（毁灭的倒影）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="CerydraBlack", voice_tag="CerydraBlack")
define CerydraBlack_shadow_destruction_cave = Character('{size=-15}                               洞穴{/size}\n■■■■（毁灭的倒影）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", who_yoffset=-20, image="CerydraBlack", voice_tag="CerydraBlack")
define Aglaea = Character('阿格莱雅', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Aglaea", voice_tag="Aglaea")
define Anaxa = Character('那刻夏', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Anaxa", voice_tag="Anaxa")
define FlameReaver = Character('盗火行者', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="FlameReaver", voice_tag="FlameReaver")
define Herta = Character('黑塔', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Herta", voice_tag="Herta")
define Hysilens = Character('海瑟音', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Hysilens", voice_tag="Hysilens")
define Lygus = Character('来古士', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Lygus", voice_tag="Lygus")
define Screwllum = Character('螺丝咕姆', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Screwllum", voice_tag="Screwllum")
define Tribbie = Character('缇宝', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Tribbie", voice_tag="Tribbie")
define Trinnon = Character('缇宁', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Trinnon", voice_tag="Trinnon")
define Tribios_Talanton = Character('缇里西庇俄丝（塔兰顿）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Tribios", voice_tag="Tribios")
define Tribios = Character('缇里西庇俄丝', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Tribios", voice_tag="Tribios")
define Bartholos = Character('巴特鲁斯', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Bartholos", voice_tag="Bartholos")
define Zagreus = Character('扎格列斯', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Bartholos", voice_tag="Zagreus")
define Meme = Character('迷迷', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Meme", voice_tag="Meme")
define EverNight = Character('长夜月', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="EverNight", voice_tag="EverNight")
define Unknown_EverNight = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="EverNight", voice_tag="EverNight")


define Talanton = Character('塔兰顿', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Talanton", voice_tag="Talanton")
define Unknown_Talanton = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Talanton", voice_tag="Talanton")
define Name_Talanton = Character('塔兰顿', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Talanton", voice_tag="Talanton")
define Oronyx = Character('欧洛尼斯', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Oronyx")
define Unknown_Oronyx = Character('？？？（欧洛尼斯）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Oronyx")
define Name_Oronyx = Character('乌拉诺斯（欧洛尼斯）', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Oronyx")

define Regent = Character('摄政王', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Regent", voice_tag="Regent")
define Noble = Character('贵族', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Regent", voice_tag="Regent")

define priest = Character('祭司', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="priest", voice_tag="priest")
define duanfengjue = Character('断锋爵', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="NPC_temp", voice_tag="duanfengjue")
define donglinjue = Character('冬霖爵', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="NPC_temp", voice_tag="donglinjue")
define SeaMonster = Character('海妖', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="SeaMonster", voice_tag="SeaMonster")
define yeshijue = Character('曳石爵', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="NPC_temp", voice_tag="yeshijue")
define yinfengjue = Character('吟风爵', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="NPC_temp", voice_tag="yinfengjue")

define scholar = Character('学者', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="scholar")
define commoner_hopeful = Character('期待的平民', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="commoner_hopeful")
define commoner_doubtful = Character('质疑的平民', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="commoner_doubtful")




define Unknown_Meme = Character('？？？', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="Meme")


define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv, ctc="ctc_triangle", ctc_position="fixed")

define little_girl = Character('小女孩', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="little_girl", voice_tag="")
define merchant = Character('商人', color="#FFD333", ctc="ctc_triangle", ctc_position="fixed", image="merchant", voice_tag="")

