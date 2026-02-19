init python:
    def forced_dissolve(duration=1.0):
        """
    执行一个不可被跳过的 dissolve 转场。
    
    参数:
        duration: 转场持续时间，默认 1.0 秒。
        
    用法:
        show my_image
        $ forced_dissolve(0.5)
        # 代替: with dissolve (默认为 0.5s)
    """
        
        renpy.transition(Dissolve(duration))
        
        renpy.pause(duration, hard=True)

