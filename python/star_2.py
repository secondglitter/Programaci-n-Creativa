
def setup():
    size(980, 980)
    background(0)
    
    star(300, 300, 200, 100, 4)
    star(500, 500, 150, 50, 4)
    
def star (cx, cy, ra, rb, np, start_ang=0):
    step = TWO_PI / np
    begin_shape()
    for i in range(np):
        ang = start_ang + step * i + frame_count / 50.0
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex (ax, ay)
        bx = cx  + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex (bx, by)
    end_shape(CLOSE)