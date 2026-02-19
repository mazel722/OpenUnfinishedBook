label p1_ch2:
    stop music fadeout 0.5
    play music "music/Re Co.mp3" fadein 2.0
    $ display_chapter("第二章", "火光啊，为我等以血加冕", time=3.0)

    scene black with fade
    stop music fadeout 2.0

    "这是......一段刻律德菈的记忆，似乎揭示了她的过往。"
    "要读一读吗......"
    menu:
        "观看记忆":
            pass
        "忽略记忆（跳过chapter 2）":
            scene white with fade
            centered "{size=40}{color=#000000}起初，刻律德菈只是街头的一介乞儿，流着凡人的红血。因发色肖似皇室，她被野心勃勃的贵族收养，包装成“流浪归来的王女”。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n然而，预言中的王储是黄金裔；人们要求刻律德菈展示她的血液。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n出乎意料的是，高台上的“王女”真的流出了金血。{/color}{/size}"
            centered "{size=40}{color=#000000}原来，刻律德菈并非一人，而是一对双生子。站在台前的是健康的凡人，刻律德菈；躲在幕后的是自幼失声的黄金裔，刻律德菈的姊妹。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n在高台上展示金血的，正是那个无声的影子。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n数年后，贵族的摄政令王国日渐衰败，刻律德菈领兵出征。征途中，她与律法泰坦塔兰顿交易，以不再生长为代价，换取了真正的黄金血。{/color}{/size}"
            centered "{size=40}{color=#000000}当她携大军兵临城下，意图夺回权柄时，贵族以囚禁在宫中的哑女为质，企图揭穿“双生子”的秘密。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n为了成全刻律德菈，她在宫中引火自焚。大火吞噬了唯一的破绽。{/color}{/size}"
            extend "{size=40}{color=#000000}\n\n从此，世间再无双子。刻律德菈判处摄政王火刑，在灰烬中加冕为唯一的“凯撒”。{/color}{/size}"
            jump p1_ch3
    pause 4.0
    play music "music/In the Arms of Tomorrow.mp3" fadein 1.0 fadeout 1.0
    scene bg Okhema_citygate_day with fade


    show commoner_hopeful at left
    show commoner_doubtful at right
    with dissolve
    commoner_hopeful "这么多年了......这仗，该到头了。" id _102_0018
    commoner_doubtful "可你说，这王女......真是陛下的血脉？" id _102_0019
    commoner_doubtful "谁都知道陛下没有后嗣，怎么突然就接回来这么一位？" id _102_0020
    commoner_doubtful "我听说，其实就是贵族老爷在路边捡了一个小乞丐，随便糊弄我们的。" id _102_0021
    commoner_doubtful "真是命好啊，能住进皇宫里，怎么就没让我碰上这种好事呢。" id _102_0022

    hide commoner_doubtful

    with dissolve
    show scholar at right with dissolve

    scholar "别再卖弄你们的无知！" id _102_0023
    scholar "昨日，军队从雅努萨波利斯回来，带回了塔兰顿的神谕和圣女的预言。" id _102_0024
    scholar "「许珀耳的血脉仍留存于世，并将在不久之后登上王位。」" id _102_0025

    scholar "《北境先祖书》第三卷有记载，君主的幼妹于战乱初年起便离开了皇室，流落在民间。" id _102_0026
    scholar "若王女殿下是她的后裔，血脉上......并非无据可考。" id _102_0027

    commoner_doubtful "书上的话，能当几个利衡币？关键是血——刻法勒的黄金血！" id _102_0028
    commoner_hopeful "盼着它是真的吧。我老了，经不起又一次战乱了。" id _102_0029
    commoner_hopeful "......那个冬天，我的两个孩子都没能回来。" id _102_0030
    commoner_hopeful "哪怕这王女是从书里变出来的，只要她能让这该死的战争彻结束，我就认她是我的王。" id _102_0031
    commoner_doubtful "所以，我们在等一个孩子给我们带来和平？" id _102_0032

    scholar "......也在等决定未来的血。" id _102_0033
    play sound "sfx//concert_hubbub.mp3" fadein 3.0 volume 0.5
    "平民" "来了！" id _102_0034
    scene black
    stop music

    "群众" "......" id _102_0035
    stop sound fadeout 3.0
    Noble "肃静！" id _102_0036


    play music "music/The City of Progress.mp3" fadein 2.0 fadeout 1.0

    show cg p1_ch2_Cerydra_Regent with fade


    Noble "我们在此聚集，见证王女的回归！" id _102_0037




    commoner_hopeful "她的头发......只有塔兰顿赐福的王室才有那样的蓝发！难道她真的......" id _102_0038
    commoner_doubtful "还有呢？还有呢？！天选之人才能流淌的黄金血！" id _102_0039


    Noble "北境的子民啊！看呐！战火灼烧北境十数载，而今，先王的血脉将重归王座！" id _102_0040
    Noble "站在我身边的，是旧王朝最后的明珠——" id _102_0041
    Noble "王女殿下，刻律德菈！" id _102_0042
    play sound "sfx/concert_hubbub.mp3" fadein 1.5 volume 0.5
    "群众" "......" id _102_0043
    stop sound fadeout 3.0
    Noble "肃静！" id _102_0044

    Noble "抬起头来，诸位！因为许珀耳的新王，已从火中归来！" id _102_0045

    Noble "从此，再无分裂与战乱。吾等都应当团结在黄金的血脉下，重建富饶的家园！" id _102_0046

    Cerydra "......" id _102_0047
    "王女依旧沉默。" id _102_0048
    "风更大了，卷着雪沫子拍打在人们脸上。" id _102_0049
    "哪怕是再狂热的口号，也填不饱肚子，驱不散严寒。" id _102_0050
    "人们需要的不是一个漂亮的木偶，而是一个能带来粮食和火炭的王。" id _102_0051
    play sound "sfx/talking.mp3" fadein 1.0 volume 1
    "骚动变得剧烈。有人挥舞着拳头，有人伸长了脖子。" id _102_0052



    commoner_doubtful "给我们看证据！" id _102_0053
    "大声的平民" "黄金血！黄金血！" id _102_0054
    "大声的平民" "我们不要空话！我们要活路！" id _102_0055

    Noble "神谕已至，圣女的预言已达，神赐的凭证，岂容置疑？" id _102_0056

    "王女" "......" id _102_0057

    commoner_doubtful "她到底在等什么？" id _102_0058
    commoner_doubtful "都到了现在了，还要我们等吗？！" id _102_0059
    "平民" "要是真的有金血，有什么可遮遮掩掩的......" id _102_0060

    "平民" "不会是个骗子吧？" id _102_0061


    show cg p1_ch2_CerydraBlack with dissolve
    stop sound fadeout 3.0
    Noble "肃静！" id _102_0062
    Noble "我看到你们焦虑，愤懑，忧心忡忡。而王女殿下仁慈，会给予你们祈求之物。" id _102_0063

    Noble "请吧，殿下。只要一滴血，所有的质疑都将烟消云散。" id _102_0064

    "王女" "......" id _102_0065
    Noble "取刀来。" id _102_0066
    show cg p1_ch2_Cerydra_blood_noblood with Fade(0.5, 1.0, 1.5)
    pause 2.0
    show cg p1_ch2_Cerydra_blood_eyeclosed_noblood with dissolve
    pause 2.0
    show cg p1_ch2_Cerydra_blood_smile_noblood with dissolve
    pause 2.0
    show cg p1_ch2_Cerydra_blood_smile with dissolve

    "群众" "......" id _102_0067
    stop sound fadeout 3.0



    "众平民" "神迹！是神迹！" id _102_0068

    "众平民" "刻律德菈！许珀耳的女王！" id _102_0069
    play sound "sfx/metal.mp3" volume 0.5 fadeout 10.0
    show cg p1_ch2_Cerydra_blood with dissolve
    "少女——现在的女王——站在高台上。她松开手，任由染血的匕首掉落。" id _102_0070
    play sound "sfx/long_clapping.mp3" fadein 3.0 volume 0.5
    "清脆的响声被欢呼声淹没。" id _102_0071
    stop sound fadeout 2.0
    "人们争先恐后地低下头去，向那滴血液献祭自己的虔诚。仿佛只要沾染上一点金色，便能从无尽的苦难中得到解脱。" id _102_0072
    "王女却将目光投向高处。" id _102_0073

    show cg p1_ch2_sky with fade
    "阴云如铅块般低垂，寒鸦划过晦暗的天幕。" id _102_0074
    "它在大风中艰难地维持着平衡，像是与无形的命运搏斗。" id _102_0075
    "它是自由的吗？" id _102_0076
    "还是说，{w}这漫天的风雪早已写好了它的坠落？" id _102_0077




    scene white with fade
    pause 1.0

    centered "{size=40}{color=#000000}快马踏碎了黎明的薄冰，将那一滴黄金血传遍了六邦十二城。" id _102_0078
    extend "\n\n消息在一夜之间点燃了整个北境。" id _102_0079
    extend "\n\n黄金血，是神明尚未抛弃这片土地的铁证。" id _102_0080
    extend "\n\n人们奔走相告，在街头巷尾，在每一张餐桌前，那个名字——“刻律德菈”，被无数次咀嚼、吞咽。{/color}{/size}" id _102_0081
    centered "{size=40}{color=#000000}战争无止无休，许多东西都将匮乏。" id _102_0082
    extend "\n\n但绝不会匮乏的是痛苦，泥浆，血液和死亡。成千上万的死亡。" id _102_0083
    extend "\n\n......人们都期待和平。" id _102_0084
    extend "\n\n人们说：“她承诺了和平。”{/color}{/size}" id _102_0085




    stop music fadeout 3.0

    scene bg Cerydra_room with Fade(1.0, 0.5, 2.0)
    play music "music/New Page.mp3" fadein 2.0 fadeout 1.0
    pause 2.0

    show Cerydra smile_wocrown at left with dissolve




    Cerydra "你回来了。" id _102_0086
    Cerydra "你在笑，看来....事情比我们预想的还要顺利。" id _102_0087
    Cerydra "万众瞩目之下，是何种感觉？" id _102_0088
    show CerydraBlack at right with dissolve
    Unknown_CerydraBlack "......" id _102_0089
    Cerydra "你的血还在流，我为你包扎一下吧。" id _102_0090
    show cg p1_ch2_hand with fade
    Cerydra "......我从未这样愤恨我们的躯体。" id _102_0091
    Cerydra "我们是同胞而生的姐妹......为何我生来康健，你却如此脆弱？" id _102_0092
    Cerydra "为何我是凡血，你是黄金？" id _102_0093
    CerydraBlack_shadow "「缺陷是金血的代价。」" id _102_0094
    Cerydra "......是啊。" id _102_0095
    Cerydra "听说，黄金裔中，有些人陷入疯狂，有些人天生失明，有些人流失人性....." id _102_0096
    Cerydra "而你被剥夺了声音。" id _102_0097
    Cerydra "所以，只能由你走上台前，用血液博得信赖；也只能由我演讲、巡游，鼓动人心。" id _102_0098
    Cerydra "我们就像是被神明随手撕开的一张纸，拼在一起才算完整。" id _102_0099
    Cerydra "拼在一起，才是王女「刻律德菈」。" id _102_0100
    CerydraBlack_shadow "......" id _102_0101
    Cerydra "...总有一天，我们会亲自改写这一切。" id _102_0102
    hide cg p1_ch2_Cerydra_CerydraBlack with fade
    show Cerydra normal_wocrown at extreme_left
    show CerydraBlack angry at extreme_right
    show Regent smile
    with dissolve

    Noble "哦，王女殿下，日安。" id _102_0103
    Noble "原来你们在这里享受难得的清净，我还以为您正忙着挑选晚宴的首饰呢。" id _102_0104

    Noble "我亲爱的孩子，今天的归来仪式堪称完美。" id _102_0105
    Noble "您听听外面，民众的欢呼简直令人心醉。" id _102_0106
    Noble "啊......战争，天灾，饥饿......他们太需要一道确凿无疑的光亮了。" id _102_0107
    Cerydra "......" id _102_0108
    Noble "民众往往盲目。他们是受惊的鸟雀，哭嚎，奔逃，却不知路在何方。" id _102_0109

    Noble "王国需要您高贵的血脉，为他们指明道路。" id _102_0110

    show Cerydra angry_wocrown

    Cerydra "哦？阁下突然造访，总不会是演讲欲还没有得到满足，想对我再即兴一段吧？" id _102_0111

    Noble "还是这么牙尖嘴利，我的孩子，这可不好。" id _102_0112
    Noble "您现在是王女，您要成为一个能让他们顶礼膜拜的偶像。" id _102_0113

    Noble "这轻而易举。您只需要像今天一样，保持您的美丽、高贵与仁慈....." id _102_0114
    Noble "我会为您解决一切烦恼。" id _102_0115

    show Cerydra eyeclosed_wocrown with dissolve

    Cerydra "......" id _102_0116

    show Cerydra sneer_wocrown with dissolve



    Cerydra "你想做摄政王。" id _102_0117
    show Cerydra normal_wocrown with dissolve

    Noble "您的聪慧，总是这么令我惊喜。" id _102_0118

    Noble "好了，刻律德菈。晚宴马上就要开始了，要熟记礼节才行哦？" id _102_0119
    Noble "可不要像乞丐一样，让人看笑话。" id _102_0120
    Noble "细节决定成败，尤其是对刚刚归来的王女而言。你说呢？" id _102_0121
    show Cerydra sneer_wocrown with dissolve

    Cerydra "不必多言。" id _102_0122

    play sound "sfx/walkout.mp3" 
    hide Regent with dissolve
    pause 1.0

    show Cerydra eyeclosed_wocrown at left
    show CerydraBlack at right
    with dissolve

    Cerydra "我们的身份，是她手中的把柄。" id _102_0123
    Cerydra "她手握「刻律德菈」有两人的秘密，因此......" id _102_0124
    show Cerydra normal_wocrown with dissolve
    Cerydra "此时此刻，你我无法颠覆她。" id _102_0125

    CerydraBlack_shadow "......" id _102_0126

    CerydraBlack_shadow "「猎物在以为自己掌控一切的时候，往往是最松懈的。」" id _102_0127

    Cerydra "即便，我们只能是她手中的剑？" id _102_0128
    show CerydraBlack cat with dissolve

    CerydraBlack_shadow "「那就做一柄最好的剑。直到......剑尖调转的那一天。」" id _102_0129

    Cerydra "在那之前，我们要一直这样演下去，是么？" id _102_0130
    Cerydra "你是影子，而我是傀儡。" id _102_0131
    show CerydraBlack eyeclosed with dissolve

    CerydraBlack_shadow "「我们是共犯，刻律德菈。」" id _102_0132
    show CerydraBlack cat with dissolve
    CerydraBlack_shadow "「只要我们在一起，这就不是表演，而是......狩猎。」" id _102_0133
    scene black with fade
    play music "music/Agnus Aeon.mp3" fadein 2.0 fadeout 2.0
    pause 0.5
    show bg fireseed at truecenter with Dissolve(2.0)
    pause 1.0

    "[user_name]" "原来，刻律德菈并不是王女，而是被捏造了身份的女孩......" id _102_0134
    "[user_name]" "一对双生子共同登上王位，当世，后世，都无人知晓......真是匪夷所思。" id _102_0135
    "[user_name]" "除此之外，塔兰顿的态度也很古怪。" id _102_0136
    "[user_name]" "为什么说“金血是罪恶之物”？" id _102_0137
    "[user_name]" "那个谈论黄金血的男人，又是谁？" id _102_0138
    "[user_name]" "......继续阅读记忆吧，或许能找到真相。" id _102_0139
    stop music fadeout 2.0

    show cg p1_ch2_map with Fade(1.0, 1.0, 1.5)
    pause 1.0

    play music "music/Lost but Won.mp3" fadein 2.0
    "自从被推上台前，年轻的王女并未如众人预料般，成为安静的傀儡。" id _102_0140
    "她巡游全境，在广场、在军营、在贫民窟发表演说。" id _102_0141
    "蓝发在风雪中飘扬，她承诺面包，承诺秩序。" id _102_0142
    "奇迹般地，濒临崩溃的许珀耳在她手中竟有了起色，暴乱渐息，粮仓渐满。" id _102_0143
    "如今，哪怕是再傲慢的贵族也不得不承认——{w}那个位置上坐着的，不仅仅是一个漂亮的符号。" id _102_0144




    scene bg Okhema_palace_indoor_day with Fade(1.0, 1.0, 1.5)
    "许珀耳王城，议事厅" id _102_0145


    "侍者" "王女殿下已至！" id _102_0146
    show Cerydra normal_wocrown at center with dissolve
    Cerydra "贵安。诸位阁下，我乃先王姊妹之女，刻律德菈。" id _102_0147
    play sound "sfx/concert_hubbub.mp3" volume 0.5 fadein 1.0
    "侍者" "肃静！" id _102_0148
    stop sound fadeout 3.0
    Cerydra "时间宝贵，我便直入主题了。" id _102_0149
    Cerydra "市井之人所求不过温饱，朝夕可度。可我知道，在座诸位想要更多。" id _102_0150
    show Cerydra smile_wocrown with dissolve
    Cerydra "譬如，我的“新律”能如何让只值三个铜板的蜜酿，在南境卖上十万利衡币的高价。" id _102_0151
    Cerydra "又譬如，这“新律”如何能让诸位手中的私兵不再受限，可以扩充成两支、三支......" id _102_0152

    Cerydra "直至踏平南境的冻土，将新的领地划入诸位的名下。" id _102_0153

    play sound "sfx/concert_hubbub.mp3" volume 0.1
    "贵族" "王女！新律如何，若落不到手里，不过是一纸空谈。" id _102_0154
    "贵族" "您描绘的蓝图再宏大，也不如一枚枚落袋的金币来得响亮。" id _102_0155
    play sound "sfx/laughing.mp3" volume 0.5


    "众宾" "哈哈哈哈！是啊，殿下，空头支票我们可吃不下！" id _102_0156
    stop sound fadeout 1.0
    Cerydra "......" id _102_0157
    show Cerydra normal_wocrown with dissolve
    Cerydra "阁下所言极是。若权力不在掌中，律法便是废纸。" id _102_0158
    Cerydra "我尚年幼，羽翼孱弱。在这深宫之中，不得不将大权暂且推与摄政王。" id _102_0159
    show Cerydra angry_wocrown with dissolve
    Cerydra "但今日我依然设宴，只因我知晓......" id _102_0160
    Cerydra "诸位与我一样，皆为摄政王所不容。" id _102_0161
    show Cerydra eyeclosed_wocrown with dissolve
    "宾客" "......" id _102_0162

    Cerydra "近年来，这许珀耳的蛋糕不仅没有变大，反而在她的独裁下越切越小，你们积怨已久。" id _102_0163
    show Cerydra sneer_wocrown with dissolve
    Cerydra "诸君，想要见到财富与权力重新流向你们的家族......节流不如开源。" id _102_0164
    show Cerydra eyeclosed_wocrown with dissolve
    Cerydra "许珀耳的土地贫瘠，养不活太多的野心。所以——" id _102_0165
    show Cerydra normal_wocrown with dissolve
    Cerydra "向外看。" id _102_0166
    Cerydra "南方的吕奎亚人，据守暖水港和矿脉，囤积着足以让我们度过十个冬天的粮食。" id _102_0167
    show Cerydra smile_wocrown with dissolve
    Cerydra "若能取得这场战争的胜利......诸位，那是荣耀，更是财富。" id _102_0168
    "宾客" "是啊......与其相互倾轧，不如......" id _102_0169
    show Cerydra angry_wocrown with dissolve
    Cerydra "许珀耳能否取得这场战争的胜利，夺回我们血脉中的荣耀？！" id _102_0170
    show Cerydra eyeclosed_wocrown with dissolve
    Cerydra "我多么希望，能直接许诺各位胜利的果实。" id _102_0171
    show Cerydra angry_wocrown with dissolve
    Cerydra "但......这战场上的答案，只能由你们来书写！" id _102_0172
    Cerydra "告诉我！你们的剑，还利吗？" id _102_0173
    "贵族2" "殿下！如果我们出兵......新律承诺的那些？" id _102_0174
    show Cerydra normal_wocrown with dissolve
    Cerydra "刻律德菈从不食言。" id _102_0175
    play sound "sfx/long_clapping.mp3" fadein 1.0 volume 0.1
    "贵族们" "好！为了荣耀！" id _102_0176
    "贵族1" "为了许珀耳！" id _102_0177

    show Cerydra smile_wocrown with dissolve
    Cerydra "那么，让我们举杯：敬新律！" id _102_0178
    "贵族们" "敬新律！" id _102_0179
    pause 1.0
    stop sound fadeout 2.0

    scene bg Cerydra_room with Fade(1.0, 2.0, 2.0)
    show Cerydra normal_wocrown at left
    show CerydraBlack cat at right
    with dissolve
    Cerydra "是宰相的密信。我们的“象”就位了。" id _102_0180
    CerydraBlack_shadow "「是时候了。」" id _102_0181
    show Cerydra sneer_wocrown with dissolve
    Cerydra "一切如我们所料。那些贪婪的家伙已经咬钩，迫不及待地想要发动战争。" id _102_0182
    show Cerydra normal_wocrown with dissolve

    Cerydra "不过......南方的吕奎亚人不仅有坚固的堡垒，兵力也远多于我们。" id _102_0183
    Cerydra "按照常规推演，这根本就是一场——必败的仗。" id _102_0184
    CerydraBlack_shadow "「置之死地而后生。」" id _102_0185
    Cerydra "当然。这正合我意，不是吗？" id _102_0186
    show Cerydra smile_wocrown with dissolve
    Cerydra "若非必败之局，摄政王怎会放心把兵权交到我手里？" id _102_0187
    Cerydra "她想让我死在战场上，或者...背着战败的骂名回来领死。" id _102_0188
    Cerydra "但她忘了，战场之上，瞬息万变。不到最后，谁也无法轻言结局。" id _102_0189
    Cerydra "这一次，我要让所有人看到......谁才是真正的“王”。" id _102_0190

    scene black with fade
    pause 2.0



    scene bg Palace_meetingroom with fade
    show Cerydra normal_wocrown at left
    show Regent at right
    with dissolve

    Regent "军务大臣，财政官......" id _102_0191
    Regent "也是稀奇，那群平日里吵得不可开交的老东西，今天的意见倒是难得一致。" id _102_0192
    Regent "也许是你今晚的宴会起了效果？呵......" id _102_0193
    Regent "他们说，许珀耳不能再困守于此。北境的冻土种不出粮食，如果不打通南方的补给线，这个冬天......会有一半的平民饿死。" id _102_0194
    Regent "他们提议——出征。" id _102_0195
    Cerydra "为生存而战，不仅是贵族的愿望，也是民心所向。" id _102_0196
    Regent "我亲爱的孩子。这也是为了你啊。你知道，这是一次豪赌。" id _102_0197
    Regent "吕奎亚人不是软柿子。但若是赢了......" id _102_0198
    Regent "许珀耳疆域扩张，你的威望将无人能及。" id _102_0199
    show Cerydra smile_wocrown with dissolve
    Cerydra "呵。您也会依然是那位深受爱戴的摄政王，不是吗？" id _102_0200
    show Regent smile with dissolve
    Regent "既然是众望所归，我也只能顺水推舟了。" id _102_0201
    show Cerydra normal_wocrown with dissolve
    Regent "我真的很担心你的安危，我的孩子......" id _102_0202
    Regent "但作为王室的旗帜，只有你亲自挂帅，那些饿狼才肯卖命。" id _102_0203
    Regent "殿下，您应该不会缺少这点勇气，对吗？" id _102_0204
    Cerydra "于国于民，我理应出征。若就此退缩，这“王女”之名，不要也罢。" id _102_0205
    Regent "殿下越发果断了。好，好极了！" id _102_0206
    Regent "既已得到您的首肯，臣这就去安排。" id _102_0207
    Regent "啊呀，瞧我，人老了就容易啰嗦。深夜邀约实在不合礼节，要是累坏了殿下，可就是我的罪过了。" id _102_0208
    Regent "万望注意贵体，那战场上刀枪无眼......王国暂时不能没有您。" id _102_0209
    show Cerydra smile_wocrown with dissolve
    Cerydra "呵，多谢关心。" id _102_0210
    Cerydra "需要谁，许珀耳自会做出选择。" id _102_0211
    play sound "sfx/walkout.mp3" fadein 0.5 volume 2
    hide Cerydra with dissolve


    Regent "......" id _102_0212
    Regent "我骄傲的孩子啊.....王座太窄了。" id _102_0213
    Regent "只需要一个听话的，就够了。" id _102_0214


    scene black with fade
    stop music fadeout 2.0
    pause 2.0
    play music "music/Frozen March.mp3" fadein 2.0

    pause 2.0
    "穿越埃普斯群山，一场闪电般的奇袭，撕开了南方坚不可摧的防线。" id _102_0215
    "吕奎亚的臣服不过是这出宏大戏剧的序章。金血将领福特图多，注定要在她剑指之处折戟，化作王座下最坚固的基石。" id _102_0216
    "一城、两城、三城...许珀耳的军队如火焰燎原。" id _102_0217
    "城门接连洞开，如同倒下的多米诺骨牌。军队的洪流用铁与血洗刷着旧日的边界。" id _102_0218
    "当蓝发的少女高举旗帜，铁蹄将踏破她所指向的国度——" id _102_0219

    scene bg Palace_meetingroom with Fade(1.0, 1.5, 1.5)
    show Regent at center with dissolve



    "密探" "大人......这就是前线的消息。吕奎亚军队全线溃败，指挥官死状凄惨。" id _102_0220
    "密探" "据说......是因为触怒了王女，被律法碎尸万段。" id _102_0221
    with vpunch

    show Regent angry with dissolve
    Regent "那个冒牌货......她怎么可能！" id _102_0222
    "密探" "王女的军队，的确行过雅努萨波利斯。相传，王女独自进入神殿......" id _102_0223
    "密探" "自那之后，军队士气高涨，都在传颂王女是塔兰顿的化身。" id _102_0224
    "密探" "要是让她带着大军回来......" id _102_0225
    show Regent smile with dissolve
    Regent "呵......她回不来。" id _102_0226

    Regent "既然吕奎亚人杀不了她，那就让许珀耳人自己来杀。" id _102_0227
    Regent "传令下去，封锁所有前线消息。" id _102_0228
    Regent "告知全城，王女刻律德菈，已在南境战败，生死不明。" id _102_0229
    "密探" "这......大人......" id _102_0230
    Regent "无需忧惧。“陛下”在宫中，不是么？" id _102_0231
    Regent "就算她能够班师回朝，只要二人当面对质，迫使她露出红色的血液......" id _102_0232
    Regent "哈哈哈......她最忠诚的将士，也会倒戈。" id _102_0233
    "密探" "阁下，真是妙计。" id _102_0234
    Regent "只要谎言说得足够大，只要恐惧埋得足够深......" id _102_0235
    Regent "愚民们只会相信他们愿意相信的东西。" id _102_0236

    stop music fadeout 3.0
    play music "music/Lost but Won.mp3" fadein 2.0

    scene bg Wild_night with Fade(1.0, 1.5, 1.5)
    show Cerydra normal_wocrown at center with dissolve

    "卫兵" "模模糊糊的影子......是王城吗？" id _102_0237
    "卫兵" "我......活着回来了？" id _102_0238
    show Cerydra angry_wocrown with dissolve
    Cerydra "将士们，都城就在前方！" id _102_0239
    Cerydra "我们夺取了荣耀，我们夺取了生存的权利。现在——" id _102_0240
    show Cerydra smile_wocrown with dissolve
    Cerydra "去拿回属于我们的奖赏！" id _102_0241
    "众人" "为了许珀耳！为了陛下！" id _102_0242
    "众人" "为了许珀耳！为了陛下！" id _102_0243
    "卫兵" "等等，都城的城门，为何紧闭？" id _102_0244
    show Cerydra normal_wocrown at center with dissolve
    "卫兵" "那是......摄政王阁下？" id _102_0245



    scene bg Styxia_outdoor_night with Fade(1.0, 0.5, 1.5)
    show Regent angry at center with dissolve

    "大臣" "阁下，我军得胜归来，还请速速打开城门，犒劳将士！" id _102_0246
    Regent "城下何人？竟敢冒充我许珀耳大军！" id _102_0247
    play sound "sfx/concert_hubbub.mp3" fadein 1.0 volume 0.2

    "士兵" "冒充？我身上的伤难道是假的？！" id _102_0248
    "士兵" "那是摄政王！她疯了吗？" id _102_0249
    "士兵" "我们为了许珀耳流血拼命，回来就这个待遇？！" id _102_0250
    "大臣" "摄政王阁下！我们带着吕奎亚人的降书，还有满载的战利品！您这是何意？" id _102_0251
    stop sound fadeout 2.0
    "王女抬起手，止住了身后的骚动。" id _102_0252
    "她策马上前几步，独自站在吊桥前。" id _102_0253
    Regent "......" id _102_0254
    "刻律德菈仰起头，看着城楼上那个熟悉的身影。" id _102_0255
    show Regent smile at right
    show Cerydra normal_wocrown at left
    with dissolve
    Cerydra "既见王女，为何不行礼？" id _102_0256
    Regent "哈哈哈哈......何其可笑！" id _102_0257
    Regent "王女？你也配！" id _102_0258
    play sound "sfx/concert_hubbub.mp3" fadein 1.0 volume 0.2
    pause 3.0


    stop sound fadeout 1.0
    Regent "你们以为，你们追随的是王女，对吗？" id _102_0259
    Regent "睁开眼看看吧，将士们！" id _102_0260
    Regent "战败的消息早已传回王城，你们的王身受重伤，已然失声。" id _102_0261
    Regent "她由我的手下亲手救回，此刻就在寝殿中！" id _102_0262
    play sound "sfx/concert_hubbub.mp3" fadein 1.0 volume 0.2
    "民众" "这......不可能吧......" id _102_0263
    Regent "如今从南方归来的，是吕奎亚人的妖女，是窃取了王女面容的异族怪物！" id _102_0264
    Regent "你们正在对一个傀儡顶礼膜拜......对一个骗子卑躬屈膝！" id _102_0265
    "民众" "......" id _102_0266
    "卫兵" "肃静！" id _102_0267
    stop sound fadeout 1.0
    Cerydra "摄政王，你在质疑我的身份与血统？" id _102_0268
    Cerydra "你是否想过，诽谤皇室的代价？看来，你已做好身首异处的准备。" id _102_0269
    Regent "是吗？那么你大可以划破手腕，证明你就是我们敬爱的王。" id _102_0270
    show Cerydra smile_wocrown with dissolve
    Cerydra "......" id _102_0271

    "她静静地看着摄政王，眼神里甚至带着一丝怜悯。" id _102_0272
    show Cerydra sneer_wocrown with dissolve
    Cerydra "这就是你的底牌吗？" id _102_0273

    show cg p1_ch2_CerydraWhite_blood_noblood with Fade(1.0, 1.0, 1.5)
    pause 2.0


    show Cerydra normal_wocrown with dissolve
    Cerydra "谎言终究是谎言。" id _102_0274
    Cerydra "而我向臣民许诺的......绝无虚假。" id _102_0275
    "她举起剑，将剑刃对准了自己的手掌。" id _102_0276
    "所有人都屏住了呼吸。城上的人，城下的人。" id _102_0277
    "这一幕似曾相识。" id _102_0278
    "摄政王的心猛地跳了一下。她想起了广场上的下午，那滴金色的血。" id _102_0279
    pause 2.0
    show cg p1_ch2_CerydraWhite_blood_smile with dissolve
    pause 2.0
    show cg p1_goldblood with dissolve
    pause 2.0

    "少女划破手腕，黄金血伴随众人的嗤笑滴落，将「王」的绝望淹没。" id _102_0280

    show Cerydra sneer_wocrown with dissolve
    Cerydra "我，刻律德菈，许珀耳的女王。" id _102_0281
    show Cerydra eyeclosed_wocrown with dissolve
    Cerydra "我带着荣耀归来。而你们——" id _102_0282
    show Cerydra angry_wocrown with dissolve
    Cerydra "要将你们的王，拒之门外吗？" id _102_0283
    "民众" "陛下！" id _102_0284
    "民众" "摄政王胡言乱语......竟敢质疑凯撒大人？！" id _102_0285
    show Regent angry with dissolve
    Regent "......不......这不可能......" id _102_0286
    hide cg with dissolve
    show Cerydra sneer_wocrown with dissolve

    Cerydra "我已经没有耐心与你多费口舌，败者。" id _102_0287

    Cerydra "卫兵？" id _102_0288
    "卫兵" "在！" id _102_0289

    Cerydra "将她拖下去。今夜，我为许珀耳带来公正。" id _102_0290
    "卫兵" "是！" id _102_0291
    hide cg with dissolve
    show Cerydra normal_wocrown with dissolve

    Regent "哈......吕奎亚的妖女，你倒是费尽心机，连金血也事先伪造！" id _102_0292
    Regent "将士们，莫要被她蒙蔽——异族正在颠覆我们的王国！" id _102_0293
    Regent "去宫殿！去宫殿！去看看，你们的王还安安稳稳的在那里啊！" id _102_0294
    play sound "sfx/concert_hubbub.mp3" fadein 1.0 volume 0.2
    "卫兵" "这......" id _102_0295
    "卫兵" "上周就听说军队大败了。为什么突然凯旋而归？" id _102_0296
    "卫兵" "陛下身后，还有异族的军队。" id _102_0297
    "大臣" "陛下，老臣也觉得，您长途奔波，也该回宫殿修整——" id _102_0298






    Cerydra "......" id _102_0299
    stop sound fadeout 1.0

    "平民" "殿下——殿下——！" id _102_0300
    play heartbeat "sfx/heart.mp3" volume 3

    Cerydra "何事？" id _102_0301




    "平民" "皇宫——起火了！" id _102_0302
    stop music fadeout 2.0
    play sound "sfx/erming.mp3" fadein 1.0 volume 2

    pause 5.0
    stop sound
    scene black
    pause 1.0




    scene bg Okhema_palace_outdoor_night
    show Cerydra sad_wocrown
    pause 0.5
    play sound "sfx/fire.mp3" fadein 3.0 
    scene white
    pause 0.25
    scene bg Garden_night
    show Cerydra sad_wocrown
    pause 0.5
    scene white
    pause 0.25
    scene bg Okhema_palace_outdoor_night
    show Cerydra sad_wocrown
    pause 1.0


    show cg p1_ch2_CerydraBlack_die with Fade(1.0, 1.0, 1.5)
    pause 2.0



    Cerydra "█ ██ ███ ███████████" id _102_0303
    show cg p1_ch2_CerydraBlack_die_hand with Dissolve(1.5)
    CerydraBlack_shadow "「你」" id _102_0304

    CerydraBlack_shadow "「成为」" id _102_0305

    CerydraBlack_shadow "「王」" id _102_0306
    show cg p1_ch2_CerydraBlack_die_eyeclosed_hand with Dissolve(1.5)
    pause 2.0
    Cerydra "███████████" id _102_0307
    Cerydra "███████！！！" id _102_0308

    play music "music/rain.mp3" fadein 2.0

    stop heartbeat
    stop sound
    scene bg Okhema_palace_indoor_day with Fade(2.0, 3.0, 1.5)
    show Cerydra sad_wocrown with dissolve




    "仆人" "殿下......殿下......" id _102_0309

    "仆人" "您醒了！昏光庭院的人已经候着了，我这就叫他进来。" id _102_0310

    Cerydra "......" id _102_0311

    Cerydra "火......大火......怎么样了？" id _102_0312

    "仆人" "多亏您指挥及时，殿下，宫人都已撤离完毕。" id _102_0313

    "仆人" "您冲入火场之后，下了一场大雨。或许是天意吧，这火势起得迅猛，退得也快，万幸没有蔓延到别处。" id _102_0314

    "仆人" "只是那寝宫，还有您的冠冕......" id _102_0315

    Cerydra "......" id _102_0316

    "仆人" "殿下何必忧心？匠人再为您打造一顶便是，您怎能这般以身犯险？您可是帝国的支柱，国不可一日无君......" id _102_0317

    Cerydra "...都退下。" id _102_0318

    "仆人" "殿下，您还没恢复...您要去哪？！" id _102_0319
    show Cerydra angry_wocrown with dissolve

    Cerydra "退下！" id _102_0320


    scene black with fade
    play sound "sfx/rain.mp3" fadein 2.0 volume 0.5


    "女孩行走在雨中。" id _102_0321

    "茫茫天地间，刻律德菈从未如此孤独。" id _102_0322

    "——影子不能留下痕迹。所以，她选择了火。" id _102_0323

    "她把完美的谎言留给了世界，却将真实烧成了灰。" id _102_0324



    "焦糊的气味涌入她的胸口，死死的攥住她的肺叶。令人作呕。" id _102_0325




    scene cg p1_ch2_Cerydra_rain with fade



    Cerydra "哈......哈哈......" id _102_0326

    Cerydra "这就是我们筹谋了多年的，所谓的“胜利”？！" id _102_0327

    "双手插进焦黑色的土壤。泥水瞬间没过了指缝，像是无数只冰凉的小手，死死地抓住了她，要将她一同拖入地狱。" id _102_0328

    Cerydra "......" id _102_0329

    Cerydra "...是你吗？" id _102_0330

    "年轻的女孩拾起地上的冠冕。" id _102_0331



    "一缕幽蓝的火苗在冠冕上摇曳。雨丝点点落下，打在火上。" id _102_0332

    "下意识地，女孩抬起血肉模糊的手，在它上方撑起一方摇摇欲坠的天地。" id _102_0333

    Cerydra "......别熄灭......" id _102_0334

    Cerydra "......别让这最后的亮光也离开我。" id _102_0335

    "可那火并不灼手；火苗温柔地舔舐着她满是泥污的手指。" id _102_0336


    "雨水和着泪水，在苍白的脸上汇成一片，从指缝间滴滴落下。" id _102_0337

    "那火却没有被熄灭，反而像是饮下了这份悲伤的供养，在风雨中攒动着、高涨着。" id _102_0338

    "像是要跳完这一生最后的一支舞。" id _102_0339

    Cerydra "哈......" id _102_0340

    Cerydra "你想让我......戴上它......" id _102_0341

    pause 2.0


    scene cg p1_ch2_shadow with Fade(1.0, 1.5, 1.5)














    CerydraBlack_shadow "「如果可以的话，真想看到你的加冕礼。」" id _102_0342

    Cerydra "......" id _102_0343

    CerydraBlack_shadow "「还在为那倒戈的棋子伤神吗？」" id _102_0344

    Cerydra "......不。不好用的棋子，换一个便是。这等小角色，还不值得遗憾。" id _102_0345
    Cerydra "我总以为，人性是可以把握的。对于懦弱的叛徒，以仁慈饶恕他们，借此收拢人心，也是好的。" id _102_0346

    Cerydra "如今看来，这一局，是你赢了啊。" id _102_0347


    play sound "sfx/clinking3.mp3"

    "两只酒杯在空中轻碰，发出清脆的鸣响。" id _102_0348

    CerydraBlack_shadow "......" id _102_0349

    CerydraBlack_shadow "「以仁慈回报背叛，你该用什么回报忠诚呢？」" id _102_0350

    Cerydra "......的确。" id _102_0351
    Cerydra "好了，你我都不爱饮酒，就别装什么大人了。" id _102_0352

    Cerydra "明天的加冕礼只能由我去......也没什么意思。" id _102_0353
    Cerydra "刻律德菈的加冕礼，应该是我们携手在街上巡游。万千民众仰望欢呼，鲜花像雨一样从露台洒下，铺满整条大道。" id _102_0354
    Cerydra "金色的马车碾过花瓣，我们在欢呼声中登上最高的祭坛。" id _102_0355

    Cerydra "接着，神礼官向我们呈上冠冕与权杖。你我互相为对方戴冠，你我共同举起权杖。" id _102_0356

    Cerydra "待我们坐稳了位置......我必让匠人为你打造一顶一模一样的......不，比我的更精致，更华丽......" id _102_0357

    "女孩抬起手，止住了她的话语。" id _102_0358

    CerydraBlack_shadow "「不必遗憾，刻律德菈。」" id _102_0359

    CerydraBlack_shadow "「既然你想要一场属于我们的加冕礼......就让我来为你加冕吧。」" id _102_0360

    CerydraBlack_shadow "「披上你的长袍，抬起头......让我看看我的姊妹。」" id _102_0361
    pause 1.0

    CerydraBlack_shadow "「你从未像今天这样像一位女皇。」" id _102_0362


    show cg p1_ch2_Cerydra_rain with fade



















    "恭喜你，刻律德菈。"
    "许珀耳的女王，刻律德菈。"
    "你知道吗？我一直做着一个梦。"
    "你不是傀儡，我也不是影子。梦里，我们是真正的王女。我能站在正午的阳光下，大声叫你的名字。"
    "我们是这世上最亲密的共犯。只要我还活着，你就永远陷在泥潭里；只要我的影子还投在地上，你的王座下便不会安稳。"
    "这不公平，对吧？"
    "塔兰顿给了你声音，却给了我金血；命运给了我们野心，却给了我们枷锁。"
    "我们就像是被神明随手撕开的一张纸，拼在一起才算完整。"
    "所以，我们不会分离。"
    "我想做一次......哪怕只有一次，做那个为你加冕的人。"
    "从此以后，这世上再也没有躲在暗处的哑巴。也没有时刻提心吊胆、行走在刀尖上的王女。"
    "只有刻律德菈。"
    "只有凯撒。"
    "别回头，刻律德菈。别去废墟里找我。我已经不在那里了。"
    "当你举起剑的时候，我就在你的剑锋上；"
    "当你征服那个世界的时候......我就在你的眼睛里。"
    "就在你的血里，就在你的冠冕上。"

    Cerydra "不要低头。刻律德菈。" id _102_0380
    Cerydra "不要向世界低头，不要向命运低头。" id _102_0381

    Cerydra "让火焰永远向高天燃烧，让你的心......如此刻昭昭。" id _102_0382

    pause 2.0
    play music "music/Fate.mp3" fadein 2.0 fadeout 1.0

    scene bg Okhema_citygate_day with Fade(2.0, 3.0, 1.5)
    show Cerydra at center with dissolve

    Cerydra "时辰已到，把她带上来。" id _102_0383

    "卫兵" "是！" id _102_0384

    "民众 " "摄政王......是她！" id _102_0385

    "民众 " "该死的摄政王......就是她点燃了皇宫，想要加害陛下！" id _102_0386

    "民众 " "杀了她！杀了她！" id _102_0387


    "女王抬起手，掌心向下。" id _102_0388

    "仅仅一个动作，沸腾的人海便被扼住咽喉。" id _102_0389

    "她即使一言不发，也已是这里的王。" id _102_0390
    Cerydra "许珀耳的子民——抬起头来！" id _102_0391
    show Cerydra normal at left
    show Regent at right
    with dissolve
    Cerydra "今日，我为许珀耳带来公正！" id _102_0392
    show Cerydra angry with dissolve
    Cerydra "旧律已随战火化为灰烬，从今往后，我将是许珀耳唯一的王，也是唯一的律法！" id _102_0393
    show Cerydra eyeclosed with dissolve
    Cerydra "我们聚首于此，不为庆功，只为审判。" id _102_0394
    show Cerydra normal with dissolve
    Cerydra "站在你们面前的，是帝国这一代以来最大的罪人——前摄政女公爵！" id _102_0395
    Cerydra "以“摄政”之名，行僭越之实；她口称荣耀，实则用尔等的血肉填满私欲。她令帝国深陷内乱的泥沼，令饥荒蔓延如瘟疫，近乎断送帝国的未来！" id _102_0396
    show Cerydra angry with dissolve
    Cerydra "依据新律，此人罪无可赦！今日，我以“律法”之名，宣判汝——火刑！" id _102_0397
    Cerydra "不论是谁，凡试图凌驾于帝国之上、以阴谋亵渎公义者——此火，便是结局！" id _102_0398
    show Cerydra smile with dissolve
    show Regent smile at right with dissolve
    Regent "......呵......讲得好，我亲爱的“刻律德菈”。" id _102_0399
    Regent "我教导你的言辞，至少没有白费。" id _102_0400
    Regent "看看你......我的好孩子。" id _102_0401
    Regent "为了这场名为“正义”的表演，昨夜定是彻夜未眠吧？怎么手上还沾着朱笔的墨迹？" id _102_0402
    Regent "以前我叫仆人给你擦手的时候，你还总是嫌麻烦。怎么，离开了我，这点小事都顾不上了？" id _102_0403
    Cerydra "哈......时至今日，我仍愿意尊你一声吾师。" id _102_0404
    show Cerydra normal with dissolve
    Cerydra "帝国内乱，我远离皇室，流落在外。是你认出了我的血统，助我重归王座。" id _102_0405
    Cerydra "没有你那些年的“栽培”，就没有现在站在这里的刻律德菈。" id _102_0406
    Cerydra "因此，我赐你火刑，免于死后被分列于城墙上，供往来旅人观赏。" id _102_0407
    show Cerydra sneer with dissolve
    Cerydra "然而，私恩已偿，公罪难逃。" id _102_0408
    Cerydra "既然你教会了我权术的残酷，那我便用这残酷——为你送葬。" id _102_0409
    show Cerydra smile with dissolve
    Regent "虽然结局有些意外......不过，能死在自己最得意的作品手里，总好过死在那些庸碌的蠢货刀下。" id _102_0410
    Regent "这盘棋，是你赢了，陛下。" id _102_0411
    Regent "唯有一事，我至死难安。塔兰顿的铁律不可违逆，你究竟付出了什么......才换来了那身流淌的黄金？" id _102_0412
    Cerydra "哈......你想知道神明是如何低头的么？" id _102_0413
    Cerydra "既是最后一问，我便让你看个明白。" id _102_0414
    Cerydra "想必你已听闻——行军途中，我曾进入三相神殿，面见塔兰顿。" id _102_0415

    scene bg FateTemple_law_room with fade
    show Cerydra normal at left
    show Talanton light at right
    with dissolve




    Talanton "此地不欢迎僭越之人。" id _102_0416
    Cerydra "我以许珀耳女皇的身份站在这里，何来僭越？" id _102_0417
    Talanton "谎言重复千遍，也无法成为真理。" id _102_0418
    Talanton "一个被推上台前的傀儡，一片用谎言编织的泡沫。我已经拒绝过你，人子。" id _102_0419
    show Cerydra angry_wocrown with dissolve
    Cerydra "看看外面！我的士兵在流血，我的国家在燃烧！" id _102_0420
    Cerydra "而你，所谓的律法之神......躲在废墟里，守着你失序的规矩腐烂！" id _102_0421
    show Cerydra normal_wocrown with dissolve
    Cerydra "不错，我是僭主。那么，告诉我——" id _102_0422
    show Cerydra angry_wocrown with dissolve
    Cerydra "是谁在统领这支军队？是谁在必败的战局里撑到现在？" id _102_0423
    Talanton "......人子......野心。" id _102_0424
    Talanton "汝昨日冒名称王，今日便要走入死地。如今，汝请求金血......" id _102_0425
    show Cerydra normal_wocrown with dissolve

    Talanton "汝可曾预料，汝将付出何等代价？" id _102_0426
    Cerydra "代价？没有比失败更可怖的代价。" id _102_0427
    Cerydra "不错，上次我向你请求，只是为了摆脱乞儿的无力，为了活下去......" id _102_0428
    show Cerydra angry_wocrown with dissolve

    Cerydra "然而今日......我已为王！" id _102_0429
    Cerydra "我不为苟活，只为扭转这不公的世界！" id _102_0430




    show Cerydra normal_wocrown with dissolve
    Talanton "......" id _102_0431
    "巨大的天平缓缓转动，发出沉闷的轰鸣。它倾斜，摇摆......" id _102_0432

    scene black with fade

    Unknown_Khaos "我已将之分给你们。" id _102_10002
    Unknown_Khaos "自今夜起，我的血便是你们的血，你们的痛亦是我的痛。" id _102_10003
    Unknown_Khaos "黄金的河流将漫过你们的脉搏，流经你们的心脏，成为力量的源头。" id _102_10004
    Unknown_Khaos "我们将并肩前行......哪怕脚下是深渊，头顶是长夜。" id _102_10005
    Unknown_Khaos "——直到我们夺回明天，点燃黎明。" id _102_10006

    scene bg FateTemple_law_room with fade
    show Cerydra normal at left
    show Talanton light at right
    with dissolve

    Talanton "人子，吾已称量汝的决心。契约已成。" id _102_0433
    Talanton "命运的馈赠......皆有代价。汝之代价......尚未示现。" id _102_0434
    Talanton "汝将不再生长。" id _102_0435
    Talanton "汝将为......律法的奴隶，直到......被自己的野心吞噬。" id _102_0436


    show cg p1_ch2_Cerydra_high with Fade(1.0, 1.0, 1.5)


    Regent "哈......是我低估了你的疯狂，我的孩子......" id _102_0437
    Regent "既然泰坦都被你折服，输给你......倒也不算辱没了我的名声。" id _102_0438
    Regent "动手吧。别让犹豫毁了这完美的谢幕。" id _102_0439
    "民众" "杀了她！火刑！杀了她！" id _102_0440
    "民众" "凯撒！凯撒！凯撒！" id _102_0441

    scene black with Fade(1.0, 2.0, 2.0)
    "这是她赢下的第一盘棋。" id _102_0443
    "新王俯瞰着台下。万千臣民俯首，漆黑的大地上燃起星火，如同天上星河。" id _102_0444
    "胜者亦是败者。" id _102_0445
    "无人能够真正掌控命运。" id _102_0446

    Cerydra "除非——你愿为之献祭所有。" id _102_0447

    stop music fadeout 2.0

    scene black with fade
    jump p1_ch3
return

