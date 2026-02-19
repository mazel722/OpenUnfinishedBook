image cg temp FlameReaver:
    "temp/FlameReaver.png"
    zoom 0.7

label test:

    $ renpy.music.set_volume(0.1, delay=0, channel='sound')
    play sound "sfx/calendar.mp3" loop
    "1"
    "2"

    $ renpy.music.set_volume(0.7, delay=5.0, channel='sound')
    "3"
    "4"
    "测试可滚动文本窗口"
    call screen scrollable_text_window(
        title="测试用文本",
        content_text="测试用文本内容。\n" * 50)
    "滚动文本窗口测试结束。"
    "测试章节展示弹窗"
    scene white with fade
    $ display_chapter("第一章", "黎明", time=3.0)
    "章节展示弹窗测试结束。"

    scene white with fade
    pause 2.0
    centered "{size=40}{color=#000000}快马踏碎了黎明的薄冰，将那一滴黄金血传遍了六邦十二城。"
    extend "\n\n消息在一夜之间点燃了整个北境。"
    extend "\n\n黄金血，是神明尚未抛弃这片土地的铁证。"
    extend "\n\n人们奔走相告，在街头巷尾，在每一张餐桌前，那个名字——“刻律德菈”，被无数次咀嚼、吞咽。{/color}{/size}"
    centered "{size=40}{color=#000000}战争无止无休，许多东西都将匮乏。"
    extend "\n\n但绝不会匮乏的是痛苦，泥浆，血液和死亡。成千上万的死亡。"
    extend "\n\n......人们都期待和平。"
    extend "\n\n人们说：“她承诺了和平。”{/color}{/size}"

    show cg temp FlameReaver with dissolve
    FlameReaver "你的命运......尚未走到尽头。"
    "准备播放视频..."

    $ play_resumable_video("videos/p1_ch5_2.webm", fade_time=1.0)

    "视频播放结束（或者是被跳过了），游戏继续。"

    "视频真正播完了。"
return

