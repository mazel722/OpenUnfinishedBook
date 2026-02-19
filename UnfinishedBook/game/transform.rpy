init:
    transform cyber_glitch_v3:

        matrixcolor BrightnessMatrix(0.05) * TintMatrix("#e0f7ff")


        block:

            choice:
                parallel:
                    linear 0.01 xoffset 12
                    linear 0.01 xoffset -8
                    linear 0.01 xoffset 0
                parallel:
                    matrixcolor TintMatrix("#0033ff") * BrightnessMatrix(0.4)
                    pause 0.03
                    matrixcolor TintMatrix("#e0f7ff") * BrightnessMatrix(0.05)


            choice:
                parallel:
                    linear 0.05 zoom 1.005
                    linear 0.05 zoom 1.0
                parallel:
                    alpha 0.6
                    pause 0.02
                    alpha 1.0


            choice:
                pause 0.8


            choice:
                pause 0.2

            repeat


transform shake:

    xoffset 0

    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10

    linear 0.05 xoffset 0


transform v_shake:
    yoffset 0
    linear 0.05 yoffset -10
    linear 0.05 yoffset 10
    linear 0.05 yoffset -10
    linear 0.05 yoffset 10
    linear 0.05 yoffset 0



transform scene_look_around:

    zoom 1.3
    align (0.5, 0.5)






    ease 1.5 align (0.8, 0.5)

    ease 1.5 align (0.2, 0.5)
    ease 2.0 align (0.5, 0.5) zoom 1.0


transform scene_zoom_door_in:
    zoom 1.0 yoffset 0
    ease 5.0 zoom 2.0 yoffset 1000

transform scene_zoom_titan_in:
    zoom 1.0 yoffset 0
    ease 3.0 zoom 1.5 yoffset 500



transform char_black:

    matrixcolor TintMatrix("#000000")







transform char_half_gray:

    matrixcolor TintMatrix("#000000de")


transform faded_memory:


    matrixcolor TintMatrix("#ffdcb9") * SaturationMatrix(0.4)


    blur 0.5





transform continuous_shake:
    xoffset 0
    linear 0.05 yoffset -15
    linear 0.05 yoffset 15
    repeat

