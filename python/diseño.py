def setup():
    size(980, 980) # area de trabajo o dibujo
    background(200, 0, 200) # color del fondo
    rect_mode(CENTER) # punto de insercion del rectangulo
    fill(0, 200, 0) # color de la figura (r, g, b)
    stroke(255, 0, 0) # color de las lineas al rededor de la figura (r, g, b)
    stroke_weight(5) # anchura de las lineas
    rect( width / 2, height / 2, 200, 50) # rectangulo (x, y, w, h)
    no_stroke() #no lineas al rededor de la figura
    fill(255) #255-blanco 0-negro 128-gris
    ellipse(200, 200, 300, 100) # (x, y, w, h)    