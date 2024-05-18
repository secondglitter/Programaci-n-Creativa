
def setup():
    size(980, 980)
    background(255)
    
    for x in range ( 100, 1000, 100):
        for y in range (100, 800, 100):
            n = random_int(1,6)
            print(n, x, y)
            if n <= 2:
                fill(255)
                rect_mode(CENTER)
                square(x,y, 50)
                fill(0)
                rect_mode(CENTER)
                square(x,y, 30)
            elif n <= 4:
                fill(255)
                circle(x, y, 50)
                fill(0)
                circle(x, y, 30)
            else:
                p = random_int (5, 8)
                fill(0)
                star(x,y, 10, 30, p)
                fill(255)
                star(x,y, 5, 15, p)

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