init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size





style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_idle_bar.png", gui.slider_borders, tile=gui.slider_tile)

    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















transform ui_ani_fade(target_alpha=1.0):

    ease 0.0 alpha target_alpha


screen say(who, what):
    window:
        id "window"

        at ui_ani_fade(0.0 if ui_hidden else 1.0)

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0 at ui_ani_fade(0.0 if ui_hidden else 1.0)





















init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height



    background Image("gui/textbox_4.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)

    xalign gui.name_xalign
    yalign 0.5
    outlines [(2, "#000000", 0, 0)]
    color "#FFD333"



style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    outlines [(2, "#000000", 0, 0)]



    layout "greedy"
    adjust_spacing False









screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xanchor gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width









screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 1.0
    ypos 800
    yanchor 1.0
    spacing gui.choice_spacing

style choice_button:

    background Frame("gui/new/choices/choice_idle.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    hover_background Frame("gui/new/choices/choice_hover.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    focus_mask True

    xsize 550
    yminimum 65


    ypadding 15

style choice_button_text:


    idle_color "#ffffff"
    hover_color "#ffffff"
    size 26
    xpos 65
    ypos 0
    yalign 0.0
    xsize 500

screen choice_center(items):
    style_prefix "choice_center"
    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_center_vbox:
    xalign 0.5

    yalign 0.4

    spacing gui.choice_spacing

style choice_center_button:
    background Frame("gui/new/choices/choice_center_idle.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    hover_background Frame("gui/new/choices/choice_center_hover.png", gui.choice_button_borders, tile=gui.choice_button_tile)
    xsize 696
    yminimum 70

style choice_center_button_text:
    idle_color "#ffffff"
    hover_color "#000000"
    xalign 0.5






image auto_flash:
    contains:
        "gui/rightup/auto_0.png"
    contains:
        "gui/rightup/auto_1.png"
        alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0
        repeat


default ui_hidden = False

screen ui_hider():
    zorder 200
    if ui_hidden:

        button:
            xysize (config.screen_width, config.screen_height)
            background None
            action SetVariable("ui_hidden", False)


screen quick_menu():

    zorder 100

    if quick_menu:
        frame:
            xalign 2.05
            yalign 0.1

            background "gui/rightup/back.png"
            at [Transform(zoom=0.65), ui_ani_fade(0.0 if ui_hidden else 1.0)]


            style_prefix "quick"

            imagebutton:
                idle "gui/rightup/skip_0.png"
                hover "gui/rightup/skip_1.png"
                selected_idle "gui/rightup/skip_1.png"
                selected_hover "gui/rightup/skip_1.png"

                action Skip()

                alternate Skip(fast=True, confirm=True)
                tooltip _("快进")
                xpos -6
                ypos -6
                focus_mask True
                selected renpy.is_skipping()

            imagebutton:
                idle "gui/rightup/auto_0.png"
                hover "gui/rightup/auto_1.png"

                selected_idle "gui/rightup/auto_2.png"

                selected_hover "gui/rightup/auto_2.png"

                action Preference("auto-forward", "toggle")
                tooltip _("自动")
                xpos -6
                ypos -6
                focus_mask True

            imagebutton:
                idle "gui/rightup/hide_0.png"
                action SetVariable("ui_hidden", True)
                hover "gui/rightup/hide_1.png"

                tooltip _("隐藏")
                xpos -6
                ypos -6
                focus_mask True


        frame:
            xalign -0.06
            yalign 0.06

            background im.Flip("gui/leftup/back.png", horizontal=True)
            at [Transform(zoom=0.45), ui_ani_fade(0.0 if ui_hidden else 1.0)]
            has hbox
            xanchor 0.0
            xpos 320
            ypos 15
            spacing 50
            imagebutton:
                idle "gui/leftup/setting.png"
                hover "gui/leftup/setting_hover.png"
                at Transform(zoom=1.9)
                action ShowMenu('preferences')
            imagebutton:
                idle "gui/leftup/history.png"
                hover "gui/leftup/history_hover.png"
                at Transform(zoom=1.9)
                action ShowMenu('history')




















init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("ui_hider")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")

init python:

    in_preferences = False










image start_button_hover_anim:
    "gui/new/button/start_0.png"

    "gui/new/button/start_2.png" with Dissolve(0.5, alpha=True)


transform dissolve_fade:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

screen navigation():





    add Movie(play="videos/lizi/output.webm", side_mask=True, loop=True, size=(1920, 1080)) at dissolve_fade


    if main_menu and not in_preferences:
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/start_2.png"

            focus_mask "gui/new/main_menu/start_2.png"
            action Start("p1_ch1")
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/chapterselect_1.png"
            focus_mask "gui/new/main_menu/chapterselect_1.png"
            action ShowMenu("chapter_select")

        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/about_1.png"
            focus_mask "gui/new/main_menu/about_1.png"
            action [SetVariable("in_preferences", True), ShowMenu("about")]
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/quit_1.png"
            focus_mask "gui/new/main_menu/quit_1.png"
            action ShowMenu("quit_confirm")
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/read_1.png"
            focus_mask "gui/new/main_menu/read_1.png"
            action ShowMenu("read_screen")
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/preferences_1.png"
            focus_mask "gui/new/main_menu/preferences_1.png"
            action [SetVariable("in_preferences", True), ShowMenu("preferences")]
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/load_1.png"
            focus_mask "gui/new/main_menu/load_1.png"
            action [SetVariable("in_preferences", True), ShowMenu("load")]
        imagebutton:
            idle "gui/new/main_menu/idle.png"
            hover "gui/new/main_menu/help_1.png"
            focus_mask "gui/new/main_menu/help_1.png"
            action [SetVariable("in_preferences", True), ShowMenu("help")]

        text "主界面" xpos 1530 ypos 932 size 28 color "#ffffffe1"

        text "[__import__('datetime').datetime.now().strftime('%H:%M')]" xanchor 1.0 xpos 1750 ypos 932 size 28 color "#ffffffe1"

    else:



        style_prefix "navigation"











        if main_menu:




            imagebutton:
                idle "gui/new/main_preferences/startbutton_idle.png"
                hover "gui/new/main_preferences/startbutton_hover.png"
                selected_idle "gui/new/main_preferences/startbutton_hover.png"
                focus_mask "gui/new/main_preferences/startbutton_idle.png"
                action Start("p1_ch1")

            imagebutton:
                idle "gui/new/main_preferences/loadbutton_idle.png"
                hover "gui/new/main_preferences/loadbutton_hover.png"
                selected_idle "gui/new/main_preferences/loadbutton_hover.png"
                focus_mask "gui/new/main_preferences/loadbutton_idle.png"
                action ShowMenu("load")

            imagebutton:
                idle "gui/new/main_preferences/preferencesbutton_idle.png"
                hover "gui/new/main_preferences/preferencesbutton_hover.png"
                selected_idle "gui/new/main_preferences/preferencesbutton_hover.png"
                focus_mask "gui/new/main_preferences/preferencesbutton_idle.png"
                action ShowMenu("preferences")

            imagebutton:
                idle "gui/new/main_preferences/aboutbutton_idle.png"
                hover "gui/new/main_preferences/aboutbutton_hover.png"
                selected_idle "gui/new/main_preferences/aboutbutton_hover.png"
                focus_mask "gui/new/main_preferences/aboutbutton_idle.png"
                action ShowMenu("about")

            imagebutton:
                idle "gui/new/main_preferences/quitbutton_idle.png"
                hover "gui/new/main_preferences/quitbutton_hover.png"
                selected_idle "gui/new/main_preferences/quitbutton_hover.png"
                focus_mask "gui/new/main_preferences/quitbutton_idle.png"
                action Quit(confirm=not main_menu)

            imagebutton:
                idle "gui/new/main_preferences/helpbutton_idle.png"
                hover "gui/new/main_preferences/helpbutton_hover.png"
                selected_idle "gui/new/main_preferences/helpbutton_hover.png"
                focus_mask "gui/new/main_preferences/helpbutton_idle.png"
                action ShowMenu("help")


        else:
            imagebutton:
                idle "gui/new/preferences/historybutton_idle.png"
                hover "gui/new/preferences/historybutton_hover.png"
                selected_idle "gui/new/preferences/historybutton_hover.png"
                focus_mask "gui/new/preferences/historybutton_idle.png"
                action ShowMenu("history")


            imagebutton:
                idle "gui/new/preferences/savebutton_idle.png"
                hover "gui/new/preferences/savebutton_hover.png"
                selected_idle "gui/new/preferences/savebutton_hover.png"
                focus_mask "gui/new/preferences/savebutton_idle.png"
                action ShowMenu("save")




            imagebutton:
                idle "gui/new/preferences/loadbutton_idle.png"
                hover "gui/new/preferences/loadbutton_hover.png"
                selected_idle "gui/new/preferences/loadbutton_hover.png"
                focus_mask "gui/new/preferences/loadbutton_idle.png"
                action ShowMenu("load")


            imagebutton:
                idle "gui/new/preferences/preferencesbutton_idle.png"
                hover "gui/new/preferences/preferencesbutton_hover.png"
                selected_idle "gui/new/preferences/preferencesbutton_hover.png"
                focus_mask "gui/new/preferences/preferencesbutton_idle.png"
                action ShowMenu("preferences")





            if _in_replay:

                textbutton _("结束回放") action EndReplay(confirm=True)

            elif not main_menu:
                imagebutton:
                    idle "gui/new/preferences/titlebutton_idle.png"
                    hover "gui/new/preferences/titlebutton_hover.png"
                    selected_idle "gui/new/preferences/titlebutton_hover.png"
                    focus_mask "gui/new/preferences/titlebutton_idle.png"

                    action ShowMenu("main_menu_confirm")




            imagebutton:
                idle "gui/new/preferences/aboutbutton_idle.png"
                hover "gui/new/preferences/aboutbutton_hover.png"
                selected_idle "gui/new/preferences/aboutbutton_hover.png"
                focus_mask "gui/new/preferences/aboutbutton_idle.png"
                action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):



                imagebutton:
                    idle "gui/new/preferences/helpbutton_idle.png"
                    hover "gui/new/preferences/helpbutton_hover.png"
                    selected_idle "gui/new/preferences/helpbutton_hover.png"
                    focus_mask "gui/new/preferences/helpbutton_idle.png"
                    action ShowMenu("help")

            if renpy.variant("pc"):



                imagebutton:
                    idle "gui/new/preferences/quitbutton_idle.png"
                    hover "gui/new/preferences/quitbutton_hover.png"
                    selected_idle "gui/new/preferences/quitbutton_hover.png"
                    focus_mask "gui/new/preferences/quitbutton_idle.png"
                    action ShowMenu("quit_confirm")




style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")








screen main_menu():
    tag menu



    add gui.main_menu_background






    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.first_run_seen:
        timer 0.5 action Show("scrollable_text_window", title=_("欢迎"), content_text=_("""本游戏为《崩坏：星穹铁道》白厄中心向的无盈利二创同人游戏，官方享有原作最终解释权。请勿对本作进行恶意篡改、恶搞，以及在不适合的地方提及本作等行为。
非常感谢您体验本游戏，我们诚挚得希望您拥有美好的体验。"""), close_action=[SetField(persistent, "first_run_seen", True), Hide("scrollable_text_window")])


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")










screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"


    if main_menu:

        add gui.game_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    spacing spacing

                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    spacing spacing

                    transclude

            else:

                transclude

    use navigation

    imagebutton:
        xpos 30
        ypos 960
        idle "gui/new/chapter_select/return_idle.png"
        hover "gui/new/chapter_select/return_hover.png"
        focus_mask True
        action [SetVariable("in_preferences", False), Return()]





    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180



style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45









screen about():
    tag menu




    use game_menu(_(""), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")

    text _("关于") xalign 0.1 ypos 83 size 40 color "#FFFFFF"


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size










screen save():
    tag menu


    use file_slots(_(""))
    add "gui/new/save_load/page.png" xpos 0 ypos 0
    text _("保存") xalign 0.1 ypos 83 size 40 color "#FFFFFF"


screen load():
    tag menu


    use file_slots(_(""))
    if not renpy.variant("mobile"):
        add "gui/new/save_load/page.png" xpos 0 ypos 0
    else:
        add "gui/new/save_load/page.png" xpos 90 ypos -15
    text _("读取游戏") xalign 0.1 ypos 83 size 40 color "#FFFFFF"



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:


            order_reverse True


            $ page_name_str = FilePageName(auto=_("自动存档"), quick=_("快速存档"))
            if page_name_str.isdigit():
                $ page_name_str = _("第 {} 页").format(page_name_str)

            label page_name_str:
                style "page_label"
                xpos 663
                ypos 0



            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)


                        idle_background "gui/new/save_load/slot_idle.png"
                        hover_background "gui/new/save_load/slot_hover.png"
                        hover_foreground "gui/new/save_load/slot_fore_hover.png"
                        insensitive_background "gui/new/save_load/slot_idle.png"
                        focus_mask True
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)




            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.9

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("上传同步"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("下载同步"):
                            action DownloadSync()
                            xalign 0.5



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    size 25
    hover_color gui.hover_color
    font "albbpht.otf"

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")









screen preferences():
    tag menu





    use game_menu(_(""), scroll="viewport")






































































    vbox:
        xpos 500
        ypos 200



        if renpy.variant("pc") or renpy.variant("web"):
            fixed:
                fit_first True

                add "gui/new/setting/back.png"

                text _("显示") xalign 0.05 ypos 20 size 26 color "#FFFFFF"

                text _("全屏") xanchor 0.5 xpos 830 yalign 0.5 size 26 color "#FFFFFF"
                imagebutton:
                    idle "gui/new/setting/left_idle.png"
                    hover "gui/new/setting/left_hover.png"
                    selected_idle "gui/new/setting/left_hover.png"
                    selected_hover "gui/new/setting/left_hover.png"
                    focus_mask True
                    action Preference("display", "fullscreen")

                text _("窗口") xanchor 0.5 xpos 1130 yalign 0.5 size 26 color "#FFFFFF"
                imagebutton:
                    idle "gui/new/setting/right_idle.png"
                    hover "gui/new/setting/right_hover.png"
                    selected_idle "gui/new/setting/right_hover.png"
                    selected_hover "gui/new/setting/right_hover.png"
                    focus_mask True
                    action Preference("display", "window")


        fixed:
            fit_first True

            add "gui/new/setting/back.png"
            text _("文字速度") xalign 0.05 ypos 20 size 26 color "#FFFFFF"



            add "gui/new/setting/basebar.png":
                align (0.925, 0.5)


            bar:
                value Preference("text speed")
                style "slider"


                left_bar Null()
                right_bar Null()


                thumb "gui/new/setting/thumb.png"

                xsize 550
                ysize 50

                align (0.925, 0.5)

        fixed:
            fit_first True

            add "gui/new/setting/back.png"
            text _("自动前进时间") xalign 0.05 ypos 20 size 26 color "#FFFFFF"



            add "gui/new/setting/basebar.png":
                align (0.925, 0.5)


            bar:
                value Preference("auto-forward time")
                style "slider"


                left_bar Null()
                right_bar Null()


                thumb "gui/new/setting/thumb.png"

                xsize 550
                ysize 50

                align (0.925, 0.5)

        fixed:
            fit_first True

            add "gui/new/setting/back.png"
            text _("音乐音量") xalign 0.05 ypos 20 size 26 color "#FFFFFF"



            add "gui/new/setting/basebar.png":
                align (0.925, 0.5)


            bar:
                value Preference("music volume")
                style "slider"


                left_bar Null()
                right_bar Null()


                thumb "gui/new/setting/thumb.png"

                xsize 550
                ysize 50

                align (0.925, 0.5)


        fixed:
            fit_first True

            add "gui/new/setting/back.png"
            text _("音效音量") xalign 0.05 ypos 20 size 26 color "#FFFFFF"



            add "gui/new/setting/basebar.png":
                align (0.925, 0.5)


            bar:
                value Preference("sound volume")
                style "slider"


                left_bar Null()
                right_bar Null()


                thumb "gui/new/setting/thumb.png"

                xsize 550
                ysize 50

                align (0.925, 0.5)

        fixed:
            fit_first True

            add "gui/new/setting/back.png"
            text _("语音音量") xalign 0.05 ypos 20 size 26 color "#FFFFFF"



            add "gui/new/setting/basebar.png":
                align (0.925, 0.5)


            bar:
                value Preference("voice volume")
                style "slider"


                left_bar Null()
                right_bar Null()


                thumb "gui/new/setting/thumb.png"

                xsize 550
                ysize 50

                align (0.925, 0.5)

        fixed:
            fit_first True

            add "gui/new/setting/back.png"

            text _("全部静音") xalign 0.05 ypos 20 size 26 color "#FFFFFF"

            text _("开") xanchor 0.5 xpos 830 yalign 0.5 size 26 color "#FFFFFF"
            imagebutton:
                idle "gui/new/setting/left_idle.png"
                hover "gui/new/setting/left_hover.png"
                selected_idle "gui/new/setting/left_hover.png"
                focus_mask True
                action Preference("all mute", "enable")

            text _("关") xanchor 0.5 xpos 1130 yalign 0.5 size 26 color "#FFFFFF"
            imagebutton:
                idle "gui/new/setting/right_idle.png"
                hover "gui/new/setting/right_hover.png"
                selected_idle "gui/new/setting/right_hover.png"
                focus_mask True
                action Preference("all mute", "disable")

    text _("设置") xalign 0.1 ypos 83 size 40 color "#FFFFFF"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675









screen history():
    tag menu



    predict False

    use game_menu("", scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        text_size 30

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                    size 30

        if not _history_list:
            label _("尚无对话历史记录。") text_size 30 text_color "#ffffff"

    text _("历史") xalign 0.1 ypos 83 size 40 color "#FFFFFF"

style chapter_select_label:
    size 40
    bold True
    xalign 0.5



style chapter_select_button:
    xpadding 40
    ypadding 10


style chapter_select_button_text is button_text:
    size 28
    idle_color "#ffffff"
    hover_color "#d4d0d07c"




transform fade_in_out_effect:
    alpha 0.0
    linear 0.1 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0


screen effect_image_overlay(img_path):
    zorder 200
    add img_path at fade_in_out_effect align (0.5, 0.5)
    timer 1.5 action Hide("effect_image_overlay")

screen chapter_select():
    tag menu

    add "gui/new/chapter_select/back.jpg"

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
            yanchor 0.5
            xpos 260
            ypos 750
            spacing 20
            textbutton _("Chapter 1     浪潮啊，诉说那不归征途") action Start("p1_ch1") style "chapter_select_button"
            textbutton _("Chapter 2     火光啊，为我等以血加冕") action Start("p1_ch2") style "chapter_select_button"
            textbutton _("Chapter 3     金血啊，联结最初的谎言") action Start("p1_ch3") style "chapter_select_button"
        vbox:
            xanchor 0.0
            yanchor 0.5
            xpos 1080
            ypos 750
            spacing 20
            textbutton _("Chapter 4     天平啊，称量这诸世不公") action Start("p1_ch4") style "chapter_select_button"
            textbutton _("Chapter 5     剑琴啊，奏响凯歌与征服") action Start("p1_ch5") style "chapter_select_button"
            textbutton _("Chapter 6     ████████████████") action Start("p1_ch6") style "chapter_select_button"

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




define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    font "msyh.ttf"
    size 25


style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font "msyh.ttf"
    size 22

style history_label:
    xfill True

style history_label_text:
    xalign 0.5







screen help():
    tag menu


    default device = "keyboard"



    use game_menu(_(""), scroll="viewport"):

        style_prefix "help"


        null height 100

        vbox:
            spacing 23









            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help



    imagebutton:
        xpos 0 ypos 0
        idle "gui/new/help/mouse_idle.png"
        hover "gui/new/help/mouse_hover.png"
        selected_idle "gui/new/help/mouse_hover.png"
        focus_mask True
        action SetScreenVariable("device", "mouse")

    imagebutton:
        xpos 0 ypos 0
        idle "gui/new/help/keyboard_idle.png"
        hover "gui/new/help/keyboard_hover.png"
        selected_idle "gui/new/help/keyboard_hover.png"
        focus_mask True
        action SetScreenVariable("device", "keyboard")

    if GamepadExists():
        imagebutton:
            xpos 0 ypos 0
            idle "gui/new/help/handle_idle.png"
            hover "gui/new/help/handle_hover.png"
            selected_idle "gui/new/help/handle_hover.png"
            focus_mask True
            action SetScreenVariable("device", "gamepad")
    text _("帮助") xalign 0.1 ypos 83 size 40 color "#FFFFFF"


screen keyboard_help():

    hbox:
        label _("回车") text_color "#ffffff"
        text _("推进对话并激活界面。")

    hbox:
        label _("空格") text_color "#ffffff"
        text _("在没有选择的情况下推进对话。")

    hbox:
        label _("方向键") text_color "#ffffff"
        text _("导航界面。")

    hbox:
        label _("Esc") text_color "#ffffff"
        text _("访问游戏菜单。")

    hbox:
        label _("键盘") text_color "#ffffff"
        text _("按住时快进对话。")

    hbox:
        label _("Tab") text_color "#ffffff"
        text _("切换对话快进。")

    hbox:
        label _("上一页") text_color "#ffffff"
        text _("回退至先前的对话。")

    hbox:
        label _("下一页") text_color "#ffffff"
        text _("向前至后来的对话。")

    hbox:
        label "H" text_color "#ffffff"
        text _("隐藏用户界面。")

    hbox:
        label "S" text_color "#ffffff"
        text _("截图。")





    hbox:
        label "Shift+A" text_color "#ffffff"
        text _("打开无障碍菜单。")


screen mouse_help():

    hbox:
        label _("左键点击") text_color "#ffffff"
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击") text_color "#ffffff"
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击") text_color "#ffffff"
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上") text_color "#ffffff"
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下") text_color "#ffffff"
        text _("向前至后来的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键") text_color "#ffffff"
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键") text_color "#ffffff"
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键") text_color "#ffffff"
        text _("向前至后来的对话。")

    hbox:
        label _("十字键，摇杆") text_color "#ffffff"
        text _("导航界面。")

    hbox:
        label _("开始，向导，B/右键") text_color "#ffffff"
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键") text_color "#ffffff"
        text _("隐藏用户界面。")




style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0














screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 150

            textbutton _("确定") action yes_action
            textbutton _("取消") action no_action


    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")








screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("正在快进")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:

    font "DejaVuSans.ttf"








screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id



define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")










screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}







style pref_vbox:
    variant "medium"
    xsize 675




screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        frame:
            xalign 2.05
            yalign 0.1

            background "gui/rightup/back.png"
            at [Transform(zoom=0.65), ui_ani_fade(0.0 if ui_hidden else 1.0)]

            style_prefix "quick"

            imagebutton:
                idle "gui/rightup/skip_0.png"
                hover "gui/rightup/skip_1.png"
                selected_idle "gui/rightup/skip_1.png"
                selected_hover "gui/rightup/skip_1.png"
                action Skip()
                alternate Skip(fast=True, confirm=True)
                tooltip _("快进")
                xpos -6
                ypos -6
                focus_mask True
                selected renpy.is_skipping()

            imagebutton:
                idle "gui/rightup/auto_0.png"
                hover "gui/rightup/auto_1.png"


                selected_idle "gui/rightup/auto_2.png"
                selected_hover "gui/rightup/auto_2.png"
                action Preference("auto-forward", "toggle")
                tooltip _("自动")
                xpos -6
                ypos -6
                focus_mask True

            imagebutton:
                idle "gui/rightup/hide_0.png"
                action SetVariable("ui_hidden", True)
                hover "gui/rightup/hide_1.png"
                tooltip _("隐藏")
                xpos -6
                ypos -6
                focus_mask True
        frame:
            xalign -0.06
            yalign 0.06

            background im.Flip("gui/leftup/back.png", horizontal=True)
            at [Transform(zoom=0.45), ui_ani_fade(0.0 if ui_hidden else 1.0)]
            has hbox
            xanchor 0.0
            xpos 320
            ypos 15
            spacing 50
            imagebutton:
                idle "gui/leftup/setting.png"
                hover "gui/leftup/setting_hover.png"
                at Transform(zoom=1.9)
                action ShowMenu('preferences')
            imagebutton:
                idle "gui/leftup/history.png"
                hover "gui/leftup/history_hover.png"
                at Transform(zoom=1.9)
                action ShowMenu('history')







style window:
    variant "small"



style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"



style game_menu_outer_frame:
    variant "small"


style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900




style my_text:
    size 36
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

screen custom_video_player(video_path):
    modal True

    key "game_menu"




    add Movie(play=video_path, loop=False)


    timer 0.1 action Return() repeat True




screen quit_confirm:

    modal True
    zorder 201

    add Solid("#00000080")

    add "gui/new/jump_window/window.png"


    text _("您确定要退出吗？") xalign 0.5 ypos 360 size 40 color "#ffffff" outlines [(2, "#000000", 0, 0)]

    imagebutton action Quit(confirm=False):
        idle "gui/new/jump_window/yes_idle.png"
        hover "gui/new/jump_window/yes_hover.png"
        focus_mask True

    imagebutton action Hide("quit_confirm", Dissolve(0.5)):
        idle "gui/new/jump_window/no_idle.png"
        hover "gui/new/jump_window/no_hover.png"
        focus_mask True

screen quit_confirm_1:

    modal True
    zorder 200

    add Solid("#00000080")

    add "gui/new/jump_window/window.png"


    text _("您确定要退出吗？") xalign 0.5 ypos 360 size 40 color "#ffffff" outlines [(2, "#000000", 0, 0)]

    imagebutton action Quit(confirm=False):
        idle "gui/new/jump_window/yes_idle.png"
        hover "gui/new/jump_window/yes_hover.png"
        focus_mask True

    imagebutton action [Hide("quit_confirm", Dissolve(0.5)), Pause(0.5), Return()]:
        idle "gui/new/jump_window/no_idle.png"
        hover "gui/new/jump_window/no_hover.png"
        focus_mask True



screen main_menu_confirm:
    modal True
    zorder 200
    add Solid("#00000080")

    add "gui/new/jump_window/window.png"


    text _("您确定要返回到标题界面吗？\n此操作将会使未保存的进度丢失。") xalign 0.5 ypos 335 size 40 color "#ffffff" outlines [(2, "#000000", 0, 0)] text_align 0.5

    imagebutton action MainMenu(confirm=False):
        idle "gui/new/jump_window/yes_idle.png"
        hover "gui/new/jump_window/yes_hover.png"
        focus_mask True

    imagebutton action Hide("main_menu_confirm", Dissolve(0.5)):
        idle "gui/new/jump_window/no_idle.png"
        hover "gui/new/jump_window/no_hover.png"
        focus_mask True




style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color "#ffffff"
    size 36

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    color "#ffffff"
    hover_color "#ffaa00"
    size 28

