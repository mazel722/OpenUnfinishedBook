screen scrollable_text_window(title, content_text, close_action=Return()):
    modal True
    zorder 100



    style_prefix "scrollable_text"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800
        padding (40, 40)

        has vbox
        spacing 20


        hbox:
            xfill True


            text title:
                style "scrollable_text_title"
                xalign 0.5
                xfill True
                yalign 0.5


            textbutton "x":
                style "scrollable_text_close_button"
                action close_action
                xalign 1.0
                yalign 0.5


        add Solid("#ffffff") size (1120, 2) alpha 0.3 xalign 0.5


        viewport:
            id "content_viewport"
            scrollbars "vertical"
            mousewheel True
            draggable True


            has vbox
            spacing 15
            xfill True

            text content_text:
                style "scrollable_text_content"




style scrollable_text_frame is frame:
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style scrollable_text_title is text:
    size 40
    color "#ffffff"
    text_align 0.5

style scrollable_text_content is text:
    size 26
    color "#ffffff"
    line_spacing 8
    justify True

style scrollable_text_close_button is button:
    background None
    padding (10, 5)

style scrollable_text_close_button_text is button_text:
    size 40
    color "#cccccc"
    hover_color "#ff6666"







transform chapter_modal_dissolve:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen chapter_announce_window(title, subtitle="", time=2.0):
    modal True
    zorder 200


    timer time action Return()

    fixed:
        at chapter_modal_dissolve


        add Solid("#00000080")

        frame:


            background Solid("#000000")
            xalign 0.5
            yalign 0.5
            padding (80, 50)

            has vbox
            spacing 20
            align (0.5, 0.5)

            text title:
                size 60
                bold True
                align (0.5, 0.5)
                color "#ffffff"
                outlines [(2, "#00000040", 2, 2)]

            if subtitle:
                text subtitle:
                    size 36
                    align (0.5, 0.5)
                    color "#dddddd"


init python:
    def display_chapter(title, subtitle="", time=2.0):
        """
    显示章节名，强制停留指定时间，并允许退出。
    """
        
        renpy.config.skipping = None
        
        
        
        renpy.show_screen("chapter_announce_window", title=title, subtitle=subtitle, time=time)
        renpy.pause(time, hard=True)
        renpy.hide_screen("chapter_announce_window")
        
        renpy.pause(1.0, hard=True)
        renpy.pause(0.5)

