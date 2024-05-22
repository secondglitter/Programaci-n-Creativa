
def setup():
    size(800, 800)
    background(100)
    
    columnas = 10
    filas = 10
    off_x = 50 #margen
    w = (width - 2 * off_x) / columnas
    off_y = (height - w * filas) / 2 #margin y
    
    for i in range(columnas):
        x = off_x + i * w + w / 2
        print(x)
        for j in range(filas):
            y = off_y + j * w + w / 2
            star(x, y, w / 3, w / 6, 2 + i)
        
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