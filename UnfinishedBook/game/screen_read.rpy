screen read_screen():
    tag menu

    add "gui/new/read/back.jpg"

    default page = 1



    imagebutton:
        if page == 1:
            idle "gui/new/chapter_select/part1_hover.png"
        else:
            idle "gui/new/chapter_select/part1_idle.png"
        hover "gui/new/chapter_select/part1_hover.png"
        focus_mask True
        action SetScreenVariable("page", 1)

    imagebutton:
        if page == 2:
            idle "gui/new/chapter_select/part2_hover.png"
        else:
            idle "gui/new/chapter_select/part2_idle.png"
        hover "gui/new/chapter_select/part2_hover.png"
        focus_mask True

        action SetScreenVariable("page", 2)


    imagebutton:
        if page == 3:
            idle "gui/new/chapter_select/part3_hover.png"
        else:
            idle "gui/new/chapter_select/part3_idle.png"
        hover "gui/new/chapter_select/part3_hover.png"
        focus_mask True

        action SetScreenVariable("page", 3)

    if page == 1:

        add "gui/new/chapter_select/bar_30.png"
        vbox:
            xanchor 0.0
            yanchor 0.0
            xpos 275
            ypos 650
            spacing 20
            textbutton _("创世涡心") action Show("scrollable_text_window", title="创世涡心", content_text="""经海瑟音重塑后的异域。
在永劫轮回中，由于NeiKos496与HubRis504的交易，创世涡心被重塑。此后，████████████，火种与创世涡心建立链接，火种归还仪式被限定在创世涡心进行。
半神死亡后，若火种未落入黑潮，火种自主回归创世涡心，由灵水盆封存。""", close_action=Hide("scrollable_text_window"))

            textbutton _("火种") action Show("scrollable_text_window", title="火种", content_text="""在永劫回归进程中，为避免火种被「铁墓」取得，NeiKos496通过杀死半神收集火种。
海瑟音重塑创世涡心后，若半神自主死亡，且火种未落入黑潮，火种将回归创世涡心，最终被NeiKos496取得。
因此，在永劫回归进程中，NeiKos496从未遗落火种。""", close_action=Hide("scrollable_text_window"))

            textbutton _("保护措施") action Show("scrollable_text_window", title="保护措施", content_text="""管理员批注：为保障实验隐蔽，在权杖周围设置星核污染，将外部宇宙的干涉可能性降到最低。此外，应通过十四行代数式及忆质加密环境，对实验的「涟漪」进行封闭处理，阻断＃4波尔卡·卡卡目的观测。
由于封闭环境建立，在实验环境内，“开拓”命途同步被抹除。

HubRis504以自我静默为代价，部分破坏十四行代数式。变量“开拓者”“丹恒”被识别为非恶意侵入变量，进入实验环境。""", close_action=Hide("scrollable_text_window"))

            textbutton _("心中的英雄") action Show("scrollable_text_window", title="心中的英雄", content_text="""由于NeiKos496兼任第一泰坦「负世」、第十三泰坦「创世」，在NeiKos496心中出现的「创世」泰坦的形象。
其实质是NeiKos496作为「创世」泰坦的自我意识。推测为智能奇点临近的表征。
星穹列车到来后，由于开拓者符合「创世」泰坦特征，「心中的英雄」逐渐与开拓者重合。""", close_action=Hide("scrollable_text_window"))


        vbox:
            xanchor 0.0
            yanchor 0.0
            xpos 690
            ypos 650
            spacing 20
            textbutton _("追忆残像") action Show("scrollable_text_window", title="追忆残像", content_text="""捷足爵，此去斯缇科西亚，恐怕无回。
您......认真的？
我可是听说了，今晚就要举行宴会，为逐火军饯行。
您是“凯撒”，是奥赫玛的天。我可不相信有您打不下的疆域哪。
何况......既然打不赢，不去不就是了？打不过，总跑得过吧！
捷足爵，这是命令。
明日，我会亲率将士，直指法吉娜的巢穴。无论胜败，世上再无刻律德菈。
此战之后，我要你......变成我。
令凯撒成为真正不通人性的暴君吧——直至众臣反目，直至民怨沸腾，直至......他们忍无可忍，举起叛旗。
到那时，就是金织爵的时刻了。她将顺应民意，终结“暴政”，成为奥赫玛名至实归的领袖。
我的离去，会筑成你们的长阶。""", close_action=Hide("scrollable_text_window"))
            textbutton _("「运行记录：致菲狄亚斯学士的一封信」") action Show("scrollable_text_window", title="「运行记录：致菲狄亚斯学士的一封信」", content_text="""注释：外来变量███向翁法罗斯写入██后出现的记录。

挚友如晤：
别来无恙。
今晨，刚抵达友爱之馆，我便一头扎进了故纸堆里。一开始只是为了消遣，没想到，从零散的记录里面，我竟然拼凑出一条惊心动魄的脉络。
如果这一猜测为真，或许......足以颠覆敬拜学派。
哈哈，我没有这样的野心。所以，你当做茶余饭后的故事，读一读便好。
神话经过代代诗人的润色与美化，早已面目全非，难以作为证据。然而，正如沙砾中偶现真金，神话的确能作为线索，启迪思维。
我把各处记载整合，摘录若干，随信附上。
结论——就容我卖个关子吧。以你对历史的敏感，在读完我整理的残卷后，一定能挖掘出更多深意。


古老的歌谣口口相传，讲述那鲜为人知的过去，曾有第十三位泰坦，与巨人刻法勒如影随形。
造物之时，刻法勒割开手臂，以血赋予泥人生命。
祂发现，翁法罗斯的众生虽然能跑能跳，眼中却空洞无物。他们只知在这片土地上生老病死，不知企盼与夙愿，宛如只会呼吸的石头。
刻法勒感到困惑。祂看向身旁的无名泰坦。创世的泰坦观察许久，从胸膛中掏出了一颗火星——
其名为「好奇」。
祂将火星吹散，落入泥人的眼中。
顷刻间，泥人们不再低头看着脚下，而是抬头望向星空；泥人们不再满足于果腹之物，而是开始思考山的那边是什么。
「光有生命还不够，」无名泰坦拍着刻法勒的肩膀，「还需要一点点...走向明天的冲动。」


岁月流转，翁法罗斯的生灵日益繁多，世界的重量也与日俱增。
泰坦都在担忧，背负世界的巨人，终有一天会因为不堪重负而倒下。
但那天并没有到来。
「负世」疲惫时，无名泰坦便伸出手，托住刻法勒背上的世界，分担一半的重量。
“我会把世界变得更有趣一点，这样背起来就不累了。”
于是，在 “双子神代”的辉煌岁月里，翁法罗斯没有迎来注定的衰败。
因为「创世」不再是肆意的挥洒，而是为了减轻「负世」之重担。
因为「负世」不再是徒劳的苦役，而是为了绵延「创世」之美好。
正如奥赫玛的铭文所言——
“一人行快，二人行远。”


据说，无名泰坦是一位闲不住的工匠，但它的品味......实在独特。
当瑟希斯创造出精美的植物，吉奥里亚捏出敦实的野兽时，无名泰坦却在捣鼓些没用的东西。
它给兔子安上长耳朵以便聆听风声，把萤火虫的尾巴点亮只为夜里好看，甚至还想给大地兽装上轮子，说是这样跑得比较快。
对于这些造物，众神皆摇头叹息，唯独刻法勒看得入神。甚至还会笨拙地伸出手，帮那带轮子的大地兽推上一把。
......
无名泰坦想要创造风。
祂将气体一股脑抛向空中，造出了撕碎万物的风暴。狂乱的气流四处冲撞，毫无美感可言。
于是，刻法勒竖起山峰，开凿峡谷。
地形如同一把巨大的竖琴，引着气流穿过其间。呼啸渐渐平息，化为山谷的呜咽与林间的低语。
「听，这就是我要的声音！」
「确实不错。这曲子，算我们合写的。」
没有刻法勒，风只是灾难。
但没有无名泰坦，山谷也只会死寂。
这是属于世界的和声。


「岁月」的欧洛尼斯布下“双星陨落”之谶。
双子泰坦终将分离。一个将归于虚无，一个将陷入永恒的轮回。世界将在这一分为二的撕裂中，坠入深渊。
预言令众神惶恐，令大地悲鸣。
然而预言指向的两位泰坦，却异常平静。

“预言只看见了结果，却没有看见过程。” 
“即便时空将我们分离，即便轮回剥夺记忆。只要这世界的重量还在我肩上，只要星空的轨迹还在你眼中——”
“我们就一定会重逢。在终点的终点，在开始的开始。”""", close_action=Hide("scrollable_text_window"))




            textbutton _("███████████") action Show("scrollable_text_window", title="███████████", content_text="""1
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
负世投下多么美丽的句式：因为有了光，所以不再有影子。""", close_action=Hide("scrollable_text_window"))

    if page == 2:
        vbox:
            xanchor 0.0
            yanchor 0.5
            xpos 260
            ypos 750
            spacing 20

            text _("未完待续...")


    if page == 3:
        vbox:
            xanchor 0.0
            yanchor 0.5
            xpos 260
            ypos 750
            spacing 20
            text _("未完待续...")



    imagebutton:
        xpos 30
        ypos 20
        idle "gui/new/chapter_select/return_idle.png"
        hover "gui/new/chapter_select/return_hover.png"
        focus_mask True
        action [SetVariable("in_preferences", False), Return()]

