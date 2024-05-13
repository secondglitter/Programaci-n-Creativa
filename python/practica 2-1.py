
# Realiza un dibujo con los elementos: rectángulos, círculos, polígonos, ojo y estrella.

# Identifica los que más te gusten y elige colores RGB para el relleno (fill()) y el contorno (stroke()),
#o úsalos sin relleno (no_fill()) o sin contorno (no_stroke()), posicionándolos en el Pantalla en una composición interesante.

def setup():
    size(980, 980)
    background(0)
    
    for y in range (100, 800, 100):
        x = random_int (100, 500)
        ojo (x, y, 200)
    
    for y in range (100, 800, 100):
        x = random_int (500, 900)
        ojo (x, y, 200)


def ojo(x, y, w):
    r= random_int(255)
    g= random_int(255)
    b= random_int(255)
    no_stroke() 
    fill(255)
    ellipse(x, y, w, w /3)
    fill (r,g,b)
    ellipse(x, y, w /3, w /3)
    fill (0)
    ellipse(x, y, w * 0.1, w * 0.1)
    fill(255)
    r = random_int(4,9)
    star(x, y, 15, 30, r)
    
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