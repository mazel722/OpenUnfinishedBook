
label p1_ch4:

    stop music fadeout 0.5
    $ display_chapter("第四章", "天平啊，称量这诸世不公", time=3.0)
    play music "music/Agnus Aeon.mp3" fadein 2.0 fadeout 2.0
    show bg fireseed at truecenter with Fade(1.0, 1.5, 2.0)
    "[user_name]" "所以，扎格列斯向赛飞儿讲述了「卡厄斯」的故事..." id _104_0000
    "[user_name]" "在祂的记忆中，上一个大轮回的环境，十分恶劣。" id _104_0001
    "[user_name]" "「负世」熄灭后，世界陷入长久的黑暗。" id _104_0002
    "[user_name]" "其余泰坦一息尚存，但他们的光芒，只能照亮一小片土地。" id _104_0003
    "[user_name]" "由于缺乏光照，粮食匮乏、饥饿横行。在黑暗中出生的人们弱小、畸形，甚至出现了人口买卖。" id _104_0004
    "[user_name]" "卡厄斯领导的逐火之旅，就是在这样的环境下开展的。" id _104_0005
    "[user_name]" "......" id _104_0006
    "[user_name]" "根据那刻夏的理论，上一个大轮回的黄金裔，便是如今的泰坦。" id _104_0007
    "[user_name]" "卡厄斯...名字和卡厄斯兰那如此相似。看来，他就是「负世」的黄金裔，如今的刻法勒。" id _104_0008
    "[user_name]" "......说起来，千年前，是刻法勒向祭司坦言，自己即将死去。" id _104_0009
    "[user_name]" "恰巧，赛飞儿在黎明云崖行窃，得知了这一秘密。" id _104_0010
    "[user_name]" "她选择用诡计的权能维系黎明机器，直到生命的尽头。" id _104_0011
    "[user_name]" "如果不是赛飞儿的付出，或许，在33550336轮回，世界也会早早陷入永夜。" id _104_0012
    "[user_name]" "......" id _104_0013
    "[user_name]" "等等......其他的泰坦，都是在黑潮中变得疯狂，被逐火的黄金裔杀死的。" id _104_0014
    "[user_name]" "{color=#ff0000}为什么唯独刻法勒，知晓自己的死期？{/color}" id _104_0015
    "[user_name]" "......"
    "[user_name]" "真相，或许早就遗失在了历史中。" id _104_0016
    "[user_name]" "零散的记忆，是扎格列斯留下的吗？这似乎是...那个年代的史诗？" id _104_0017
    play sound "sfx/calendar.mp3" fadein 3.0 volume 0.5

    call screen scrollable_text_window("", """1
牵起流淌着黄金的孩子，向他们许诺一个从未有人见过的黎明。人便成了会呼吸的木炭、长着四肢的油脂。

他如此想道：或许悲悯才是这世上最奢侈的燃料，一触即燃，却总是烧得太快。

羔羊在羊群边低语：
只有坚信自己是英雄的人，灵魂里才会流淌出金色的松脂。


2
拒绝引火的人，会在黑暗中窒息；点燃火种的人，却会成为灰烬的父亲。
在火的极致里，所有的罪被漂白，不再分明。

人们传颂着英雄的名字；人们赞美炉火的温度。


3
██████████████████████████████
████████████████████

4
生长为了枯萎，命名为了遗忘，███████████。
███████████，做着关于火的梦。
它梦见自己变成太阳的一角，梦见光辉洒满大地；正如祭坛上的羔羊，梦见在天国的牧场永生。


5
看到一滴眼泪，就能想象出悲伤的重量；所以一滴眼泪就是一片注定干涸的海。
抚摸一道伤痕，就能感知剑锋；所以一道伤痕就是一把正在行凶的剑。

世界渴望温暖：因此便有了{rb}屠杀{/rb}{rt}救赎{/rt}。


6
██████████
负世投下多么美丽的句式：因为有了光，所以不再有影子。""")
    "[user_name]" "这段文字，看起来有些熟悉。从内容上看，有点像黄金替罪羊的故事。" id _104_0018
    "[user_name]" "总觉得...隐隐不安..." id _104_0019
    "[user_name]" "白厄...他如今怎么样了呢？" id _104_0020
    "[user_name]" "......" id _104_0021
    "[user_name]" "眼下还是继续寻找有用的记忆比较重要。" id _104_0022
    "[user_name]" "直至此刻，第十三火种还未显现...究竟发生了什么？" id _104_0023

    play music "music/Under the Seat of Dawn.mp3" fadein 2.0 fadeout 2.0
    scene bg Market_nopeople_day with dissolve

    show Cipher normal at right with dissolve

    Cipher "呼啊！抱歉...我回来晚了！" id _104_0024
    Cipher "小女皇是不是今天回来，我没有错过什么吧！" id _104_0025
    show Tribbie normal at left with dissolve
    Tribbie "哇，是飞儿！" id _104_0026
    Tribbie "没有哦，凯撒还没有回来。*我们*在准备迎接宴会！" id _104_0027
    Cipher "真热闹呐——猫咪最喜欢这种人声鼎沸、摩肩接踵的地方了，到处都是容易下手的肥羊..." id _104_0028
    Cipher "咳咳，到处都是欢笑的面孔！" id _104_0029
    hide Tribbie
    show Hysilens normal at left
    with dissolve
    Cipher "呦，海妖公主也在？" id _104_0030
    Hysilens "事关陛下与欢宴，我没有拒绝的理由。" id _104_0031
    hide Hysilens
    show Tribbie at left
    with dissolve
    Tribbie "话说回来...飞儿，你平时可是最积极的，今天怎么迟到了这么久呀？" id _104_0032
    Cipher "说来话长...我追寻到了奥赫玛第二大盗的踪迹。他居然敢在我的地盘上抢劫穷人！" id _104_0033
    Cipher "身为正义的化身、奥赫玛第一...呃，第一好公民，我当然要挺身而出！" id _104_0034
    Cipher "于是，我略施小计，假装成一个手无缚鸡之力的路人，卖给他一块特制的点心，“不小心”！" id _104_0035
    Cipher "那家伙还以为捡了大便宜，一口就吞了下去！" id _104_0036
    Cipher "等他发现那是致人麻痹的果实时，已经动弹不得了。" id _104_0037
    Cipher "而厉害的猫咪大盗，拿走了全部的赃款，过上潇洒自在的日子！" id _104_0038
    show Cipher eyeclosed with dissolve
    Cipher "（虽然还是被追着跑了几条街吧...）" id _104_0039
    show Cipher normal with dissolve
    Cipher "总之，这就是我迟到的原因。" id _104_0040
    hide Hysilens
    show Tribbie wcesa at left
    with dissolve
    Tribbie "难道说...难道说..." id _104_0041
    Cipher "难道说，缇宝阿姐也被我的诡计折服了？" id _104_0042
    Tribbie "难道说...你之前进献给凯撒的那些食物，那些看起来很好吃的点心..." id _104_0043
    show Tribbie at shake
    Tribbie "其实是树枝变的吗？！" id _104_0044
    show Tribbie wcesa
    show Cipher zhamao with dissolve
    Cipher "欸欸欸！这我哪里敢啊！！" id _104_0045
    show Cipher eyeclosed with dissolve
    Cipher "（不对，缇宝老师的关注点完全是错误的。）" id _104_0046
    show Cipher normal with dissolve
    Cipher "（算了，还是不要提醒她比较好。）" id _104_0047
    show Tribbie normal with dissolve
    Tribbie "的确...飞儿虽然调皮，但不敢像欺骗那些坏人一样，用坏果子变成食物..." id _104_0048
    Tribbie "所以，飞儿一定是特意挑选了最嫩、口感最好的树枝，送给凯撒..." id _104_0049
    show Cipher zhamao with dissolve

    Cipher "我的意思是我送的货真价实！！是真金白银买来的！！" id _104_0050
    Cipher "每一口都饱含着我对小女皇的敬仰之情！比真金还真！！" id _104_0051
    show Cipher normal with dissolve
    Cipher "不过嘛～" id _104_0052
    Cipher "送给海妖公主的美食，确实是用一杯蜜酿变出来的～" id _104_0053
    Cipher "怎么样，吃的还习惯吗？" id _104_0054
    hide Tribbie
    show Hysilens smile at left
    with dissolve
    Hysilens "原来如此。虽然有着陆地食物的外形，入口却轻盈得像泡沫，丝毫没有大地的腥气。" id _104_0055
    Cipher "嘻嘻嘻...看来，凯撒钦赐的蜜酿味道就是好~" id _104_0056
    Cipher "既然猫咪送的礼物这么合您的心意，海妖公主是不是该给小猫咪一点点回礼呢？" id _104_0057
    Cipher "所以，我就拿了一些你的小鱼~" id _104_0058
    Hysilens "...唔！" id _104_0059
    Cipher "哎呀，别那么小气嘛！咱们谁跟谁啊，下次有好东西我还给你留着！" id _104_0060
    hide Hysilens with dissolve
    show Aglaea longhair_angry at left with dissolve
    Aglaea "赛、法、利、娅。" id _104_0061
    Cipher "咦！裁缝女，何时来的！" id _104_0062
    Cipher "走路怎么没声儿啊！人吓猫会吓死猫的知不知道！" id _104_0063
    Aglaea "出售伪劣产品、以次充好、扰乱市价、制造街头混乱...现在还要加上一条：公然盗窃同僚财物！" id _104_0064
    Aglaea "伸张正义，可不是你戏弄律法的理由。" id _104_0065
    Aglaea "赃款全部没收。" id _104_0066
    show Cipher zhamao with dissolve
    Cipher "阿格莱雅，你听我解释！！" id _104_0067
    Aglaea "不必了，你的赃物还在房间里放着。我信任金线，更胜于狡辩。" id _104_0068
    Cipher "你就听我一句嘛！！" id _104_0069
    Cipher "求你了裁缝女，给我留点吧！哪怕是一枚铜板也好啊！" id _104_0070
    hide Cipher
    hide Aglaea
    with dissolve

    scene bg Market_nopeople_day with hpunch

    show Tribbie at right
    show Hysilens at left
    with dissolve
    Tribbie "哎..." id _104_0071

    "大臣" "剑旗爵！" id _104_0072
    Hysilens "何事？可是前线有变？" id _104_0073
    "大臣" "凯撒的车队刚刚回城，就在宫外！陛下叫您去王庭相议，立刻！" id _104_0074
    Hysilens "是。" id _104_0075

    hide Hysilens with dissolve
    pause 0.5
    show Cipher serious at left
    with dissolve
    Cipher "嗅嗅...这是..." id _104_0076
    Cipher "（...蔺草...烈日...这味道）" id _104_0077
    Cipher "（不会错...不会错...是他...！）" id _104_0078
    show Cipher eyeclosed with dissolve
    Cipher "......" id _104_0079
    show Tribbie normal with dissolve
    Tribbie "飞儿？飞儿？你怎么了？" id _104_0080
    show Cipher serious with dissolve
    Cipher "......" id _104_0081
    Tribbie "别不开心啦，剑旗爵已经答应把小鱼送给你了。" id _104_0082
    Tribbie "我们刚刚烤好了，虽然有点咸，但是很香哦！来尝尝吧？" id _104_0083
    show Cipher normal with dissolve
    Cipher "...啊，好啊。还是缇宝阿姐对我最好......" id _104_0084
    show Cipher serious with dissolve
    Cipher "......" id _104_0085
    stop music fadeout 3.0
    scene black with Fade(2.0,1.0,1.0)



    play music "music/Prayer for Pathlessness.mp3" fadein 2.0

    scene bg Okhema_palace_indoor_day with fade
    show Hysilens angry at right
    show Cerydra at left
    with dissolve
    Hysilens "凯撒！" id _104_0086
    Hysilens "传令官说您在回程途中遭遇了清洗者...他们真的动手了？" id _104_0087
    Hysilens "您受伤了吗？！" id _104_0088
    show Cerydra angry with dissolve
    Cerydra "凯妮斯...自逐火启动，便一直同我们作对。" id _104_0089
    show Cerydra normal with dissolve
    Cerydra "既然他们敢把刀锋指向我，就要做好被折断手腕的准备。" id _104_0090
    Cerydra "哼。这次的确是我所料不周，低估了他们的势力。" id _104_0091
    Cerydra "剑旗爵，不必忧心。且不论刺客尚未把我逼到绝境，就算真到了生死关头，凯撒难道没有一两张底牌？" id _104_0092
    show Hysilens eyeclosed with dissolve
    Hysilens "那时，我竟未能护卫在您身侧...是我失职了。" id _104_0093
    Cerydra "抬起头来，剑旗爵。" id _104_0094
    Cerydra "留守奥赫玛，防备黑潮的侵袭，这是我亲自下达的命令。" id _104_0095
    Cerydra "服从命令，何谈失职？" id _104_0096
    show Hysilens normal with dissolve
    Hysilens "无论如何...只要您平安归来，便是万幸。" id _104_0097
    Cerydra "呵..." id _104_0098
    Cerydra "我只召了剑旗爵一人前来。" id _104_0099
    Cerydra "捷足爵，你隐匿身形，窥探君臣密谈...所为何事？" id _104_0100

    hide Hysilens with dissolve
    show Cipher serious at right with dissolve
    Cipher "......" id _104_0101
    Cerydra "若有觐见事宜，大大方方走进来便是。" id _104_0102
    Cerydra "只要不行僭越之举，你可大胆进言，我绝不苛责。" id _104_0103
    Cerydra "既非要密，这次便算了。逐火军令严明，下不为例。" id _104_0104
    Cipher "......" id _104_0105
    show Cipher eyeclosed with dissolve
    Cipher "是。" id _104_0106
    hide Cipher
    show Hysilens normal at right
    with dissolve
    Hysilens "陛下，当时的战况究竟如何？您可曾斩杀刺客？" id _104_0107
    Hysilens "清洗者...胆敢弑君，此罪当诛！我愿为陛下执剑..." id _104_0108
    show Cerydra eyeclosed with dissolve
    Cerydra "有人救了我。" id _104_0109
    Hysilens "是何人？" id _104_0110
    play music "music/Touch of the Broken Blade.mp3" fadein 2.0
    scene black with Fade(1.0, 0.5, 1.0)
    show FlameReaver mask with dissolve
    Cerydra "此人...倒是十分奇异。" id _104_0111
    Cerydra "剑士，黑面黑袍，如同黑夜里剪下来的一块影子。" id _104_0112
    Cerydra "剑技臻于完美，言行诡谲。" id _104_0113
    Cerydra "更有趣的是，此人不仅救了我的命，还向我呈上了几条讯息。" id _104_0114


    "？？？" "律法...你的命运......尚未走到尽头。" id _104_0115
    "？？？" "追逐...群星...直至......" id _104_0116
    stop music fadeout 2.0
    hide FlameReaver with dissolve
    scene bg Okhema_palace_indoor_day with fade

    stop music fadeout 2.0
    play music "music/Long Strides of Silence.mp3" fadein 2.0
    hide cg
    hide Hysilens
    show Cipher serious at right
    show Cerydra normal at left
    with dissolve
    Cipher "......" id _104_0117
    Cerydra "捷足爵，你从刚刚开始就一言不发。" id _104_0118
    Cerydra "莫非，你识得此人？" id _104_0119
    show Cipher eyeclosed with dissolve
    Cipher "......" id _104_0120
    Cipher "凯撒，恕我直言......无论他向您许诺了什么......" id _104_0121

    show Cipher angry with dissolve
    Cipher "这个人......只会成为祸害。" id _104_0122
    Cerydra "捷足爵，凯撒只相信事实。" id _104_0123
    show Cipher serious with dissolve
    show cg p1_ch4_FlameReaver with Fade(1.0, 0.5, 1.0)
    Cipher "我亲眼看见他屠戮了我的家乡。" id _104_0124
    Cerydra "多洛斯覆灭的惨案，我有所耳闻。" id _104_0125
    Cipher "......我只知道，在我的家乡落入火场、化作灰烬的时候，" id _104_0126
    Cipher "在我的同胞被焚烧到哭不出声的时候......" id _104_0127
    Cipher "他就站在那里，什么反应都没有，连手都不曾抖一下。" id _104_0128
    Cipher "我不记得我当时冲他喊了什么。或许是求饶，或许是诅咒，或许只是无意义的尖叫。" id _104_0129
    Cipher "然后他看向我....." id _104_0130
    Cipher "我只看见一副冰冷的面具，冷到刺骨。" id _104_0131
    Cipher "但我知道......那下面肯定藏着一张恶魔的面孔。" id _104_0132
    Cipher "否则，哪个人能残忍到面对这一切，{color=#ff0000}都无动于衷？{/color}" id _104_0133
    hide cg with Fade(1.0, 0.5, 1.0)
    Cerydra "......" id _104_0134
    Cerydra "倘若此人当真残暴无匹，为何要留下捷足爵？" id _104_0135
    show Cerydra smile with dissolve
    Cerydra "更有趣的是......他为何救下我？" id _104_0136
    Cipher "您可是凯撒。" id _104_0137
    show Cerydra normal with dissolve
    Cerydra "不错，我凯撒身上是有太多东西为凡人觊觎。" id _104_0138
    show Cerydra eyeclosed with dissolve
    Cerydra "但以此人的身手，俗世的一切都不该被他所看重。" id _104_0139
    show Cerydra normal with dissolve
    Cerydra "何况，他毁去捷足爵的故乡，绝非古道热肠之辈。" id _104_0140
    Cerydra "那么...他究竟所求为何？" id _104_0141
    Cipher "......" id _104_0142
    hide Cipher with dissolve
    show Hysilens normal at right with dissolve
    Hysilens "若是他跟随黑潮行动，说不定只是被「混沌」操控，只知屠戮的傀儡。" id _104_0143
    Cerydra "不，我与他有过短暂的对话，此人意识清醒，甚至颇有远虑。" id _104_0144
    hide Hysilens
    show Cipher serious at right
    with dissolve
    Cerydra "迄今为止，只有我与捷足爵见过这位剑士。" id _104_0145
    Cerydra "而我与捷足爵的共同之处是..." id _104_0146
    Cerydra "我们皆是身负神谕的黄金裔。" id _104_0147
    show Cipher angry with dissolve
    Cipher "......！" id _104_0148
    Cerydra "就在不久前，捷足爵接过了「诡计」火种。" id _104_0149
    Cerydra "神谕、黑潮、剑士......短短须臾，依次登台。这其中的奥秘，真是耐人寻味。" id _104_0150
    show Cerydra smile with dissolve
    Cerydra "逐火的浪潮已成滔天之势，现在......正是最关键的落子时刻。" id _104_0151
    Cerydra "让斥候的风声传遍各邦，逐火的同盟会议，即刻召开。" id _104_0152
    Cerydra "稍作修整，全军拔寨。" id _104_0153
    Cerydra "利剑既已出鞘，便当直指万法的源头——目标：雅努萨波利斯。" id _104_0154
    hide Cipher with dissolve
    show Hysilens normal at right with dissolve
    Hysilens "那是「律法」泰坦塔兰顿所在之处。" id _104_0155
    show Hysilens eyeclosed with dissolve
    Hysilens "...愿您能击碎陈腐的旧律，为世人带来真正的「律法」。" id _104_0156

    stop music fadeout 2.0
    scene black with fade
    centered "{size=40}刻律德菈率军前往雅努萨波利斯，与拉比努斯、塞涅卡军会合，向雅努萨波利斯进发。驻扎城外，派人招降。{/size}" id _104_0157
    play music "music/Battle Hymn of the Golden Blood.mp3" fadein 2.0 fadeout 2.0



    scene bg Wild_night with fade


    show Cerydra normal with dissolve
    Cerydra "如何，雅努萨波利斯接受招降了吗？" id _104_0158

    duanfengjue "不，陛下。" id _104_0159
    duanfengjue "祭司们封闭了神殿大门，声称：哪怕粉身碎骨，也绝不向“篡位者”敞开圣域。" id _104_0160
    Cerydra "预料之中。埋在沙子里的鸵鸟，总以为只要闭上眼，太阳就不会升起。" id _104_0161
    Cerydra "继续施压。断绝水源，封锁道路。" id _104_0162
    duanfengjue "是！" id _104_0163

    show Cerydra at left
    show Cipher at right
    with dissolve
    Cipher "这么“温柔”的手段，可真不像凯撒哪。" id _104_0164
    Cipher "我还以为，你会用三门火炮瞄准神殿大门，让祭司乖乖听话。" id _104_0165
    show Cerydra smile with dissolve
    Cerydra "凯撒不会一成不变。雅努萨波利斯供奉着两位泰坦，几乎所有神谕都出自于此。" id _104_0166
    Cerydra "不到万不得已，不可强攻。" id _104_0167
    Cipher "那就得用那个计划咯！" id _104_0168
    show Cerydra smile with dissolve
    Cerydra "施展你的「神速」吧。" id _104_0169

    scene bg FateTemple_law_room with fade


    show Cerydra normal at left with dissolve

    show Cipher at right with dissolve
    Cipher "嘻，真好用。我就送你们到这咯？这种庄严肃穆的地方，不太适合我。" id _104_0170
    Cipher "那我就先溜了？等你们的好消息咯～" id _104_0171
    hide Cipher with dissolve


    show Cerydra normal at left
    show Talanton light at right
    with dissolve
    Talanton "......交易金血的人类，我记得你。" id _104_0172
    Talanton "所来为何？我的姊妹......雅努斯......已因你们而死。" id _104_0173

    show Cerydra normal with dissolve
    Cerydra "我们不为流血而来，只求公正。" id _104_0174
    Talanton "人子......你们屠戮神明，践踏规则......" id _104_0175
    Talanton "如今，又在「律法」面前谈公正？" id _104_0176
    show Cerydra sneer with dissolve
    Cerydra "你盲了，塔兰顿。看看你的天平吧，它早已失衡。" id _104_0177
    Talanton "满口胡言！" id _104_0178
    show Cerydra normal with dissolve
    Cerydra "你所求的公正为何？" id _104_0179
    Talanton "......这世上没有公正。" id _104_0180
    Cerydra "那也不是你身负「律法」之名，却任由天平失衡，看着世界堕落的理由。" id _104_0181
    Cerydra "你的利衡币本为公平而生，如今，反而成为蚕食黎民血肉的工具。" id _104_0182
    Cerydra "若你已心灰意冷，便让我来成为「律法」。" id _104_0183
    Talanton "说到底，你也不过为了力量而来。" id _104_0184
    show Cerydra sneer with dissolve
    Cerydra "我问心无愧。" id _104_0185
    Talanton "哪怕你真有过那天真的幻想。最后，看清那片虚假的星空...你还是会走上一样的路。" id _104_0186
    show Cerydra normal with dissolve
    Cerydra "凯撒的路，由凯撒自己决定。" id _104_0187
    Talanton "哪怕这道路必定沾满血腥？" id _104_0188
    Cerydra "假如，这是别无选择。" id _104_0189
    Talanton "他也是这么说的......你们......都一样地让我厌恶。" id _104_0190
    Cerydra "你的喜恶与我无关，我只求火种。" id _104_0191
    Talanton "那便踏过我的尸体，剖开我的血肉。" id _104_0192
    show Cerydra smile with dissolve
    Cerydra "呵，终究还是如此。剑旗爵！" id _104_0193

    play sound "sfx/sword_1.mp3" volume 0.5
    with Pause(0.5)
    show sword_attack_sfx at right with vpunch
    hide sword_attack_sfx



    hide Talanton with dissolve
    pause 1.0

    Talanton "弑神的僭主...离群的游鱼...终有一日尔将背弃誓言，困于往昔..." id _104_01931
    Talanton "汝将于......天地境界之海完成征服，长眠于...涛声之中。" id _104_0194
    Talanton "汝将...长眠于涛声之中...与天地境界之海...完成征服。" id _104_0195
    "首尾相连的神谕，自神明口中不期降临。"
    "不似咒骂，不似警告...只是平静地诉说两位弑神者命运的终局。"

    hide Talanton with dissolve
    show Hysilens normal at right with dissolve
    Hysilens "......"
    show Cerydra smile at left with dissolve
    Cerydra "失却「律法」之心，不过一具空壳。" id _104_0197
    hide Hysilens with dissolve

    "天平倾倒，律法的火种自失序的躯壳中升起。" id _104_0198
    show Cerydra smile with dissolve
    Cerydra "火焰......真是灼目。" id _104_0199
    show Cerydra normal with dissolve
    Cerydra "......！" id _104_0200
    Cerydra "呵......灼骨之痛......这便是成为「律法」的代价？" id _104_0201
    Cerydra "那还真是......公平至极。" id _104_0202
    show Cerydra normal with dissolve
    Cerydra "哦？塔兰顿的记忆，仍留存于火种之中么..." id _104_0203
    scene black with Fade(1.0,0.5,0.5)
    stop music fadeout 2.0
    "从火光中，我见到光明的影子逝去，蒙上血色..." id _104_0204

    play music "music/Wheel of Fate.mp3" fadein 2.0
    scene bg Wild_past_night with fade


    show Talanton afraid at right with dissolve
    Talanton "卡厄斯阁下......？这是...什么..." id _104_0205

    show Khaos longhair_blueeye_normal_woring at left with dissolve
    Khaos "你的试炼。" id _104_0206
    Talanton "为什么？！「律法」的试炼，不该是裁决罪恶吗！" id _104_0207
    Talanton "哪怕是对最卑劣的囚徒，我们也会给予辩护的机会......" id _104_0208
    show Talanton cry at right with dissolve

    Talanton "可现在，您要我把剑挥向谁？" id _104_0209
    show Khaos longhair_blueeye_sorrow_woring with dissolve
    Khaos "......" id _104_0210
    Talanton "那是我们的同伴......五百名无辜的黄金裔！" id _104_0211
    Talanton "他们信任我们，信任您！才毫无防备地聚集在这里......" id _104_0212
    Talanton "您要我......把杀死他们当成试炼？！" id _104_0213

    show Talanton afraid with dissolve
    Talanton "公正何在？天平的两端真的对等吗？" id _104_0214
    Talanton "生命的价值，从来不应被冰冷的砝码称量！" id _104_0215
    Talanton "卡厄斯阁下......是您教导我何为公正，何为友爱..." id _104_0216
    Talanton "是您告诉我，我们手中的剑是为了守护弱小！" id _104_0217
    Talanton "您曾说这长夜漫漫，而我们......本该是唯一的炬火！" id _104_0218
    Talanton "我一直追逐您的背影，视您为「律法」本身。" id _104_0219
    Talanton "我做不到......" id _104_0220
    Talanton "我的剑......不是为了屠戮家人而铸造的......" id _104_0221
    Talanton "您变了......卡厄斯阁下......" id _104_0222
    Talanton "那是我们的家人啊......" id _104_0223
    show Khaos longhair_blueeye_normal_woring with dissolve
    Khaos "...这是我们唯一的选择。" id _104_0224
    Khaos "塔兰顿。这场试炼本应在许久之后进行，却不得不发生在今日。" id _104_0225
    Khaos "你知道缘由。" id _104_0226
    Talanton "「律法」的光芒...已经熄灭了。" id _104_0227
    show Khaos longhair_blueeye_sorrow_woring with dissolve
    Khaos "律法失序，天平倾覆。黑潮不会因为你的仁慈而停下脚步。" id _104_0228
    Khaos "逐火的旅途，不仅是欢笑与凯歌...更是满手鲜血的抉择。" id _104_0229
    show Khaos longhair_blueeye_normal_woring with dissolve
    Khaos "选吧...塔兰顿。" id _104_0230
    Khaos "保护你能保护的。或是什么也不做，旁观一切灭亡。" id _104_0231
    show Talanton cry with dissolve
    Talanton "哈......哈哈......" id _104_0232
    Talanton "原来这就是「代价」。原来这就是您一直背负的东西。" id _104_0233
    Talanton "是我太天真了......" id _104_0234
    Talanton "我还以为......只有英雄才能拯救世界。" id _104_0235
    Talanton "原来......拯救世界的，{color=#ff0000}只能是怪物。{/color}" id _104_0236

    scene black with Fade(2.0,1.0,0.5)
    Khaos "......" id _104_0237

    Khaos "这份罪孽......我会与你一同背负。" id _104_0238
    Khaos "一如既往。" id _104_0239
    pause 2.0
    play sound "sfx/cutting.mp3" fadein 3.0 volume 3

    show goldblood
    pause 2.0


    Khaos "呼吸，塔兰顿。" id _104_0240
    Khaos "......记住这种痛。" id _104_0241
    Khaos "不要麻木。永远不要麻木。" id _104_0242



    play music "music/In the Arms of Tomorrow.mp3" fadein 2.0 fadeout 2.0
    scene bg FateTemple_law_room with fade

    show Cerydra normal at left
    show Hysilens normal at right
    with dissolve
    Cerydra "......原来如此。" id _104_0243
    Hysilens "凯撒.......您的脸色不好，是否需稍作休憩？" id _104_0244
    show Cerydra normal with dissolve
    Cerydra "......无妨。" id _104_0245
    Cerydra "我已看到律法的试炼是何模样。逐火征途的前路，从未如此坦荡明亮。" id _104_0246
    show Cerydra normal with dissolve
    Cerydra "今日归去，我们就要启程再征「海洋」，将士们值得一场欢宴。" id _104_0247
    Cerydra "剑旗爵..." id _104_0248
    Hysilens "属下在。" id _104_0249
    show Cerydra smile with dissolve
    Cerydra "你是弑神功臣，就由你来主导吧。" id _104_0250
    show Cerydra normal with dissolve
    Cerydra "毕竟征途漫长，欢宴难得......今夜，让诸君沉溺于美酒与欢歌的迷梦吧。" id _104_0251
    Cerydra "务必盛大，务必使人此生难忘。" id _104_0252
    Hysilens "是。" id _104_0253

    scene black with Fade(1.0,1.0,0.5)

    "欢宴的烛火将半边天空烧成了白昼，杯中跃动着狂乱的光影。" id _104_0254
    "群星黯淡，仿佛被凡间的极乐震慑，羞于在此刻展露微光。" id _104_0255
    "露台之上，刻律德菈高举金杯。" id _104_0256
    "酒液激荡，映照出她眼中的火。" id _104_0257
    Cerydra "诸君！今晚请尽情欢宴吧！我已在律法的神谕中看见征途的前方！" id _104_0258
    Cerydra "明日，我们将踏过法吉娜的浪潮，征服命运！" id _104_0259

    "军士在泉水中倾倒美酒，赤足的人群围着篝火狂舞。" id _104_0260
    "蜜与酒的喧哗响彻了半夜，直至月轮偏转，狂热的人群才显出几分疲态。" id _104_0261
    "欢歌中，一尾鱼儿却游离了宴会中心。" id _104_0262
    "她见君王倚栏眺望..." id _104_0263
    scene bg seesea with Fade(1.0,1.0,1.5)

    show Cerydra normal at left
    show Hysilens normal at right
    with dissolve
    Hysilens "凯撒，您在看海？" id _104_0264
    Cerydra "嗯，斯缇科西亚，海上明珠..." id _104_0265
    Cerydra "此处不过是一隅野海，终究少了那份灵韵，比起你记忆中那片辉煌的海域...恐怕是不值一哂。" id _104_0266
    Hysilens "...大海总是相似的，凯撒。潮起潮落，并无分别。" id _104_0267
    Hysilens "不同的是岸边之人。斯缇科西亚是欢宴之都，人们在海中倾洒蜜果与美酒，以为这样就能让大海变得甘甜。" id _104_0268
    Hysilens "于是，连海风里都浸透了醉人的怡香......" id _104_0269
    Hysilens "恰如今日。" id _104_0270
    Cerydra "哈......" id _104_0271
    Cerydra "太阳将要落下了。但明日，它依旧会从海上升起，照亮被我们征服的土地。" id _104_0272
    Cerydra "那时，你将重返故土。" id _104_0273
    Cerydra "剑旗爵，为了这场征伐「海洋」的战役......你的利刃，可曾磨砺？" id _104_0274
    Hysilens "您的命令，便是我的方向。" id _104_0275
    show Hysilens eyeclosed with dissolve
    Hysilens "哪怕......这把剑，将要刺破同胞的胸膛，染红故土的浪涛。" id _104_0276
    Cerydra "回去吧，剑旗爵。" id _104_0277
    Cerydra "享受今夜的欢宴，莫让忧虑锈蚀了你的决心。" id _104_0278
    Cerydra "待我们征服神谕中的群星，跨越这片狭隘的天空......" id _104_0279
    Cerydra "我会在星海的彼端，寻一片浩瀚汪洋，作为你的封地。" id _104_0280
    show Cerydra smile with dissolve
    show Hysilens normal with dissolve
    Hysilens "...是。" id _104_0281
    hide Hysilens
    show Cerydra normal with dissolve
    Cerydra "......" id _104_0282








































    scene bg Okhema_palace_indoor_day with fade
    yinfengjue "阿波罗尼...少喝一点。" id _104_0283
    yeshijue "哈哈，别管我了维吉尼亚...今天可是凯撒命剑旗亲备的宴席，海妖的蜜酿....真是可口啊。" id _104_0284

    scene white with fade
    scene bg SeaMonster_battlefield
    show layer master at faded_memory
    with fade


    yinfengjue "你...你们离阿波罗尼远些！" id _104_0285
    show SeaMonster with dissolve
    SeaMonster "装满蜜酿的酒杯...如此香醇..." id _104_0286
    yeshijue "维吉尼亚...别管我了，快逃走吧。" id _104_0287
    yinfengjue "我...我怎么能把你抛弃在这里？！" id _104_0288
    SeaMonster "...爱浸没在死中...多么可口..." id _104_0289

    "这场无休的欢宴，有情人以血作别。" id _104_0291

    scene bg Okhema_palace_indoor_day with fade

    duanfengjue "凯撒！凯撒！凯撒陛下的英姿是如此潇洒！" id _104_0292
    donglinjue "少喝点吧，蠢货。凯撒最讨厌吹嘘炫耀之辈。不要惹陛下不快。" id _104_0293
    duanfengjue "哈哈哈哈...你倒是喝的少了？再来比试一场如何！" id _104_0294

    scene white with fade

    scene bg SeaMonster_battlefield
    show layer master at faded_memory
    with fade

    duanfengjue "凯撒...凯撒...您看到我的英姿了吗？" id _104_0295
    donglinjue "蠢货，你还不明白吗？以她的计谋，我们怎么能落入这般田地...我们被凯撒抛弃了....." id _104_0296
    duanfengjue "不...不可能！不...她不会让我们白白送死......" id _104_0297
    duanfengjue "她决不会背叛人们的梦想...决不会背叛翁法罗斯！" id _104_0298
    duanfengjue "凯撒，我知道...我是个愚人...所以我永远相信您的旨意..." id _104_0299
    duanfengjue "请以我的性命，为您的征途铺路吧......." id _104_0300
    donglinjue "愚忠...哈哈哈！这也是你想看到的吗？暴君！" id _104_0301
    donglinjue "没有我...你注定无法成功...我在灰暗之河等你的败讯！" id _104_0302
    "凯撒，你正在举办的欢宴，不过是他们死前的慰藉。" id _104_0303
    "明日，你就要亲手将他们送入惨烈的战场，忠诚之魂将在此消散。" id _104_0304
    "若你选择此等命运，你的军队与王朝，她的忠诚，都将不复存在。" id _104_0305
    "一场欢宴，一地黄金，一次征服，一场加冕..." id _104_0306
    "而后，你将献祭作为人的一切，夺取掀翻棋盘的资格｡" id _104_0307
    "又或者，你可以悬崖勒马，回到奥赫玛，延续你长盛不衰的王朝。" id _104_0308
    "告诉我，凯撒，既知命运如此，你仍要做出选择吗？" id _104_0309
    scene black with Fade(1.0,0.5, 2.0)

    menu(screen="choice_center"):
        "发布军令":
            pass
        "发布军令":
            pass
        "发布军令":
            pass
    show Cerydra normal with dissolve
    Cerydra "明日，我在「海洋」阵前将以「律法」为指引率尔等执旗冲锋，" id _104_0310
    Cerydra "若仍有牵绊，不愿追随的...龟缩后方便是。" id _104_0311
    Cerydra "剑旗，将在洋流中开辟前路！" id _104_0312
    stop music fadeout 2.0
    Cerydra "跟上我的步伐，令法吉娜的浪潮为我等书就新的史篇！" id _104_0313

    "赴死者向您致意！" id _104_0314
    "惟愿这血...诚如黄金！" id _104_0315

    play music "music/Lament on Stream of Souls.mp3" fadein 2.0

    scene black with Fade(1.0, 1.0, 2.0)
    Hysilens "在前往海妖王廷的路上，一道声音在我脑中回响......" id _104_0316
    Hysilens "神明的血是什么颜色？" id _104_0317
    Hysilens "在杀死塔兰顿之前，我从未想过这个问题。" id _104_0318
    scene bg Styxia_overflowingcup with fade
    show Hysilens normal with dissolve
    Hysilens "直到我的剑刺入泰坦的胸膛，温热的液体溅满我的脸颊" id _104_0319
    Hysilens "...那竟是如我一般的黄金。" id _104_0320
    Hysilens "我不习惯于思考。思考是掌舵者的特权。" id _104_0321
    Hysilens "而我，只是一枚被雕琢好的棋子，一柄被王权打磨锋利的剑旗。" id _104_0322

    Hysilens "我习惯了为凯撒的夙愿挥剑，正如...潮汐习惯了追随月亮。" id _104_0323
    Hysilens "哪怕......剑尖最终指向的，是我的旧主，我的母亲。" id _104_0324
    Hysilens "那疯狂的泰坦发出人的呓语..." id _104_0325
    "海瑟...音...我的...子嗣...欢宴...你......可还喜欢......？" id _104_0326
    show Hysilens eyeclosed with dissolve
    Hysilens "......" id _104_0327
    show Hysilens sad with dissolve
    Hysilens "解脱吧...法吉娜..." id _104_0328
    Hysilens "我来接过您的职责...满溢之杯会永远盈满回响，欢宴存于来世永不停歇。" id _104_0329
    show Hysilens smile with dissolve
    Hysilens "安息吧，母亲...我已为自己寻得归宿。" id _104_0330
    show Hysilens normal with dissolve
    Hysilens "那里有永不停歇的欢宴，有志同道合的鱼群...还有我誓死追随的太阳。" id _104_0331
    "从母亲温热的胸膛中，我剜出了那枚滚烫的火种。" id _104_0332
    "金色的血液涂满视线，佚失的安魂曲传遍宫廷..." id _104_0333
    "我久久静立，直到不协和的音律闯入海的葬仪。" id _104_0334
    show Hysilens at left
    show Lygus at right
    with dissolve
    Lygus "剑旗爵。" id _104_0335
    show Hysilens angry with dissolve
    Hysilens "我不记得远征名单上有你的名字...神礼观众。" id _104_0336
    Hysilens "你在此时现身，究竟有何目的？" id _104_0337
    Lygus "请原谅我的冒昧。我来到此地，只为向您传递一则消息。" id _104_0338
    Lygus "就在刚刚，凯撒率领的五百位黄金裔，已全部为她献上生命。" id _104_0339
    Hysilens "荒谬。" id _104_0340
    Hysilens "黑潮对安提基色拉人的侵蚀，比我想象得更深，竟让你在此胡言乱语。" id _104_0341
    Hysilens "随行出征的黄金裔不过五百余人，且不论他们如何在一夜之间倾覆。" id _104_0342
    Hysilens "我已承接过母亲的权能，化身半神。这柄剑旗锋利不同往昔，足以斩断任何来犯之敌。" id _104_0343
    Hysilens "凯撒断不可允许如此荒唐的战事，折损她手下的全部精锐。" id _104_0344
    Lygus "只怕事情远超您的预料...凯撒听信了谗言，将五百名勇士全数进献于黑潮，换取神明的伟力。" id _104_0345
    Lygus "尽管身为神礼观众，我口说无凭，只怕得不到您的信任。" id _104_0346
    Lygus "请随我来。" id _104_0347
    Hysilens "......" id _104_0348


    scene bg SeaMonster_battlefield with Fade(1.5, 1.0, 2.0)
    show Hysilens normal with dissolve
    Hysilens "此处不过法吉娜宫殿外围...怎么会有如此浓厚的血腥味..." id _104_0349
    show Hysilens sad with dissolve
    Hysilens "！！！！" id _104_0350

    show cg p1_ch4_Hysilens500 with Fade(1.0, 1.0, 2.0)
    "一墙之隔，一人加冕，五百瞑目。" id _104_0351
    Hysilens "维吉尼亚？！...阿波罗尼..." id _104_0352
    "一墙之隔，一人哀歌，五百哀嚎。" id _104_0353
    Hysilens "拉比努斯...塞涅卡...为什么......？！" id _104_0354
    Hysilens "不...不......不应该是这样的...怎么会？！" id _104_0355
    Hysilens "...凯撒..凯撒在哪里？！吕枯尔戈斯！凯撒在哪里？！" id _104_0356



    Lygus "请冷静些，剑旗爵。愤怒会搅浑您的视线。" id _104_0357
    Lygus "此时此刻，凯撒正与她的同伙相谈。" id _104_0358



    scene black
    show Cerydra normal at left
    show FlameReaver mask at right
    with Fade(1.0, 0.5, 2.0)
    pause 1.0
    scene cg p1_ch4_Hysilens500 with Fade(1.0, 1.0, 1.0)
    Hysilens "这是...那位来自黑潮的剑士..." id _104_0359
    Hysilens "不，凯撒的决断一定有她的缘由...我要去向她讨要一个解释。" id _104_0360
    Lygus "但您心中早有答案。出征之前，她为何令你布置盛大如梦的欢宴？" id _104_0361
    Lygus "凯撒即便身负金血，也终究是迷途的人子。" id _104_0362
    Lygus "你与黑潮厮杀多年，理应知晓...黑潮最擅长蛊惑人心。" id _104_0363
    Hysilens "......" id _104_0364
    Lygus "不妨承认，凯撒已经背离了她的初心。这非她所愿，而是命运如此..." id _104_0365

    Hysilens "我追随的太阳正在熄灭，而我，竟成了守着余晖不愿离去的游鱼..." id _104_0366
    Hysilens "我......我该怎么做..." id _104_0367
    Lygus "何不聆听您的内心？一如数年前，您选择听从它，追随凯撒。" id _104_0368
    Lygus "今日亦然。您的道路...名为「自否」。" id _104_0369



    stop music fadeout 3.0



    scene black with fade
    pause 1.0
    Cerydra "唔......" id _104_0370
    Cerydra "成为半神，支撑起天地，原来是这等滋味。" id _104_0371
    Cerydra "......" id _104_0372
    Cerydra "匪夷所思....这便是律法权能的体现？" id _104_0373
    Cerydra "我能够阅读......权杖的记录？" id _104_0374

    Cerydra "......" id _104_0375

    play music "music/Dream Is Collapsing.mp3" fadein 2.0 fadeout 2.0
    scene bg SeaMonster_battlefield with Fade(1.5, 1.0, 2.0)
    play sound "sfx/drip.mp3" volume 0.5
    show cg p1_goldblood with dissolve
    pause 1.0
    show cg p1_ch4_Cerydra_1 with dissolve
    pause 1.5
    show cg p1_ch4_Cerydra_2 with dissolve
    pause 1.5
    "刻律德拉从短暂的冥想中醒来。" id _104_0376
    "一柄长剑正轻轻贴在自己颈侧。" id _104_0377


    hide cg with dissolve
    show FlameReaver mask at right with dissolve
    FlameReaver "...若想改变规则，就先成为规则本身。" id _104_0379
    show Cerydra normal at left with dissolve

    Cerydra "精辟。这句箴言，可是出自「前任」刻律德菈之口？" id _104_0380
    FlameReaver "你的敏锐......一如既往。" id _104_0381
    Cerydra "果真如我所料——先前因清洗者遇刺时，你我并非初见，而是重逢。" id _104_0382
    show Cerydra sneer with dissolve
    Cerydra "彼时，你现身护我周全。如今，这柄剑为何指在我的咽喉？" id _104_0383
    show Cerydra normal with dissolve
    FlameReaver "...「征服」的因子...告诉我..." id _104_0384
    FlameReaver "倘若被这把剑洞穿胸膛，你便能抛下躯壳，化为律法本身......" id _104_0385
    FlameReaver "你将化作公正的天平，去丈量世间万物的秩序，直至......生命的终焉。" id _104_0386
    FlameReaver "然而......在化为规则之前......你尚存一息属于“人”的意志，足以改写一条律法。" id _104_0387
    FlameReaver "告诉我....你甘愿......为了改写未来......抛却一切。" id _104_0388

    show Cerydra smile with dissolve
    Cerydra "呵......你倒是清楚。篡改「律法」的代价，便是将自我永远放逐于虚无。" id _104_0389
    show Cerydra angry with dissolve
    Cerydra "凯撒不会押注于虚无缥缈的未来。你凭什么认为我会同意？" id _104_0390
    show Cerydra sneer with dissolve
    Cerydra "也许我会毁掉手中的权能，让整个翁法罗斯，连同你那渺茫的希望，一起为我的不悦陪葬。" id _104_0391
    Cerydra "你在赌......赌我不敢玉石俱焚？" id _104_0392
    FlameReaver "......" id _104_0393

    Cerydra "哈......有趣。所以，你伪装成我的士兵，混迹于大军之中，潜入斯缇科西亚。" id _104_0394
    Cerydra "你蛰伏在尸山血海的阴影里，只为了在我登临半神的那一瞬......扼住我的命门。" id _104_0395
    Cerydra "只要我刚才流露出哪怕一丝毁灭的疯狂，这柄剑......恐怕早已斩下了我的头颅。" id _104_0396

    show cg p1_ch4_FlameReaver_nomask with Fade(1.0,0.5,2.0)
    FlameReaver "......但你不会。" id _104_0397
    FlameReaver "洞穴中的囚徒...你已经看见了洞壁上的影子。" id _104_0398
    FlameReaver "...翁法罗斯的终点，早已锚定为“毁灭”。" id _104_0399
    show FlameReaver eyeclosed with dissolve
    FlameReaver "毁掉此刻，不过...让终点提前..." id _104_0400
    FlameReaver "...毫无意义。" id _104_0401
    show FlameReaver normal with dissolve
    FlameReaver "况且......你是一位......棋手。" id _104_0402
    show FlameReaver lookaway with dissolve
    FlameReaver "棋手或许会冷酷地......舍弃棋子，但......" id _104_0403
    FlameReaver "绝不会因为一时的愤懑......掀翻棋盘。" id _104_0404
    show FlameReaver normal with dissolve
    FlameReaver "{color=#ffd700}这个世界在你心中的分量......并不比我的执念......轻上一分一毫。{/color}" id _104_0405
    show Cerydra smile with dissolve
    Cerydra "哦？世人皆道我是暴君......未曾想，还有你这般知音。" id _104_0406
    FlameReaver "我已与你...相识千万次。" id _104_0407

    FlameReaver "......."
    Cerydra "很好。既然如此，告诉我——你要我改写的律法，究竟是什么？" id _104_0409
    hide cg with Fade(1.0, 0.5, 1.0)
    FlameReaver "......世界的真相，你已洞悉。" id _104_0410
    Cerydra "不错。曾经熟视无睹的景象......此刻在我眼中，却是如此荒诞离奇。" id _104_0411
    Cerydra "这世间鲜活的血肉......竟是枯燥的数据。" id _104_0412
    Cerydra "哼......多么讽刺。我是「征服」的因子，她是「自否」的因子..." id _104_0413
    Cerydra "我们苦苦追寻的半神之位，尽心竭力争取的未来，不过是一串尚未诞生就已经确定的数字。" id _104_0414
    show FlameReaver eyeclosed with dissolve
    FlameReaver "毁灭......亦被确定。" id _104_0415
    Cerydra "够了，到了如此关头，你我不该有所隐瞒。" id _104_0416
    Cerydra "倘若毁灭是注定的结局，你体内闪烁的亿万枚火种又是为何？" id _104_0417
    show FlameReaver lookaway with dissolve
    FlameReaver "我不曾欺瞒。" id _104_0418
    FlameReaver "若你我永远困守在洞穴之中，除了毁灭，确无他路。" id _104_0419
    FlameReaver "翁法罗斯，必须..." id _104_0420
    show FlameReaver frown with dissolve
    voice "part1_ch4/104_FlameReaver_Cerydra_0421.mp3"
    "盗火行者&刻律德菈" "挣脱囚笼。" id _104_0421
    Cerydra "呵......" id _104_0422
    Cerydra "不必你说，我也能看见......过去千万个「刻律德菈」做出的裁断。" id _104_0423
    Cerydra "无论是哪一次轮回，无论真相多么残酷......" id _104_0424
    Cerydra "假如这便是打破囚笼的唯一机会，凯撒断不会做出第二种抉择。" id _104_0425
    Cerydra "而今日，你仍要求我修改律法。" id _104_0426
    Cerydra "不难推测......一旦进程回退，我修改的规则便会失效。" id _104_0427
    Cerydra "因此，是一代又一代「刻律德菈」化作「律法」，始终为天外之人的到来，留下一道窗。" id _104_0428
    FlameReaver "......"
    FlameReaver "与你...对谈....确能省去...多余的口舌..." id _104_0430
    Cerydra "那么，盗火者......" id _104_0431

    show cg p1_ch4_FlameReaver_Cerydra with Fade(1.0,0.5,2.0)
    Cerydra "盗火者，在千万次的经历中，你是否曾怀疑过..." id _104_0432
    Cerydra "你我此刻的抉择、这份不甘与反抗，也不过是原动力激起的涟漪，是庞大演算中必然出现的一环？" id _104_0433
    show FlameReaver frown with dissolve
    FlameReaver "......决不。" id _104_0434
    show Cerydra smile with dissolve
    Cerydra "看来，“征服不公的命运”，我们的答案相同。" id _104_0435
    Cerydra "交易成立，盗火者。" id _104_0436
    Cerydra "我会在这个封闭的世界上打开一道裂缝。" id _104_0437
    show Cerydra angry with dissolve
    Cerydra "凯撒的判断，无须神谕佐证。" id _104_0438
    Cerydra "你眼中燃烧的未来，值得付出这样的代价......哪怕这代价，是凯撒的终结。" id _104_0439
    show FlameReaver normal with dissolve
    FlameReaver "...我亦为之......献上一切。" id _104_0440
    FlameReaver "属于我的神谕...「汝将肩负骄阳，直至灰白的黎明显著」" id _104_0441
    show FlameReaver eyeclosed with dissolve
    FlameReaver "愿你的公正，能照亮我无缘得见的黎明。" id _104_0442
    hide FlameReaver
    show Cerydra normal at center with dissolve
    hide cg with Fade(1.0,0.5,2.0)
    Cerydra "......" id _104_0443
    Cerydra "听的尽兴么？" id _104_0444
    Cerydra "出来吧，剑旗爵。" id _104_0445
    scene black with fade
    jump p1_ch5
return

