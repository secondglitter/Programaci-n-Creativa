
def setup():
    size(980, 980)
    background(240)
    # aqui defines los valores que quieras que tenga
    ojo (100, 200, 300)
    
    # otra forma de crear es con range
    for y in range (100, 1000, 100):
        ojo (width /2, y, 150)

# esta es una forma de llamar varias veces la varible ojo sin repetir codigo
def ojo(x, y, w):
    r= random_int(255)
    g= random_int(255)
    b= random_int(255)
    no_stroke() #para que no tenga un margen alrededor de la figura
    fill(255)
    ellipse(x, y, w, w /3)
    fill (r,g,b)
    ellipse(x, y, w /3, w /3)
    fill (0)
    ellipse(x, y, w * 0.1, w * 0.1)