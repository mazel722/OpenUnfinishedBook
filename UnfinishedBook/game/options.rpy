












define config.name = _("未竟之书")




define gui.show_name = False





define config.version = "1.0.20260217"


define config.quit_action = ShowMenu("quit_confirm_1")









define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.has_sync = False



define config.main_menu_music = "audio/music/Till We Meet Again.mp3"





define gui.about = _p("""
""")


init python:

    _current_character = None

    def store_character_callback(who, *args, **kwargs):
        """存储当前说话的角色对象"""
        global _current_character
        _current_character = who
        
        return args, kwargs

    def auto_voice_function(id):
        """自动语音函数：根据角色的 voice_tag 和对话 id 生成语音文件路径"""
        global _current_character
        
        chapter = id.split('_')[1]
        part_num = chapter[0]
        ch_num = chapter[-1]
        number_part = id.split('_')[-1]
        
        
        print("[DEBUG] _current_character 类型: {}".format(type(_current_character)))
        print("[DEBUG] _current_character 值: {}".format(_current_character))
        print("[DEBUG] 接收到的 id: {}".format(id))
        print("[DEBUG] 当前章节: {}".format(chapter))
        
        
        if 'Trailblazerreverse' in id:
            
            parts = id.split('_')  
            
            number_part = parts[-1]  
            
            sex_value = renpy.store.reverse_sex
            if sex_value == 'female':
                voice_tag_player = 'Trailblazerfemale'
            else:
                voice_tag_player = 'Trailblazermale'
            
            path = "part{}_ch{}/{}_{}_{}.mp3".format(part_num, ch_num, chapter, voice_tag_player, number_part)
            print("[AUTO VOICE DEBUG] 玩家角色 | 性别: {} | voice_tag: {} | 路径: {}".format(
            sex_value, voice_tag_player, path))
            return path
        elif 'Trailblazer' in id:
            
            parts = id.split('_')  
            number_part = parts[-1]  
            
            sex_value = renpy.store.sex
            if sex_value == 'female':
                voice_tag_player = 'Trailblazerfemale'
            else:
                voice_tag_player = 'Trailblazermale'
            
            path = "part{}_ch{}/{}_{}_{}.mp3".format(part_num, ch_num, chapter, voice_tag_player, number_part)
            print("[AUTO VOICE DEBUG] 玩家角色 | 性别: {} | voice_tag: {} | 路径: {}".format(
            sex_value, voice_tag_player, path))
            return path
        
        
        
        
        voice_tag = getattr(_current_character, 'voice_tag', '')
        if _current_character == "[user_name]":
            voice_tag = 'Trailblazerfemale' if renpy.store.sex == 'female' else 'Trailblazermale'
        elif len(id.split('_')) >= 4:
            voice_tag = id.split('_')[-2]
        
        print("[DEBUG] 获取到的 voice_tag: {}".format(voice_tag))
        
        if voice_tag is None:
            
            path = "part{}_ch{}/{}__{}.mp3".format(part_num, ch_num, chapter, number_part)
            print("[AUTO VOICE DEBUG] 旁白 - 路径: {}".format(path))
            return path
        
        path = "part{}_ch{}/{}_{}_{}.mp3".format(part_num, ch_num, chapter, voice_tag, number_part)
        print("[AUTO VOICE DEBUG] 角色: {} | part: {} | voice_tag: {} | id: {} | 路径: {}".format(
        getattr(_current_character, 'name', 'Unknown'), part_num, voice_tag, id, path))
        return path


    config.say_arguments_callback = store_character_callback

define config.auto_voice = auto_voice_function





define build.name = "未竟之书"


transform flashing_text:
    alpha 0.5
    linear 1.0 alpha 1.0
    pause 0.5
    linear 1.5 alpha 0.5
    repeat

label splashscreen:




    show logo at center
    pause 3.5


    show mianze at center with Fade(1.0, 2.0, 1.0)
    hide logo
    pause 3.5

    play music "audio/music/Till We Meet Again.mp3" fadein 1.0
    show splash_image at center with Fade(1.0, 2.0, 1.0)
    hide mianze
    pause 1.0

    image splash_text = Text("{size=40}点击屏幕进入游戏{/size}", outlines=[(2, "#000000", 0, 0)])


    show splash_text at flashing_text with dissolve:
        xalign 0.5
        yalign 0.85







    pause


    hide splash_text
    hide splash_image
    with Dissolve(0.5)

    return








define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.end_splash_transition = dissolve



define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)






default preferences.text_cps = 30




default preferences.afm_time = 15




default preferences.skip_unseen = True














define config.save_directory = "UnfinishedBook-1765372168"






define config.window_icon = "gui/window_icon.png"






init python:
















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.save', None)
    build.classify('saves/**.save', None)
    build.classify('**.text', None)
    build.classify('**.md', None)
    build.classify('saves/persistent', None)



    build.classify('game/**.webm', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.json', 'archive')
    build.classify('game/**.py', 'archive')



    build.documentation('*.html')
    build.documentation('*.txt')
return

