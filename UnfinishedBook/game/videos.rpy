init python:
    def play_resumable_video(video_path, fade_time=0.5):
        """
    播放支持暂停的视频
    参数:
        video_path: 视频路径
        fade_time: 渐入渐出时间（秒）
    """
        
        renpy.music.play(video_path, channel='movie', loop=False, fadein=fade_time)
        
        
        renpy.transition(Dissolve(fade_time))
        
        
        _orig_quit_action = config.quit_action
        config.quit_action = [Function(renpy.music.set_pause, True, channel='movie'), Show("video_pause_menu_new"), Show("quit_confirm")]
        
        
        renpy.call_screen("video_player_screen")
        
        
        config.quit_action = _orig_quit_action
        
        
        renpy.music.stop(channel='movie', fadeout=fade_time)
        
        
        renpy.transition(Dissolve(fade_time))

    def check_video_done():
        if renpy.music.get_pause(channel='movie'):
            return None
        if not renpy.music.get_playing(channel='movie'):
            return True


screen video_player_screen():
    zorder 100
    modal True


    key "game_menu" action [Function(renpy.music.set_pause, True, channel='movie'), Show("video_pause_menu_new")]



    add Movie(channel='movie', size=(1920, 1080))


    textbutton "暂停":
        align (0.95, 0.05)
        text_size 30
        text_color "#ffffff"
        text_outlines [(2, "#000000", 0, 0)]
        action [Function(renpy.music.set_pause, True, channel='movie'), Show("video_pause_menu_new")]


    timer 0.1 repeat True action Function(check_video_done)



screen video_pause_menu_new():
    modal True
    zorder 200

    key "game_menu" action Hide("video_pause_menu_new")

    on "hide" action Function(renpy.music.set_pause, False, channel='movie')

    add Solid("#000000", alpha=0.7)

    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 40)
        background Solid("#2a2a2a")

        has vbox
        spacing 30

        text "是否跳过此视频？" size 40 xalign 0.5 color "#ffffff"

        hbox:
            spacing 50
            xalign 0.5

            textbutton "继续观看":
                xsize 220
                ysize 70
                text_size 32
                text_xalign 0.5

                action Hide("video_pause_menu_new")

            textbutton "跳过视频":
                xsize 220
                ysize 70
                text_size 32
                text_xalign 0.5

                action [Function(renpy.music.stop, channel='movie'), Hide("video_pause_menu_new")]



image burn = Movie(play="videos/burn.webm", side_mask=True, size=(1920, 1080), loop=False)
image goldblood = Movie(play="videos/goldblood.webm", size=(1920, 1080), loop=False)

