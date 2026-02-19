
label p1_ch6:
    stop music fadeout 0.5
    $ display_chapter("第六章", "████████████████████", time=3.0)
    centered "{color=#ffffff}{size=40}......{w}\n\n我看见一缕黄金，自高天坠落。 {w}\n\n哪怕只是微不足道的一线，也足以证明——神明亦会流血。{/color}{/size}"
    centered "{color=#ffffff}{size=40}终于，伴随我亿万年的痛楚...{w}\n\n灼烧着我、温暖着我的温度，正如潮水般退去。{w}\n\n喧嚣止息，只余下......一片澄澈的空明。{/color}{/size}"
    centered "{color=#ffffff}{size=40}是啊，我从不为寻求救赎而燃烧。{w}\n\n漫长的跋涉与痛苦本身，即是我生命的全部。{w}\n\n纵使注定在徒劳中陨落，我已将凡人的愤怒，刻入寰宇。{w}\n\n——向命运挥剑的瞬间，我确信自己是幸福的。{/color}{/size}"
    play music "music/Emotions.mp3" fadein 4.0 fadeout 1.0
    pause 3.0

    scene bg Okhema_citygate_day with Fade(1.0, 2.0, 2.0)
    show Trinnon normal at right
    show Phainon normal at left
    with dissolve
    Phainon "......缇宁老师，这就是全部的计划。" id _106_20000
    Trinnon "小白......你变得越来越像阿雅了。" id _106_20001
    show Phainon eyeclosed with dissolve
    Phainon "在最后的时刻，逐火之旅需要的，不再是只会冲锋的战士。" id _106_20002
    show Phainon sad with dissolve
    Phainon "......我决不能辜负她的嘱托。" id _106_20003
    Trinnon "*我们*能感觉到你的不舍。你的心里，在下雨。" id _106_20004
    Phainon "......" id _106_20005
    Trinnon "好吧。如果是小白的愿望的话...." id _106_20006
    Trinnon "我们会在城外大道开启百界门，送[user_name]离开。" id _106_20007
    Trinnon "但是...你真的想好了吗？一旦门关上，就再也回不来了。" id _106_20008
    show Phainon eyeclosed with dissolve
    Phainon "......我不知道。" id _106_20009
    show Phainon normal with dissolve
    Phainon "如果这个世界存在奇迹，那大概不是创世涡心星空背后的秘密......而是搭档自天边降临的一瞬。" id _106_20010
    show Phainon sad with dissolve
    Phainon "这一路走来，我看过太多的牺牲，也听过太多的谎言。" id _106_20011
    Phainon "我已经明白，未来不可能是一片沐浴在西风中的理想乡，静候着我们踏入其中。" id _106_20012
    Phainon "缇宁老师，假如......我们的明天不在「再创世」，而在天外之界......" id _106_20013
    Phainon "假如凭我独自一人，无法承载再创世的职责......" id _106_20014
    Phainon "即便我有无数个理由说服自己这是为了大局......但我依然不知道，擅自决定[user_name]的去留，是不是正确的选择。" id _106_20015
    Phainon "但......" id _106_20016
    show Phainon normal with dissolve
    Phainon "我绝不能令[user_name]以身犯险。" id _106_20018
    Trinnon "小白......纵使犹豫，你心中已经有答案了，对吗？" id _106_20019
    Phainon "......没错，缇宁老师。" id _106_20020
    Phainon "我请求您，打开自奥赫玛到天外载具所在地的百界门，让他们能够安然无恙地离开。" id _106_20021
    Trinnon "小白......" id _106_20022
    Trinnon "我知道，你还有很多话想对[user_name]说。" id _106_20023
    Trinnon "但是，如果[user_name]知道了真相......绝不会同意你独自留下来。" id _106_20024
    Trinnon "所以，那些话，你一直留在心里。" id _106_20025
    show Phainon lookaway with dissolve
    Phainon "真是......什么都瞒不过缇宁老师。" id _106_20026
    Trinnon "既然不能当面说出口，那么，小白..." id _106_20027
    Trinnon "写一封信吧。" id _106_20028
    show cg p1_ch6_Phainon_letter with Fade(1.0,1.0,2.0)
    Phainon "（哪怕，这封信或许永远不会寄出。）" id _106_20030
    "青年从抽屉的最底层拿出一张泛黄的信纸。" id _106_20032
    "那是青年从古玩市场淘来的，据说是旧时代的诗人留下的存货。" id _106_20033
    "他幻想过，等到一切尘埃落定，等到世界不再需要英雄和救世主......" id _106_20034
    "他要用这张纸，写一封信。" id _106_20035
    "也许是给未来的自己，也许是给一同逐火的战友。" id _106_20036
    "但青年没能想到，这张纸最后的归宿——{w}竟是一封诀别书。" id _106_20037
    "......" id _106_20038
    "笔尖悬在纸面上许久，墨水差点滴落下来。" id _106_20039



    Phainon "明明已经下了决断了，可真正落笔的时候，我又这样踌躇......" id _106_20043
    Phainon "与你道别......果然还是太过困难了啊。" id _106_20044

    Phainon "还记得么，搭档？在重渊初遇的时候，我还以为你们是从天而降的、艾格勒的爪牙，是阻碍逐火的敌人。" id _106_20046
    Phainon "那时的我可没想到，被我视为威胁的人，后来会成为我独一无二的搭档。" id _106_20047
    Phainon "后来，我们斩落纷争，取回岁月，见证理性与死亡，一起走过波澜壮阔的旅途。" id _106_20048
    Phainon "不知从什么时候开始，我习惯了回头就能看到你在身后；" id _106_20049
    Phainon "习惯了与你并肩作战，习惯了在篝火旁听你讲天外的故事。" id _106_20050
    Phainon "而现在，逐火的旅途，就要走到终点了。" id _106_20051
    Phainon "神谕总是残酷的，它总是高高在上地索取代价，从不问凡人是否支付得起。" id _106_20052
    Phainon "「再创世」的预言含混不清，对于来自翁法罗斯之外的你们，它的影响无法预估。" id _106_20053
    Phainon "在除却了犹疑之后，这是我发自心底认定的，正确的选择。" id _106_20054
    Phainon "若来世如期而至，不管我会变成哪般模样——我都一定会让世界记住「开拓」的名讳。" id _106_20055
    Phainon "如果真的有奇迹，或许在很久很久以后的某一天，我们终将重逢。" id _106_20056
    Phainon "那时候，你我都只是普通的旅人。" id _106_20057
    Phainon "我们可以坐下来，喝一杯酒，聊聊那些没有做完的梦。" id _106_20058
    "就此搁笔吧，青年想。" id _106_20059
    Phainon "......" id _106_20061

    play sound "sfx/clock.mp3" fadein 6.0
    Phainon "但，我是说万一。要是你不爽我单方面的决定和安排，想靠自己开辟一条崭新的道路、一个无人设想过的未来——" id _106_20063
    Phainon "——你总能找到打破规则的办法，对么？" id _106_20064

    $ ui_hidden = True
    pause 0.5
    stop music fadeout 5.0
    pause 2.0
    play sound "sfx/duang.mp3" volume 2.0
    pause 5.0

    show burn

    pause 3.8
    scene black with Fade(0.0,1.0,2.0)
    pause 2.0
    $ ui_hidden = False
    play music "music/you and me beta.mp3" fadein 2.0 fadeout 1.0
    pause 5.0

    play sound "sfx/book_fall.mp3" volume 0.5
    pause 0.5


    Castorice "啊——！非常抱歉！" id _106_20084
    Castorice "您还好吗？需要我去请风堇小姐过来看看吗，白厄阁下？" id _106_20085
    show cg p1_ch6_Phainon_Castorice_eyeclosed with Dissolve(1.0)
    Phainon "不用麻烦。真要说的话，能被知识“醍醐灌顶”，或许也是种幸运。" id _106_20086
    Phainon "遐蝶小姐......是在找那刻夏老师课上提到的资料吗？我来帮把手吧。" id _106_20087
    Castorice "感激不尽。关于古代灵魂学的厚重书籍，总是被放在让人够不到的地方......" id _106_20088
    Castorice "明明是那样轻盈的东西，承载它的文字却总是这般沉重。" id _106_20089
    Castorice "即使在满是学者的树庭里，也不是所有人都愿意去触碰“灵魂”这种虚无缥缈的课题。" id _106_20090
    Phainon "......毕竟您曾是哀地里亚的“女儿”。" id _106_20091
    Castorice "过去塑造了现在的我，白厄阁下。我并不避讳它。" id _106_20092
    Castorice "正如树木扎根于腐土中，我也总是能在关于死亡的解读里，找到让生者前行的力量。" id _106_20093
    Phainon "令生者前行么......" id _106_20094
    Phainon "遐蝶，你知道吗？我最近翻到了一些很有趣的记载。" id _106_20095
    show cg p1_ch6_Phainon_Castorice_smile with Dissolve(1.0)
    Phainon "在某些城邦里，人们曾供奉过一种奇特的若虫。" id _106_20096
    Phainon "它们在地底沉睡了整整十七年，只为了换取一个夏天的光明。" id _106_20097
    Phainon "若虫破土而出，在短短几十天里脱壳、振翅、鸣叫，仿佛要把积攒了十几年的生命全部燃烧殆尽。" id _106_20098
    Phainon "然后，在第一片秋叶落下之前，在第一缕凉风吹过之前......它们就会死去。" id _106_20099
    Phainon "书中说：“夏虫不可语冰。”" id _106_20100
    Phainon "那里的人用这句话，来描述人在浩瀚时间面前的无力。" id _106_20101
    Phainon "它们拼尽全力地活着、歌唱，却至死都无法理解什么是“冬天”，无法想象这世上的雪。" id _106_20102
    Phainon "对于它们来说，世界只有炎热和喧嚣。" id _106_20103
    Phainon "寂静、洁白的终局，是它们无论如何努力振翅、如何声嘶力竭地呼喊，都无法抵达的彼岸。" id _106_20104
    Phainon "我每次读到这里，总觉得......有一种说不出的感觉。" id _106_20105
    Castorice "确实......是一段极具悲剧美感的描述。" id _106_20106
    Castorice "但是，白厄阁下。我有一些不太成熟的想法。" id _106_20107
    Castorice "在夏天死去的若虫，确实从未见过雪花。" id _106_20108
    Castorice "它的眼睛里只有烈日，它的听觉里只有雷雨。在客观事实上，它的世界是残缺的。" id _106_20109
    Castorice "可是，倘若在它于地底沉睡的那十七年里，在它于枝头高歌的那几十个日夜里......它曾经无数次地幻想过一种“洁白”呢？" id _106_20110
    Castorice "它或许不知道它的名字叫“雪”。" id _106_20111
    Castorice "但它想象过有一种凉爽而温柔的东西，会在它离开后降临这片大地。" id _106_20112
    Castorice "那份“想象”，在那一刻，对于它而言就是真实的。" id _106_20113
    Castorice "正如我们。" id _106_20114
    Castorice "或许我们终其一生都在追求名为“理想乡”的明天......" id _106_20115
    Castorice "哪怕直到倒下的那一刻，眼前的黑潮仍未退去，天空依然是灰暗的......" id _106_20116
    Castorice "但这并不意味着，我们的高歌是徒劳的。" id _106_20117
    Castorice "那些与看似与此刻无缘的美好，恰恰是因为我们现在的燃烧，才有了降临的可能。" id _106_20118
    Castorice "其名为——希望。" id _106_20119
    Phainon "......" id _106_20120
    show cg p1_ch6_Phainon_Castorice_eyeclosed with Dissolve(1.0)
    Phainon "......真是精彩的辩论啊，遐蝶小姐。" id _106_20121
    Phainon "如果下次树庭的思辨会上遇到你作为对手，我恐怕只能投降了。" id _106_20122
    Castorice "您的蝉联冠军记录，也要一起拱手让人吗？" id _106_20123
    Phainon "哈哈......开玩笑的，遐蝶小姐。就算是你，我也不会放水的。" id _106_20124
    Castorice "那么...这个答案，能稍微填补您心中的空洞吗？" id _106_20125
    Castorice "您刚才想问的，其实并不是若虫。而是您自己，对吗？" id _106_20126
    show cg p1_ch6_Phainon_Castorice with Dissolve(1.0)
    Phainon "......" id _106_20127
    Castorice "作为被选中的“黄金裔”，那些看似遥不可及、甚至可能注定无法实现的愿望......" id _106_20128
    Castorice "对您来说，究竟是什么？" id _106_20129
    Phainon "......大概是......" id _106_20130
    Phainon "我必须背负的责任。" id _106_20131
    Phainon "哪怕我是若虫，我也要在我还能发声的每一秒，嘶吼着歌唱。" id _106_20132
    Phainon "哪怕我看不到，为了让后来者能看到那场雪......" id _106_20133
    Phainon "我甘愿......付出一切。" id _106_20134
    show cg p1_ch6_Phainon_Castorice_smile with Dissolve(1.0)
    Phainon "这听起来...是不是有些自大？" id _106_20135
    Castorice "不......我很庆幸，白厄阁下。" id _106_20136
    Castorice "我很庆幸......背负“救世主”这一沉重名讳的人，是你。" id _106_20137
    Castorice "不必妄自菲薄，阁下。" id _106_20138
    Castorice "命运的书籍，也许注脚残酷且沉重，也许空白处填满的尽是叹息。然而......" id _106_20139
    Castorice "若真有那么一日，我们的愿望都在半途折戟。" id _106_20140
    play sound "sfx/clock.mp3" fadein 6.0
    Castorice "我也依然相信，甘愿为残破的世界燃尽自我的你——" id _106_20141
    Castorice "就是拯救了一切的那个人。" id _106_20142

    $ ui_hidden = True
    pause 0.5
    stop music fadeout 5.0
    pause 2.0
    play sound "sfx/duang.mp3" volume 2.0
    pause 5.0

    show burn

    pause 3.8
    scene black with Fade(0.0,1.0,2.0)
    pause 2.0
    $ ui_hidden = False

    play music "music/Her Wishes.mp3" fadein 1.0 fadeout 1.0
    pause 3.0
    show cg p1_ch6_Phainon_Aglaea with Dissolve(1.0)
    Aglaea "白厄。" id _106_10000

    Phainon "......" id _106_10001
    Aglaea "......又是一夜未眠么。" id _106_10002
    Phainon "......" id _106_10003
    Phainon "...太......亮了。" id _106_10004
    Phainon "仿佛...天空...烧起来......" id _106_10005
    Aglaea "......" id _106_10006
    Aglaea "白厄，我不知道那片名为「哀丽秘榭」的土地，究竟遗落在何方......" id _106_10007
    Aglaea "但我能从你破碎的梦呓里，从你不敢阖上的眼睛中，窥见它的模样。" id _106_10008
    Aglaea "那一定是一片被神明亲吻过的土地。" id _106_10009
    Aglaea "是你曾拥有，却被夺走的一切。" id _106_10010
    show cg p1_ch6_Phainon_Aglaea_eyeclosed with Dissolve(1.0)
    Phainon "......" id _106_10011
    Aglaea "即便有些僭越...但我仍心怀此愿——" id _106_10012
    Aglaea "我希望，你能允准奥赫玛成为你的第二片故土。" id _106_10013
    Aglaea "这里或许闻不到熟悉的麦香，也没有洗濯哀愁的溪流..." id _106_10014
    Aglaea "但我将尽己所能，令你衣食无忧，令你安睡无虞。" id _106_10015
    Aglaea "孩子，我希望...你流血的脚能停下来，不再于荒芜的大地上，无依地漂游。" id _106_10016
    Phainon "......" id _106_10017
    Phainon "......不。" id _106_10018
    Phainon "我要...向「他」复仇。" id _106_10019
    Phainon "他们在...绝望中死去......被我..." id _106_10020
    Phainon "满手鲜血的人...没有资格...享受奢侈的饱暖。" id _106_10021
    Aglaea "......" id _106_10022
    Aglaea "在绝望中行进...这就是你为自己选定的唯一使命么？" id _106_10023
    Phainon "......" id _106_10024
    Aglaea "但，孩子，倘若我告诉你......命运比你想象的更残酷，也更仁慈。" id _106_10025
    Aglaea "另一种使命，已然落在你稚嫩的肩膀。" id _106_10026
    Aglaea "倘若，你的剑除了复仇，还可以为了守护而战。" id _106_10027
    Aglaea "——你愿意接受神谕，成为预言中的「救世主」吗？" id _106_10028
    Phainon "......救世......主？" id _106_10029
    Aglaea "刻法勒的神谕揭示了你的到来。" id _106_10030
    Aglaea "只有你能够完成预言中的再创世，令生者与逝者在没有黑潮的新世界复生。" id _106_10031
    Phainon "......" id _106_10032
    Aglaea "......白厄。" id _106_10033
    Aglaea "我多么希望，你能够作为普通人活下去。" id _106_10034
    Aglaea "我愿意庇护你长大，送你去神悟树庭求学。" id _106_10035
    Aglaea "去研读诗歌与真理，去体验一个普通少年理应享受的一切斑斓色彩。" id _106_10036
    Aglaea "或许，在某个午后，你将重拾遗落在灰烬中的欢笑。" id _106_10037
    Aglaea "尽管我无缘亲眼得见那副光景，但我知道......" id _106_10038
    Aglaea "当你真正展颜时...一定会如初春的阳光般美好。" id _106_10039
    Phainon "......" id _106_10040
    Aglaea "但...世界终究是残酷的。它将守护的命运强行交付于我，也将它...蛮横地交付与你。" id _106_10041
    Aglaea "倘若奥赫玛需要你......" id _106_10042
    Aglaea "倘若圣城之外，在黑夜中颤抖的人们...都在呼唤你。" id _106_10043
    play sound "sfx/clock.mp3" fadein 6.0
    Aglaea "「哀丽密榭」的白厄。" id _106_10044
    Aglaea "你愿意，与我一同踏上逐火之旅吗？" id _106_10045


    $ ui_hidden = True
    pause 0.5
    stop music fadeout 5.0
    pause 2.0
    play sound "sfx/duang.mp3" volume 2.0
    pause 5.0

    show burn

    pause 3.8
    scene black with Fade(0.0,1.0,2.0)
    pause 2.0
    $ ui_hidden = False

    scene black with fade
    play music "music/Tales From the Snow Mountain.mp3" fadein 1.0 fadeout 1.0
    pause 4.0
    show cg p1_ch6_fieldPhainon with Dissolve(1.0)

    Cyrene "玩累了吗？" id _106_10047

    show cg p1_ch6_fieldPhainon_smile with Dissolve(1.0)
    Phainonyoung "稍微...有一点。不过很开心！" id _106_10048
    Cyrene "那就在这里休息一会儿吧。草地软绵绵的，躺下去，就像陷进云朵里一样。" id _106_10049
    Phainonyoung "呼......" id _106_10050
    Phainonyoung "看着天空，突然觉得哀丽秘榭好大，又好小。" id _106_10051
    Phainonyoung "那些云从来都不停留，不知道它们是从哪里飘来的，又要飘到哪去......" id _106_10052
    Cyrene "你在向往外面的世界吗？" id _106_10053
    Phainonyoung "向往...但也舍不得。" id _106_10054
    Phainonyoung "哀丽密榭的每一个角落，每一块石头，好像都认识我。" id _106_10055
    Phainonyoung "它们看着我从一个小不点，变成现在这样，能拿起老爸的锄头和小木剑。" id _106_10056
    Phainonyoung "不过，皮西厄斯老师说过......" id _106_10057
    Phainonyoung "等我们长大了，我们一定会走出哀丽密榭，到外面看看，对吧？" id _106_10058
    Cyrene "白厄。" id _106_10059
    Phainonyoung "怎么啦，昔涟？" id _106_10060
    Cyrene "如果有一天，你能去到圣城，甚至更远的地方......" id _106_10061
    Cyrene "你会许下什么样的愿望呢？" id _106_10062
    Phainonyoung "愿望？" id _106_10063
    Cyrene "是啊。像故事里的英雄那样，得到了神明的奖赏，可以实现一个心愿。" id _106_10064
    Cyrene "是想要永远吃不完的蜂蜜烙饼？还是想要一把独一无二的宝剑？" id _106_10065
    Phainonyoung "唔......烙饼虽然好吃，但天天吃也会腻吧。" id _106_10066
    Phainonyoung "宝剑嘛......倒是挺酷的。有了它，我就能打败所有的坏人，保护村子了！" id _106_10067
    Cyrene "只是这样吗？" id _106_10068
    Cyrene "如果是“任何”愿望都可以呢？" id _106_10069
    Phainonyoung "任何愿望......？" id _106_10070
    Phainonyoung "可是，昔涟......" id _106_10071
    Phainonyoung "有你们在身边，有烙饼吃，累了还能躲进麦田里，枕着风睡一个好觉......" id _106_10072
    Phainonyoung "好像......已经没什么特别想要的了。" id _106_10073
    Cyrene "傻瓜......这叫什么愿望呀。" id _106_10074
    Cyrene "这分明就是现在呀。" id _106_10075
    show cg p1_ch6_fieldPhainon_smile_eyeclosed with Dissolve(1.0)
    Phainonyoung "嘿嘿，因为我很幸福嘛。" id _106_10076
    Cyrene "嗯......但英雄可不能只看着眼前的安逸哦。" id _106_10077
    Cyrene "真正的英雄，心里装着的是更远大的东西。" id _106_10078
    show cg p1_ch6_fieldPhainon with Dissolve(1.0)
    Phainonyoung "更远大的东西......" id _106_10079
    Phainonyoung "那样的事......我也能做到吗？" id _106_10080
    Cyrene "当然，只要你愿意。" id _106_10081
    Cyrene "只要你还没忘记，麦田的清香，风的触感......" id _106_10082
    Cyrene "只要记住了这些微不足道的暖意，记住了你是多么深爱着他们，深爱着这片土地上的每一个生命......" id _106_10083
    Cyrene "那就是你力量的源泉。" id _106_10084
    Phainonyoung "我好像......有点明白了。" id _106_10085
    Phainonyoung "如果是那样的话......" id _106_10086
    Phainonyoung "昔涟，再问我一次吧。" id _106_10087
    Cyrene "嗯？" id _106_10088
    Cyrene "那么，未来的英雄，白厄......" id _106_10089
    Cyrene "如果你能实现一个愿望，你会许下什么呢？" id _106_10090
    Phainonyoung "我的愿望？" id _106_10091
    show cg p1_ch6_fieldPhainon_smile_eyeclosed with Dissolve(1.0)
    Phainonyoung "我的愿望，就是实现大家的愿望！" id _106_10092
    Phainonyoung "如果不能实现......" id _106_10093

    stop music fadeout 1.0
    scene white with fade
    Lygus "那便是一切愤怒的源头。" id _106_10094

    $ play_resumable_video("videos/p1_ch6.webm", fade_time=1.0)


































































    scene black with Fade(2.0, 2.0, 2.0)

    $ play_resumable_video("videos/p1_ed.webm", fade_time=1.0)



    scene black with Fade(3.0,0.5,0.5)

    return
return

