#Crea un elemento gráfico/visual compuesto. Defina una función que dibuje estas instrucciones.
#Utiliza su función para hacer una composición con 3 o más ejemplos del elemento.

#Para los colores de las estrellas
# Blanco-(255)  Amarrillo-(255,255,0)

#Para los tamaños de las estrellas (x,y,10,15,5) o (x,y,5,10,5)

def setup():
    size(960, 960)
    background(0)
    noche_estrellada()

def noche_estrellada():
    estrella_fugaz()
    fill(240)
    circle(800,200, 200)
    fill(0)
    circle(770,170, 200)
    for _ in range(random_int (40,45)):
        x = random(20, 450)
        y = random(10, 750)
        fill(255)
        star(x, y, 5,10, 5)
    for _ in range(random_int (40,45)):
        x = random(460, 900)
        y = random(10, 750)
        fill(255)
        star(x, y, 5,10, 5)
          
def estrella_fugaz ():
    for _ in range(random_int(2,5)):
        x = random_int(100, 800)
        y = random_int(200, 700)
        stroke(255)
        line(x, y - 5, x - 50, y - 25)
        line(x, y, x - 80, y - 30)
        line(x, y + 5, x - 40, y - 10)
        no_stroke()
        fill(255)
        star(x, y, 5, 10, 5)
 
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