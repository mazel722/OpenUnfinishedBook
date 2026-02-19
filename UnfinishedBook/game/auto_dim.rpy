init python:




    IGNORE_DIM_TAGS = ["bg", "black", "white", "solid", "testtest_"]


transform dim_transform:


    matrixcolor TintMatrix("#ffffff")

    linear 0.3 matrixcolor TintMatrix("#606060c4")


transform undim_transform:


    linear 0.3 matrixcolor TintMatrix("#ffffff")

init python:




    dim_transform.is_dim = True
    undim_transform.is_undim = True


    def is_dim_transform(t):
        
        return (t is dim_transform) or getattr(t, "is_dim", False) or ("dim_transform" in repr(t))

    def is_undim_transform(t):
        return (t is undim_transform) or getattr(t, "is_undim", False) or ("undim_transform" in repr(t))





    IGNORE_DIM_TAGS = ["bg", "black", "white", "solid", "testtest_"]

    def highlight_speaker_callback(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "begin":
            speaking_char_tag = renpy.get_say_image_tag()
            showing_tags = renpy.get_showing_tags(layer='master')
            
            
            if not hasattr(highlight_speaker_callback, "last_attrs"):
                highlight_speaker_callback.last_attrs = {}
            current_frame_attrs = {}
            
            for tag in showing_tags:
                if tag in IGNORE_DIM_TAGS:
                    continue
                if tag.lower().startswith("cg") or tag.lower().startswith("seamonster") or tag.lower().startswith("movie"):
                    continue
                
                current_at_list = list(renpy.get_at_list(tag))
                current_attrs = renpy.get_attributes(tag, layer='master')
                current_frame_attrs[tag] = current_attrs
                
                
                attrs_changed = False
                if tag not in highlight_speaker_callback.last_attrs:
                    attrs_changed = True
                elif highlight_speaker_callback.last_attrs[tag] != current_attrs:
                    attrs_changed = True
                
                should_dim = False
                
                if speaking_char_tag:
                    if tag != speaking_char_tag:
                        should_dim = True
                else: 
                    should_dim = False
                
                
                
                
                
                if should_dim:
                    
                    if not any(is_dim_transform(t) for t in current_at_list):
                        new_at = [t for t in current_at_list if not is_undim_transform(t)]
                        new_at.append(dim_transform)
                        
                        image_tuple = (tag,)
                        if current_attrs:
                            image_tuple += current_attrs
                        renpy.show(image_tuple, at_list=new_at)
                else:
                    
                    has_dim = any(is_dim_transform(t) for t in current_at_list)
                    has_undim = any(is_undim_transform(t) for t in current_at_list)
                    
                    if has_dim or not has_undim:
                        new_at = [t for t in current_at_list if not is_dim_transform(t)]
                        if not any(is_undim_transform(t) for t in new_at):
                            new_at.append(undim_transform)
                        
                        image_tuple = (tag,)
                        if current_attrs:
                            image_tuple += current_attrs
                        renpy.show(image_tuple, at_list=new_at)
            
            highlight_speaker_callback.last_attrs = current_frame_attrs

    config.all_character_callbacks.append(highlight_speaker_callback)




    def hook_show_undim(name, at_list=[], layer='master', what=None, zorder=None, tag=None, behind=[], atl=None, **kwargs):
        
        if tag is None:
            if isinstance(name, tuple):
                tag = name[0]
            elif isinstance(name, str):
                tag = name.split()[0]
        
        
        if tag and isinstance(tag, str):
            if tag not in IGNORE_DIM_TAGS and not tag.lower().startswith("cg"):
                
                if renpy.showing(tag, layer=layer):
                    current_at = list(renpy.get_at_list(tag, layer=layer))
                    
                    if any(is_dim_transform(t) for t in current_at):
                        
                        
                        
                        
                        
                        if not at_list:
                            
                            new_transforms = [t for t in current_at if not is_dim_transform(t)]
                            
                            
                            if not any(is_undim_transform(t) for t in new_transforms):
                                new_transforms.append(undim_transform)
                            
                            
                            at_list = new_transforms
        
        
        return renpy.show(name, at_list=at_list, layer=layer, what=what, zorder=zorder, tag=tag, behind=behind, atl=atl, **kwargs)


    config.show = hook_show_undim

