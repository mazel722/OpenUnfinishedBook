label p1_ch1:
    stop music fadeout 0.5
    play music "music/fate opening.mp3" fadein 3.0 fadeout 0.5
    play sound "sfx/drip.mp3"
    pause 1.0

    centered "{size=40}有人说，记忆是不可更改的事实，像琥珀中的世界，永远凝固在那一刻。" id _101_Trailblazerreverse_0000

    extend "\n\n但......我不这么认为。" id _101_Trailblazerreverse_0001

    extend "\n\n你看，就像我们此刻的对话。" id _101_Trailblazerreverse_0002

    extend "\n\n对于翁法罗斯来说，这是不存在的“历史”。在你的记忆里，它却是真实的。{/size}" id _101_Trailblazerreverse_0003
    centered "{size=40}如果连过去都能被重新书写，那么未来呢？" id _101_Trailblazerreverse_0004

    extend "\n\n那些尚未发生的、充满变数的未来......" id _101_Trailblazerreverse_0005

    extend "\n\n是否也藏在某一段被遗忘的记忆里，等待着你去唤醒？{/size}" id _101_Trailblazerreverse_0006

    play sound "sfx/drip.mp3"





    menu(screen="choice_center"):
        "是，我所见，即为真实。":
            pass
        "不，也许...这是错觉。":
            pass

    hide text



    centered "{size=40}我们总是面临选择。" id _101_Trailblazerreverse_0008

    extend "\n\n前进，还是后退？" id _101_Trailblazerreverse_0009

    extend "\n\n遗忘，还是铭记？{/size}" id _101_Trailblazerreverse_0010

    centered "{size=40}每一个选择，都会衍生出无数种可能，编织成一张巨大的、看不见的网。" id _101_Trailblazerreverse_0011

    extend "\n\n而你，践行开拓之人......" id _101_Trailblazerreverse_0012
    play sound "sfx/drip.mp3"



    menu(screen="choice_center"):
        "有机会做出选择的时候，不要让自己后悔......":
            pass

    centered "{size=40}我相信，偶然寓于必然之中。终有一日，我会找到命定之外的解答。{/size}" id _101_Trailblazer_0013

    stop music fadeout 1.0
    play music "music/Elysiae Melody.mp3" fadein 1.0 fadeout 1.0

    pause 3.0


    Phainon "......搭档？" id _101_00002
    scene cg p1_ch1_Phainon_first_night with Fade(0.5, 0.5, 1.5)
    Phainon "怎么在这个时候停下了？这可不像你啊。" id _101_00003
    Phainon "嗯，我明白。" id _101_00004
    Phainon "那些伤...很疼吧？痛得让人连手指都不想动弹。" id _101_00005
    Phainon "......但我知道，正是这些伤痕，证明了你从未选择过退缩。" id _101_00006
    Phainon "呼......别着急，慢慢来。" id _101_00007
    Phainon "我猜，你还需要一点时间才能缓过神来。不如......让思绪飞得远一点吧？" id _101_00008

    Phainon "还记得我们在哀丽秘榭那会儿吗？那片麦田，风吹过的时候就像金色的海浪。" id _101_00009
    Phainon "那时候我就在想，如果有一天能和你一起，在风里毫无顾忌地奔跑，该有多好。" id _101_00010
    Phainon "没有黑潮，没有泰坦，只有我们，还有漫山遍野的麦香。" id _101_00011
    Phainon "......可惜，那是梦。美好的梦总是让人想赖着不走。" id _101_00012
    Phainon "我也想就这样一直坐在这里，和你聊聊没用的琐事，聊聊古玩，聊聊那些我们还没来得及去的地方......" id _101_00013
    Phainon "哪怕就这样坐上一整天，我也不会觉得无聊。" id _101_00014
    scene cg p1_ch1_Phainon_first_night_eye with dissolve
    Phainon "但是，搭档...这趟旅途还没到终点呢。" id _101_00015
    Phainon "翁法罗斯的明天，还得靠我们亲手去编织才行。" id _101_00016
    Phainon "要是少了你，我真不知道该怎么办才好了。" id _101_00017
    Phainon "来吧，握住我的手。" id _101_00018
    Phainon "哪怕只是动一动手指也好。哪怕只是把眼睛睁开一点点也好。" id _101_00019
    Phainon "回到清醒的世界吧，搭档！去完成只有你能完成的使命。" id _101_00020
    Phainon "你看......黎明就要来了。" id _101_00021
    Phainon "我在前面等你。" id _101_00022
    Phainon "......"
    Phainon "别让我等太久啊，搭档。" id _101_00024
    scene black with fade


    play music "music/Re Co.mp3" fadein 1.0 fadeout 1.0

    scene cg p1_ch1_EverNight with Fade(2.0,1.0,2.0)
    Unknown_EverNight "醒了？" id _101_0014
    menu:
        "头好晕......":
            pass
        "身体好痛......":
            pass
        "我是谁......?":
            pass

    Unknown_EverNight "嘘...... 还在痛么？没错，你还活着。" id _101_0015
    Unknown_EverNight "别急着确认身体的完整。翁法罗斯是忆质的世界——在这里，躯壳不值一提。" id _101_0016
    Unknown_EverNight "不论你伤成什么样，只要「记忆」还在，我都能把你拼得完好无损。" id _101_0017
    Unknown_EverNight "当然，前提是——你还记得自己是谁。" id _101_0018
    Unknown_EverNight "所以，亲爱的。告诉我，那个伴随你穿越星海的名字......还记得么？" id _101_0019
    $ user_name = renpy.input("请输入你的名字", default="开拓者")
    $ user_name = user_name.strip()
    if not user_name:
        $ user_name = "开拓者"

    Unknown_EverNight "值得庆幸......你的「记忆」没有被数据的洪流冲刷成白纸。" id _101_0020
    Unknown_EverNight "「记忆」......它既是过去的回响，也是未来的种子。" id _101_0021
    Unknown_EverNight "你此刻所回想起的每一个片段，每一次心跳，甚至是一瞬间的痛楚......都是你存在的证明。" id _101_0022
    Unknown_EverNight "那么......还记得之前发生了什么吗？" id _101_0023

    stop music fadeout 1.0
    menu:
        "尝试回忆":
            pass
    scene black with fade

    play music "music/Prayer for Pathlessness.mp3" fadein 1.0 fadeout 1.0

    show cg past_1 with dissolve
    "我与丹恒会合，并意外与螺丝咕姆取得联系。他警示我们，翁法罗斯实为「智识」的试验场，并正在急速坠入「毁灭」命途：一名「绝灭大君」很快就会在翁法罗斯完成进化。" id _101_Trailblazer_0024
    show cg past_2 with dissolve
    "为了联手解决危机，我作为内应留在翁法罗斯内部，丹恒则按原计划返回列车寻求帮助。不仅如此，螺丝咕姆还告诉我们，三月七也在早些时候被卷入了翁法罗斯。" id _101_Trailblazer_0025
    show cg past_3 with dissolve
    "不过，眼下当务之急是「再创世」。我很快抵达创世涡心，和白厄会合。「再创世」仪式本该在来古士主持下顺利进行，但盗火行者的出现再次让世界命运悬而未决。" id _101_Trailblazer_0026
    show cg past_4 with dissolve
    "我们斩落对方面具，发现他的脸孔竟然与白厄无异。而当他的身体被仪式剑贯穿时，海量记忆喷涌而出，有关白厄、盗火行者和翁法罗斯的种种也终于浮出水面......" id _101_Trailblazer_0027
    show cg past_5 with dissolve
    "原来，我们所有人都身处于白厄和昔涟创造的「永劫回归」中，而盗火行者就是背负无数火种后燃烧殆尽的白厄。他们的目的很简单：对抗星神，改写世界注定「毁灭」的结局。" id _101_Trailblazer_0028
    show cg past_6 with dissolve
    "永劫回归已经上演了33550336次。而在这最后一次轮回中，我答应白厄拯救这个世界；而他则会完成无数个自己的夙愿：撕裂天空，与「毁灭」正面对决。" id _101_Trailblazer_0029

    stop music fadeout 1.0
    scene black with fade
    "于是，我与迷迷启动仪式剑，尝试再度重置翁法罗斯的岁月。" id _101_Trailblazer_0030
    "然而......" id _101_Trailblazer_0031
    play music "music/Weaver of Memories.mp3" fadein 1.0 fadeout 1.0
    pause(2.0)
    show cg p1_ch1_Meme with dissolve
    Meme "太好啦......你终于醒过来了。" id _101_0032
    Meme "你昏过去的时候，真的太危险了！差一点，我们就要被逆流的时间卷走了！" id _101_0033
    Meme "翁法罗斯的时空流动......怎么会这样混乱？哪怕是借助仪式剑，也快要支撑不住了......" id _101_0034
    Meme "还好，找到了一处安全的地方，真是万幸。" id _101_0035
    Meme "还记得我们为什么要回到过去吗，[user_name]?" id _101_0036



    menu:
        "必须阻止来古士的阴谋。":
            Meme "是呀。来古士，妄图操纵一切的黑幕，真是不可饶恕。" id _101_0037
        "我决不会辜负白厄的嘱托。":
            Meme "是呀。白厄......他背负的一切如此沉重......" id _101_0038
            Meme "现在，我们必须延续他的信念，拯救翁法罗斯！" id _101_0039
        "我需要更多天外盟友的支援。":
            Meme "是呀。如今我们已经知道，封闭天空不是艾格勒的本意......" id _101_0040
            Meme "它的背后是「来古士」，妄图操纵一切的黑幕，真是不可饶恕。" id _101_0041

    Meme "下一次「再创世」后，翁法罗斯就会坠入「毁灭」的结局......" id _101_0042
    Meme "所以，我们要逆着岁月的长河，开启最后一次永劫回归。" id _101_0043
    "[user_name]" "永劫回归......白厄已经拥抱了自己的命运，现在，是我发力的时候了。" id _101_0044
    "[user_name]" "决不能让火种落入敌人手中！" id _101_0045

    Meme "没错！先在这里暂且休息，等到「岁月」的浪潮平息，我们一起催动仪式剑。" id _101_0046

    Meme "不过，总觉得有些不安...来古士会走上台前，说出一切，说明他对现状还游刃有余。" id _101_0047
    Meme "也许他还握着什么底牌。你想...连「吕枯耳戈斯」都是个假名，我们完全不知道那个坏蛋的来历。" id _101_0048
    Meme "嗯...[user_name]，是不是得借助一下你身上的宝贝啦？" id _101_0049



    menu:
        "该用识刻锚联系螺丝咕姆了...":
            Meme "对。那位智械朋友说过：「必要时，它能成为内外沟通的桥梁」。" id _101_0050
        "向星核许愿，消灭来古士...":
            Meme "这...是不是有些大材小用了？丹恒嘱托过，不能让你使用那股力量。可千万不要冒险呀。" id _101_0051
            Meme "是识刻锚——智械朋友不是说过吗：「必要时，它能成为内外沟通的桥梁」。" id _101_0052

    Meme "混乱的时空困住了我们，却也是我们的机会。在这里，我们或许能和外界取得联系。" id _101_0053
    Meme "总之，先试试看吧？至少得把你平安无事的好消息，带给天外的朋友们。" id _101_0054

    "[user_name]" "（有太多困惑了，我也很在意丹恒和三月七的情况。希望识刻锚能正常运作，我需要解答......）" id _101_0055

    stop music fadeout 1.0

    play music "music/Vector Thirteen.mp3" fadein 1.0 fadeout 1.0
    scene black with fade
    pause 2.0
    show Screwllum normal at left
    show Herta normal at right
    with dissolve
    Screwllum "「信号强度...14.8%%...对话窗口...16分22秒...前提：无外部干扰......」" id _101_0056
    Screwllum "得知你平安无事，我们很欣慰，开拓者女士。" id _101_0057


    menu:
        "见到你们，真令人安心...":
            Herta "很遗憾，现在不是高兴的时候。两个天才站在这里，代表你遇上大麻烦了。" id _101_0058
        "世界外部的情况如何？":
            Herta "很遗憾，没有好消息。两个天才站在这里，代表你遇上大麻烦了。" id _101_0059
        "黑塔，你也在？":
            pass

    Herta "听好了，小家伙。「毁灭」的目光看向了这里。我没有开玩笑，不是机器头，是纳努克。" id _101_0060
    Screwllum "时间紧迫，我会用你熟知的概念说明。" id _101_0061
    Screwllum "我们解明了翁法罗斯的真身：它是历史上第一台「权杖」，最初的原型机——博识尊神体的一部分。" id _101_0062
    Screwllum "在这片不为人知的星域，它不断重复「再创世」的进程。" id _101_0063
    Screwllum "若无法进行有效干涉，预测：十四个系统时后，铁墓将完成自我加冕，启动对「智识」命途的毁灭计划。" id _101_0064


    menu:
        "十四个系统时，这也太快了...":
            Herta "权杖内外的时间流速不同，尽管外部宇宙迫在眉睫，但你还有时间扭转这一切。" id _101_0065
        "它要如何毁灭「智识」？":
            Herta "可能性太多了。瓦解星际通讯、破坏联觉信标、让群星重回黑暗时代，甚至掀起第三次反有机战争，为银河带来灭顶之灾。" id _101_0066
            Herta "简而言之，让一切科学和技术倒向「毁灭」——既然纳努克看向了这里，就说明祂是认真的。" id _101_0067

    Herta "要阻止这一切，首先要搞明白原因。" id _101_0068
    Herta "一个求索“生命第一因”的权杖，为什么会导向毁灭？" id _101_0069
    Herta "就算毁灭是可能的答案，这权杖也太过笃定了。" id _101_0070
    Screwllum "有人在幕后推动这一切：名为「来古士」的观测者。推测：他是权杖系统的管理员。" id _101_0071
    Herta "权杖——或者说来古士——以「神谕」的方式向电信号颁布任务，就像悬在绵羊头顶的萝卜，催动着他们前进。" id _101_0072
    Herta "你有没有想过：这理所应当的神谕，真的毫无隐瞒吗？" id _101_0073
    Herta "再创世之后重返黄金世，哪有这么好的事情？" id _101_0074


    menu:
        "我从未想过":
            Herta "童年般的「黄金世」——啧，动动你的小脑瓜，怎么可能是真的？" id _101_0075
            Herta "如果是真的，铁墓又为何诞生？" id _101_0076
            Herta "只有一个解释——权杖许诺的再创世，是一场骗局。" id _101_0077
        "白厄也说过，未来不可能是理想乡......":
            Herta "看来，本地的小家伙也有所猜测。" id _101_0078
        "黄金裔别无选择。":
            Herta "当局者迷，你们身在局中，这也难免。" id _101_0079

    Herta "简单点说，现在的翁法罗斯进行的是{color=#FF0000}「假创世」{/color}；火种集齐后，根本没有美好的明天，只有哗哗涨进度的铁墓。" id _101_0080



    Herta "智械哥写下十四行代数式，封闭翁法罗斯，抹去了第十三位泰坦。" id _101_0081
    Herta "自那时起，翁法罗斯便成为了铁墓的温床。" id _101_0082
    Herta "残缺的十二泰坦进行的「再创世」，从理论上看，与毁灭无异。" id _101_0083

    Screwllum "推测：如果能够补全第十三泰坦，「再创世」将被改写为「真创世」。" id _101_0084


    menu:
        "真创世会带来什么？":
            pass
    Herta "杀死铁墓？复活死者？或者大胆点——让电信号成为生命。" id _101_0085
    Herta "无论如何，至少不会比现在更坏。" id _101_0086
    menu:
        "关于第十三泰坦，还有其他线索吗？":
            pass


    Herta "从外界观测太过局限，我们只能提出一些猜测。" id _101_0087
    Screwllum "逻辑：「假创世」的本质，是「权杖」的自主协议。在翁法罗斯，这道自主协议有另一重命名——" id _101_0088
    Screwllum "律法之泰坦。" id _101_0089
    Screwllum "假如有一种方式可以扭转「假创世」的进程，它必定与「律法」密不可分。" id _101_0090
    Herta "总之，从「律法」入手，去寻找翁法罗斯缺失的东西，这就对了。" id _101_0091
    Herta "这件事很难，我知道。我倒是想进去帮忙，可惜，你和丹恒{color=#FF0000}进入这个世界的方法{/color}仍是未解之谜，只能靠你自己。" id _101_0092
    show Screwllum at cyber_glitch_v3
    show Herta at cyber_glitch_v3
    play sound "sfx/error.mp3" loop
    Herta "如果找到...突破...权杖防御...方法..." id _101_0093
    Screwllum "黑塔，防火墙的干扰迫近了。" id _101_0094
    Screwllum "我相信你的力量，[user_name]女士。「开拓」的双手能创造奇迹，也一定能寻找到翁法罗斯缺失之物。" id _101_0095

    Herta "我就不发表什么励志演讲了，只希望下次见面你能带来好消息，小家伙。" id _101_0096
    stop music fadeout 1.0
    pause 0.5
    show black
    play movie "videos/error.webm" fadein 1.0
    play sound "sfx/error.mp3" volume 0.5
    $ renpy.pause(1.0,hard=True)
    stop movie
    stop sound



    show cg p1_ch1_Meme at center with dissolve
    play music "music/Fading Prophecy.mp3" fadein 1.0 fadeout 1.0
    Meme "......" id _101_0097
    Meme "真是...两位充满个性的「天才」呢。" id _101_0098
    Meme "联络结束了，可是时间的乱流， 还是没有平息。" id _101_0099
    Meme "甚至......加剧了？这片避风港已经无法容我们藏身，我们必须启程了。" id _101_0100
    Meme "我们就要告别第33550336次轮回......去重新认识大家，踏上全新的旅途了。" id _101_0101
    Meme "可是......下一次轮回的他们，真的还是我们熟知的伙伴吗？" id _101_0102


    menu:
        "我相信，他们从未改变。":
            Meme "是呀。为了拯救翁法罗斯，每一次轮回，大家都做出了同样的选择......" id _101_0103
            Meme "即便记忆归零，那熠熠生辉的灵魂，也绝不会被时间磨损。" id _101_0104
            Meme "所以，是时候出发啦！" id _101_0105
        "我也很不舍。":
            Meme "构成迷迷的，就是「记忆」本身。可如果抹去「记忆」重新开始...... " id _101_0106
            Meme "[user_name]还会觉得，迷迷没有变吗？" id _101_0107
            Meme "算啦，现在不是纠结这些的时候。" id _101_0108
            Meme "虽然很舍不得大家，但我们没有其他选择了。" id _101_0109
        "我不知道......也许不再是了。":
            Meme "还记得吗，白厄也认为，「按照记忆重塑而成的事物，已经不能和原来的画等号」。" id _101_0110
            Meme "虽然很舍不得大家，但我们没有其他选择了。" id _101_0111





    Meme "来吧，[user_name]，抓紧我的手，不要被乱流冲散——" id _101_0112

    Meme "借助我们的仪式剑，送你回到「岁月」的起点——" id _101_0113

    stop music fadeout 1.0
    scene black with fade

    play music "music/Don't Get Lost.mp3" fadein 1.0 fadeout 1.0
    Unknown_EverNight "嘘。" id _101_0114

    play movie "videos/p1_ch1_Evernight.webm"
    $ renpy.pause(3.0,hard=True)
    scene black
    stop movie
    pause .0



    "[user_name]" "（那时候，我和迷迷催动仪式剑，踏入混乱的时间。然而，在开启33550337次永劫回归之前，混乱的时间袭向了我。）" id _101_0115
    show cg p1_ch1_EverNight with fade
    "[user_name]" "（我晕了过去。再睁开眼时......迷迷不见了，我的记忆也有些混乱。）" id _101_0116
    "[user_name]" "（难道，就是她掀起了时空乱流，带走了迷迷？）" id _101_0117
    menu(screen="choice_center"):
        "结束回忆":
            pass
    "[user_name]" "你究竟做了什么？" id _101_0118

    Unknown_EverNight "看来，你已经完全想起来了。" id _101_0119
    Unknown_EverNight "嘘...我愿意为你解释更多，但不是现在。我们可以有很多、很多私人时间，但翁法罗斯没有。" id _101_0120
    EverNight "翁法罗斯的三月，属于永夜之帷的时间... 暂时以长夜月这个称呼，将我放进你的回忆中吧。" id _101_0121
    EverNight "你只需要明白，我不会比所谓的“迷迷”，对你而言更危险。" id _101_0122

    menu:
        "三月七......？好久不见。":
            pass
        "迷迷在哪里？":
            pass
        "我无法相信你。":
            pass
    show cg p1_ch1_EverNight_Meme with dissolve


    Meme "唔——唔！" id _101_0123
    EverNight "唉...... 你还是这样，天真得可爱啊——亲爱的[user_name]。" id _101_0124
    EverNight "你似乎对身边这个小东西完全不加防范呐——你真的清楚它的本质吗？" id _101_0125
    EverNight "还是说，你就这么相信了她是一只会飞的小狗？" id _101_0126

    menu:
        "放开迷迷！":
            EverNight "啊，看看你的表情。多么感人的羁绊。" id _101_0127
            EverNight "可是，亲爱的......你信任她，是因为你无法透过小妖精的外表，看到她的本质。" id _101_0128
            pass
        "你的意思是......？":
            pass
        "......":
            pass




    EverNight "承认吧......你真的没有想过吗？" id _101_0131
    EverNight "「难道说，{color=#FF0000}这个来路不明的生物，就是幕后黑手？{/color}」" id _101_0132
    menu:
        "我不会怀疑自己的伙伴。":
            pass
        "我确实这样想过。":
            pass



    EverNight "呵......原来你是这样想的。但我只有一种回答。" id _101_0133
    EverNight "远离她。这不是一句劝诫，而是一次通告。" id _101_0134
    menu:
        "你的目的是什么？":
            pass
        "放我离开，我必须开启再创世！":

            pass
        "......":
            pass


    EverNight "你的怀疑真让人伤心。是我在时空乱流中保留了那片安全的区域，容你们藏身哦？" id _101_0136
    EverNight "那时，如果任由你们走向过去......死只是最仁慈的解脱。" id _101_0137
    EverNight "你会变成无限的切片，散落在翁法罗斯的每一个角落，同他们一起走向毁灭。" id _101_0138
    EverNight "幸好，我及时赶到。但你还是晕了过去。" id _101_10139
    EverNight "昏迷的时候，你皱着眉头，念念有词......是梦见了谁？" id _101_10140
    EverNight "呵，不必回答我。听好了，亲爱的[user_name]。" id _101_10141
    EverNight "你所寻找的「可能」，根本不在翁法罗斯被限定的命运之内。" id _101_0139
    EverNight "我救下你的灵魂，可不是为了让你在错误的道路上白白浪费时间。" id _101_0140
    menu:
        "错误的道路？":
            "[user_name]" "由我接过负世的火种，是当下唯一的选择。" id _101_0141
        "我可不会乖乖听从你的指引。":
            pass

    EverNight "负世——你何曾与那火种有一丝一毫的共鸣？" id _101_0142
    EverNight "由你催动的仪式剑，根本不能平息岁月的洪流。所以，你也无法开启永劫回归，回到过去。" id _101_0143
    EverNight "你真以为接过白厄的使命，就能高高在上地拯救他们了？" id _101_0144
    EverNight "身为天外之人，却削足适履，试图成为命运已有的一环——荒谬至极。" id _101_0145


    EverNight "还记得么？翁法罗斯的本质，是一台权杖。" id _101_0146
    EverNight "而在世界的深处，有一座深埋其中的遗迹。在「智识」的语言中，它被称作内核层。但我为它取了个更亲切的名字......" id _101_0147
    menu:
        EverNight "翁法罗斯的心脏——无名泰坦大墓。" id _101_0148
        "能不能说的清楚点？":
            EverNight "这需要你自己去寻找，亲爱的。" id _101_0149
        "我该去找谁？":

            EverNight "这需要你自己去寻找，亲爱的。" id _101_0150
        "我不会相信你。":
            EverNight "我不需要这份信任。" id _101_0151
            EverNight "当然......空口无凭，眼见为实。" id _101_0152


    EverNight "在黑暗中「开拓」吧，一如既往......" id _101_0153
    EverNight "「忘却」会守望你的来路，如长夜般隐秘，永远安宁。" id _101_0154




    scene black with Fade(1.5, 0, 0.5)
    pause 1.0




    "[user_name]" "迷迷，你在哪？" id _101_0155
    "[user_name]" "...真的不见了......长夜月带走了它。" id _101_0156
    scene bg nodoor with fade:
        align (0.5, 0.5)
        zoom 1.1

    show layer master at continuous_shake
    play sound "sfx/collapse.mp3" fadein 3.0 volume 0.5 loop
    "[user_name]" "等等，我回到了......创世涡心？！" id _101_0157
    "[user_name]" "这片空间在崩解，来不及了！" id _101_0158
    "[user_name]" "如果不能用仪式剑回到过去，就只能用时刻锚脱离翁法罗斯了......" id _101_0159


    menu:
        "[user_name]" "可恶！该怎么办？" id _101_0160
        "尝试催动仪式剑":
            "仪式剑毫无反应。" id _101_0161
            "你已经使用过它一次，或许，它的力量耗尽了。" id _101_0162
            "如果不能回到过去，下一次再创世之后，铁墓就会诞生......" id _101_0163
            "长夜月破坏了永劫回归！她究竟在做什么......？" id _101_0164
            "但此刻，比起担忧这些，或许更该担忧自己的小命......" id _101_0165
        "直接激活时刻锚":

            "时刻锚上的数字飞速跳动，这个精巧的装置运行良好。" id _101_0166
            "只需要按下「脱离」的按钮，程序就会启动......" id _101_0167
            "[user_name]" "事到如今，只能随机应变了。或许在世界之外，能够找到扭转翁法罗斯进程的方法。" id _101_0168
            "[user_name]" "绝不能辜负白厄的嘱托。" id _101_0169





    scene black with dissolve
    play movie "videos/error.webm" fadein 1.0
    play sound "sfx/error.mp3" volume 0.5
    $ renpy.pause(1.0,hard=True)
    stop movie
    stop sound






    scene white with dissolve

    scene bg door with fade

    "[user_name]" "等等......" id _101_0170
    "[user_name]" "创世涡心深处......出现了一道光？" id _101_0171
    show bg at scene_zoom_door_in
    pause 5.0

    "[user_name]" "以前进入创世涡心的时候，从未见过它。阿格莱雅和白厄也没有提到过...看来，他们也不知情。" id _101_0172
    "[user_name]" "它通向哪里？似乎连接了另一片空间......" id _101_0173

    $ a = True
    $ loop_condition = True
    while loop_condition:
        menu:
            "进入神秘的空间。":
                $ loop_condition = False
            "要不......去别处看看？" if a:
                scene black with fade
                play sound "sfx/explosion.mp3"
                "一块巨石从天而降，切断了你身后的道路。" id _101_0174
                "[user_name]" "没有退路了。想要留在翁法罗斯寻找线索的话，只能进入这里了。" id _101_0175
                show bg door:
                    yanchor 0.5
                    ypos 1000
                    xalign 0.5
                    zoom 2.0
                with fade
                $ a = False

    scene bg UnnamedTitanTomb_outdoor with Fade(0.5, 1.5, 1.0, color="#ffffff")

    "[user_name]" "万幸，这里非常稳定，建筑不再塌陷了。" id _101_0176
    "[user_name]" "这里的装潢，似乎是一个...门厅？" id _101_0177

    "[user_name]" "......门被锁上了，需要某种权限才能打开。" id _101_0178

    "......" id _101_0179
    "{color=#ff0000}权杖δ-me13：>>>警告：对象无访问权限。{/color}" id _101_0180
    "{color=#ff0000}权杖δ-me13：█ ██ ███ ███████████{/color}" id _101_0181
    "{color=#ff0000}权杖δ-me13：>>>█ 欢迎回来█ ██ 开拓者 ███{/color}" id _101_0182
    "[user_name]" "好像有种既视感......" id _101_0183
    "[user_name]" "...第一次翻开《如我所书》的时候？" id _101_0184
    "[user_name]" "还好没被「长夜月」拿走...试试看吧。" id _101_0185
    "{color=#ff0000}权杖δ-me13：>>>操作已授权，协议名：「██ ███」{/color}" id _101_0186
    "[user_name]" "封锁解除了，没想到这本书会在这里发挥作用......" id _101_0187

    menu:
        "进入":
            pass
    show bg at scene_zoom_titan_in
    pause 1.0
    scene white with dissolve
    "[user_name]" "好刺眼......" id _101_0188
    scene black with Fade(1.0, 0.0, 1.0)



    show layer master at default
    stop music fadeout 1.0
    show bg UnnamedTitanTomb_indoor_1 at scene_look_around with fade

    "[user_name]" "尽管与创世涡心相连，这里的模样却完全不同。" id _101_0189
    "[user_name]" "翁法罗斯的风格接近神话史诗，这片空间却十分现代，就像......摘掉了伪装的面具。" id _101_0190
    "[user_name]" "远方的建筑群，是存储翁法罗斯数据的地方么......" id _101_0191
    "[user_name]" "就算是逐火的黄金裔，也不曾知道，创世涡心深处，还有这样宏伟的空间。" id _101_0192
    "[user_name]" "或许，我确实在深入翁法罗斯的真相......" id _101_0193
    "[user_name]" "等等，前面的平台上......谁在那里？！" id _101_0194








    play music "music/Frozen Tides.mp3" fadein 1.0 fadeout 1.0

    show Hysilens normal at center with dissolve
    Hysilens "...宴会...落幕了？" id _101_0195
    Hysilens "灰色的鱼儿，你是天外的宴宾，还是毁灭的走卒？" id _101_0196
    Hysilens "...又或者，你不过是我的梦中的幻影。" id _101_0197


    $ a = False
    $ b = False
    while not (a and b):
        menu:
            "你是...?" if not a:
                Hysilens "我是海洋的半神，凯撒手下的一柄剑旗。你可唤我：海瑟音。 " id _101_0198
                $ a = True

            "这里是......" if not b:
                Hysilens "此地名为无名泰坦大墓。它曾属于一道被抹消的命途，如今......它不过是时间的坟墓罢了。" id _101_0199
                $ b = True
    Hysilens "果真如她所言，寰宇浩荡，竟能将你带到我面前。" id _101_0200


    menu:
        "我听说过你。":
            "[user_name]" "你就是......千年前的黄金裔？我在史书中见过你的名字。" id _101_0201
        "我不曾听说过。":
            Hysilens "......在后世眼中，我们早已死去。" id _101_0202

    Hysilens "我听从凯撒的命令在此守望，等待一枚来自天外的音符，让此世重归完整。" id _101_0203

    menu:
        "凯撒的命令？":
            pass
        "所以，你在等待我吗？":
            pass

    Hysilens "灰鱼儿，我知晓你的来意。" id _101_0204
    Hysilens "我追随的君王，刻律德菈，便是你寻找的律法之半神。" id _101_0205
    menu:
        "你怎么知道？":
            pass
        "......":
            pass
    show Hysilens smile with dissolve
    Hysilens "不必惊慌。是凯撒料到了你的来意。她说..." id _101_0206

    scene black with fade
    Cerydra "在无穷数的未来，必定有人能够站在此处，询问「律法」之谜，追寻第十三枚火种。" id _101_0207
    Cerydra "而你，剑旗爵......" id _101_0208
    Cerydra "留守此地，为来客指引方向，也验证他的决心。" id _101_0209

    scene cg p1_ch1_Hysilens with Fade(0.5, 1.0, 1.0)


    Hysilens "在你抵达之前，在过去的三千万转，我，凯撒，那位黑袍的剑士......我们都没能迎来转机。" id _101_0210




    Hysilens "我不过是遵从她最后的命令，在此徒劳的等待。" id _101_0211
    show cg p1_ch1_Hysilens_eyeclosed with dissolve
    Hysilens "我以为，我会在满溢的蜜酿中闭上双眼，直到世界的尽头。" id _101_0212
    Hysilens "虚假的「再创世」将摧毁一切，连同我的意志，连同我的生命。没有痛苦，也不再有别离。" id _101_0213

    show cg p1_ch1_Hysilens with dissolve
    menu:
        "虚假的「再创世」？":
            pass
        "你刚刚提到了，一位黑袍剑士？":
            Hysilens "啊...你已见过他了。请代我道谢。" id _101_0214
            Hysilens "逆流于时间之海...这份痛苦，唯他一人背负。" id _101_0215


    Hysilens "翁法罗斯是一个残缺的世界，如同被夺取尾鳍的鱼儿。十二道命途看护着万千生灵，却无可避免堕向毁灭的结局。" id _101_0216
    Hysilens "所以，以人性为代价，凯撒为你准备了一种可能。" id _101_0217
    Hysilens "——第十三枚火种。这将是你改写「再创世」的前提。" id _101_0218
    scene black with fade
    pause 0.5
    show bg fireseed at truecenter with Dissolve(3.0)
    pause(2.0)
    menu:
        "第十三枚火种，是空白的？":
            pass
        "它究竟承载了什么？":
            pass


    Hysilens "这是一条不曾存在过的道路。在她为我描述的未来里，它将指向天外群星，指向真实。" id _101_0219
    Hysilens "灰鱼儿，我听得见它与你的共鸣。" id _101_0220
    Hysilens "我衷心希望，你能够点燃这簇火焰。" id _101_0221





    "[user_name]" "这大概就是黑塔所说，翁法罗斯缺失的东西。长夜月指引我来到此地，也是为了这枚火种吗？" id _101_0223

    menu:
        "为了翁法罗斯，我责无旁贷。":
            pass
        "姑且试试吧...":
            pass


    Hysilens "凯撒不会轻易将火种托付于陌路之人。触碰这枚火种之时，亦是她验证你信念的时刻。" id _101_0224
    Hysilens "或许，你会见证她的生涯。你会明白，我所追随的是怎样一位君王；而她也会触碰你思想的洋流......" id _101_0225
    Hysilens "灰鱼儿，你能够站在这片水域，本就是一种奇迹。" id _101_0226
    Hysilens "我愿意相信，你就是我们在等的人。" id _101_0227
    Hysilens "若你已经做好准备，成为这世界等待的变量......" id _101_0228
    Hysilens "便去触碰它吧。" id _101_0229

    menu:
        "读取火种内的记忆":
            pass

    scene black with fade


    "[user_name]" "......这就是火种内蕴藏的记忆吗？" id _101_0230
    "[user_name]" "看来，我要在记忆中寻找第十三火种的来历，理解翁法罗斯的真相，才能接过火种。" id _101_0231
    scene bg FateTemple_square with Fade(0.5,1.0,1.0)
    pause 1.0
    "[user_name]" "这里是......雅努萨波利斯？" id _101_0232
    "[user_name]" "通过岁月宝珠，我见过神殿坍圮前的样子。" id _101_0233
    "[user_name]" "如此繁荣的圣殿，看来，这就是33550336次轮回中，千年前的雅努萨波利斯。" id _101_0234
    "[user_name]" "咦，这段记忆是......？" id _101_0235




    play music "music/Agnus Aeon.mp3" fadein 2.0
    show bg Palace_meetingroom with Fade(0.5,3.0,1.0)
    pause 1.0
    "仆人" "请您稍作等候，大人马上就来。" id _101_0236
    show Cerydra normal_wocrown at left
    show Regent at right
    with dissolve
    Noble "我亲爱的孩子，你还记得自己叫什么，对吗？" id _101_0237
    Unknown_Cerydra "......我是刻律德菈。" id _101_0238
    Noble "你有一头美丽的蓝发，明亮的眼眸。" id _101_0239
    Noble "恰好，一如先王。" id _101_0240
    Noble "偷天换日...呵呵。" id _101_0241
    Noble "从巷尾看到你苟延残喘的时候，我就相信你能够做出一番大事业..." id _101_0242
    Noble "可别让我失望哦？" id _101_0243
    Cerydra "......" id _101_0244


    scene bg Palace_meetingroom with fade
    show priest at left
    show Regent at right
    with dissolve

    priest "阁下远道而来，神殿本该扫榻相迎。" id _101_10245
    priest "只是近日，圣女身感不适，恐怕不便见客。" id _101_10246
    Noble "呵，祭司大人说笑了。" id _101_10247
    Noble "哪怕是神明，只要价码合适，偶尔也会垂怜凡人一二，不是吗？" id _101_10248
    Noble "当然，基本的礼节我也明白。" id _101_0245
    Noble "在下已备薄礼两份，分别赠与圣女与祭司大人。" id _101_0246
    Noble "我已命人送去您的庭院了。礼单在此，祭司大人可以先行过目。" id _101_0247
    play sound "sfx/newspaper.mp3" fadein 3.0 volume 0.5

    Noble "您可曾听说过，许珀耳有一位流落人间的王女；她流着黄金的血液，发色是北境之蓝。" id _101_0248
    priest "......不曾。" id _101_0249
    Noble "不过，也可以听说过。" id _101_0250
    play sound "sfx/newspaper.mp3" fadein 3.0 volume 0.5
    priest "我想您还不明白我的意思，大人。" id _101_0251
    priest "雅努萨波利斯的圣女，是泰坦意志的代行。" id _101_0252
    priest "倘若泰坦没有获得满意的祭品...我也无法保证，是否会颁布让您满意的神谕。" id _101_0253
    Noble "自然，自然。我既然真心想要求见圣女，自然要拿出相应的诚意。" id _101_0254
    Noble "城外那块良田，我知道祭司大人一直记挂于心，不如我今日就将它赠与神殿，聊表心意如何？" id _101_0255
    priest "神明必将回应您的虔诚。" id _101_0256
    priest "不过......圣女喜静，还请王女一人前往。" id _101_0257
    Noble "如此，便感谢神明的慷慨了。" id _101_0258
    Noble "刻律德菈，去吧。" id _101_0259


    scene bg Tribios_room with Fade(1.5,0.5,1.5)
    show Tribios normal at right
    show Cerydra normal_wocrown at left
    with dissolve
    Tribios "你就是他们口中的那位......来自北境的王女？" id _101_0261
    Cerydra "正是。" id _101_0262
    Tribios "请回吧。这扇门后没有你要的东西。" id _101_0263
    Tribios "我不会为了满足权贵，编造出神明从未许诺过的预言。" id _101_0264
    show Cerydra normal_wocrown with dissolve
    Cerydra "你应当知晓，那些盼望我戴上冠冕的人，早已与神殿的祭司达成了共识。" id _101_0265
    Cerydra "无论你是否开口，明日，雅努萨波利斯的街头巷尾都会传遍圣女的口谕——" id _101_0266
    show Cerydra smile_wocrown with dissolve
    Cerydra "刻律德菈，即是命定称王之人。" id _101_0267
    Tribios "你清楚我的处境。看来，他们挑选摆在台前的傀儡，倒也并非全无考量。" id _101_0268
    Tribios "你也知道，我的话语对结局无足轻重......又何必来此，与我多费口舌？" id _101_0269
    Cerydra "我要求见塔兰顿。" id _101_0270
    Tribios "律法之泰坦更不会给你想要的预言，王女。" id _101_0271
    Cerydra "我不为乞求神谕而来。神谕皆可由人伪造。" id _101_0272
    Cerydra "...被禁锢的圣女，早已失落信仰的神殿。终有一日，这些虚妄会失去民众的敬畏。" id _101_0273
    Cerydra "但人的血色，无可伪造。" id _101_0274
    Tribios "你想要....." id _101_0275
    Cerydra "倘若这具躯壳里奔涌的，确是黄金的血液......那么，无需任何预言与神谕加冕，我亦是他们必须跪拜的王。" id _101_0276
    Tribios "......" id _101_0277
    Cerydra "没错。我要借助泰坦的伟力，将这一身凡血，换为黄金血。" id _101_0278
    Cerydra "你不想亲眼见证吗？圣女。看我是否能博得泰坦的青睐......" id _101_0279
    Cerydra "看我是个只会虚张声势的骗子，任人摆布的懦弱傀儡......亦或是，终结这乱世的女皇。" id _101_0280
    Tribios "......" id _101_0281
    Tribios "那么，请吧，王女。" id _101_0282
    scene bg FateTemple_law_room with fade
    show Cerydra normal_wocrown at left
    show Tribios normal at right
    with dissolve



    Tribios "凡人无法理解泰坦的低语。我将充当你们沟通的媒介，你听到的，将是未经凡心篡改的神谕。" id _101_0283
    Tribios "请吧。祂聆听此世一切祈祷。" id _101_0284
    show cg p1_ch1_Cerydra_trade with Fade(1.0, 0.5, 1.0)
    pause 1.0
    Cerydra "律法之泰坦，塔兰顿。" id _101_0285
    Cerydra "我，刻律德菈，许珀耳玻瑞亚的王储，向你提出一笔交易。" id _101_0286
    Cerydra "若将我体内奔涌的凡血替换为黄金，作为回馈，我将带来一个崭新的世界。" id _101_0287
    Cerydra "你所厌恶的混乱不复存在，我颁行的律法，将重新指引人的命运。" id _101_0288
    Cerydra "不再有欺瞒，不再有饥饿，不再有流浪与混乱。" id _101_0289
    Cerydra "我会将这世界的规则改造一新，将律法的恩泽，施予一切臣服者。" id _101_0290
    pause 1.0
    Tribios_Talanton "......" id _101_0291
    Tribios_Talanton "我拒绝，狂妄的人子。" id _101_0292
    hide cg with fade
    show Cerydra angry_wocrown with dissolve
    Cerydra "唔......！" id _101_0293
    "女孩感到烈火灼烧的剧痛。"
    "指甲嵌进掌心，殷红的血珠簌簌滚落。"
    "但她仍然昂着头，直视塔兰顿。" id _101_0294
    Tribios_Talanton "凡人啊，莫要将金血奉为神圣之物。" id _101_0295
    Tribios_Talanton "一切罪恶皆起源于黄金的血液，一切悲剧皆起源于黄金的血液。" id _101_0296

    scene black with fade
    Unknown_Khaos "......人们歌颂它，渴望它，为了它自相残杀。" id _101_0297
    Unknown_Khaos "不错。只有拥有金血的人，才有资格谈论“健全”与“成长”。" id _101_0298
    Unknown_Khaos "但这世上，没有无缘无故的力量。要完成一件只有你能完成的事，便必须背负只有你能背负的代价。" id _101_0299
    Unknown_Khaos "......你尚未做好准备。你将在血液的灼烧中融化。" id _101_0300

    scene bg FateTemple_law_room with fade
    show Cerydra normal_wocrown at left
    show Tribios normal at right
    with dissolve

    "巨大的天平缓缓转动，发出沉闷的轰鸣。它倾斜，摇摆，却始终没有倒向刻律德菈。" id _101_0301

    hide cg

    Tribios_Talanton "狂妄的人子，你的信念不足以撼动天平。吾拒绝将罪恶的血液交予汝。" id _101_0303
    Tribios "它拒绝再交流了。" id _101_0304
    show cg p1_ch1_Cerydra_redblood with dissolve
    Tribios "......您受伤了吗？我可以唤下人为您包扎。" id _101_03041
    Cerydra "不必了。" id _101_03042
    Cerydra "哈......看来此路不通啊。无妨，泰坦不愿给的，我仍有办法得到。" id _101_0305
    hide cg with dissolve

    Tribios "请留步，王女。" id _101_0306
    Cerydra "何事？" id _101_0307
    Tribios "我在此做出预言。刻律德菈，即为许珀耳玻瑞亚失落的皇女。" id _101_0308
    show Cerydra sneer_wocrown with dissolve
    pause 0.5
    Cerydra "哦？如你所见，我未能撼动旧律的天平。这预言，如今听来倒像是讽刺。" id _101_0309
    show Cerydra normal_wocrown with dissolve
    Tribios "北方的访客，缇里西庇俄丝绝非闭目塞听之人。" id _101_0310

    show Tribios smile with dissolve
    Tribios "在我所见的未来，{color=#FF0000}你的确不是旧朝王女，却是许珀耳的新王。{/color}" id _101_0311
    show Tribios normal with dissolve
    Tribios "你眼中的野心在涌动，如同将要燃起的燎原烈火。" id _101_0312
    Tribios "泰坦不愿赐予你血液，但命运，仍将眷顾你的意志。" id _101_0313
    Tribios "或许......你真的能为混乱的北境带来和平。" id _101_0314
    Cerydra "哈......" id _101_0315
    Tribios "请向我证明吧，王女。证明我今日的预言并非虚假。我期待着，你所描述的......新世界。" id _101_0316

    stop music fadeout 4.0
    scene black with Fade(2.0,3.0,1.0)
    jump p1_ch2
return

