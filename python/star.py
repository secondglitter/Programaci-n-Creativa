
def setup():
    size(980, 980)
    background(148)
    
    # shape sirve para dibujar poligonos
    #vertex es el punto donde esta cada uno y el siguien es en donde se conectara vertex(x, y)
    #begin_shape lo inicia, end_shape lo cierra, pero al poner dentro del end_shape CLOSE sirve para que conecte el ultimo con el primero
    
    begin_shape()
    vertex(50, 300)
    vertex(150, 300)
    vertex(50, 500)
    vertex(150, 500)
    end_shape(CLOSE)
    
    # otra manera de hacerlo es con una lista
    
    pts = [(750, 300,), (850, 300), (750, 500), (850, 500)]
    
    begin_shape()
    for x, y in pts:
        vertex(x, y)
    end_shape(CLOSE)
    
    #para hacer una estrella
    wa = 300
    wb = 100
    #para hacerlo solo despues del cuarto solo es repetir los primeros cuatro, pero invirtiendo los signos
    pt = [ (-wa, -wa), (0, -wb), (wa, -wa), (wb, 0),
           (wa, wa), (0, wb), (-wa, wa), (-wb, 0)]
    
    # como los valores son muy negativos no se vera asi que aqui asignamos unos valores para que aparesca
    xc, yc = 450, 450
    begin_shape()
    for x, y in pt:
        #aqui se los sumamos
        vertex(xc + x, yc + y)
    end_shape(CLOSE)