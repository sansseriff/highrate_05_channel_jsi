from typing import List


def bisect(layout: List[float], direction="vert", offset = 0.5, spacing=0.05, absolute_spacing = False):


    x = layout[0]
    y = layout[1]
    width = layout[2]
    height = layout[3]




    if direction != "vert":
        # horizontal bisect
        if not absolute_spacing: 
            spacing = spacing*height
        return [x,y, width, height*offset - spacing/2], [x,height*offset + (spacing/2), width, height*(1-offset) - (spacing/2)]
    else:
        # vertical bisect
        if not absolute_spacing: 
            spacing = spacing*width
        return [x,y,width*offset - spacing/2, height], [width*offset + (spacing/2), y, width*(1-offset) - spacing/2, height]
    

def margin(layout: List[float], w=0.1):
    x = layout[0]
    y = layout[1]
    width = layout[2]
    height = layout[3]
    return [x+w, y+w, width-w, height-w]
    
