
def setup():
    size(980, 980)
    background(0)
    noche_estrellada()

def noche_estrellada():
    for _ in range(random_int (100,1000)):
        x = random(100, 900)
        y = random(100, 600)
        fill(255,255,0)
        star(x, y, 10,15, 5)
    estrella_fugaz()
    fill(240)
    circle(800,200, 200)
    fill(0)
    circle(770,170, 200)
          
def estrella_fugaz ():
    for _ in range(random_int(2,5)):
        x = random_int(100, 800)
        y = random_int(200, 700)
        stroke(255)
        line(x, y - 5, x - 50, y - 25)
        line(x, y, x - 80, y - 30)
        line(x, y + 5, x - 40, y - 10)
        no_stroke()
        fill(255, 255, 0)
        star(x, y, 10, 15, 5)
 
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