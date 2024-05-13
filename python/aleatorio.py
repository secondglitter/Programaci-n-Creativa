
def setup():
    size(980, 980)
    background(240)
        
    # Funcion aleatoria para crear circulos entre en 10 y el 50
    fill(0)
    no_stroke()    
    for x in range (50, 900, 50):
        d = random(10, 50)
        circle(x, 50, d)
    
    # Este es para inprimir circulos entre el 1 y el 4 pero con numeros enteros
    for x in range(50, 900, 50):
        i = random (1,4)
        circle(x, 150, 10 + i * 10)
        
    # Para cambiar los colores de los circulos por un color aleatorio
    for x in range(50, 900, 50):
        r = random_int(255)
        g = random_int(255)
        b = random_int(255)
        fill (r, g, b)
        circle(x, 250, 40)
    
    # Aqui tomara aleatoriamente un color en de la paleta verde o azul
    for x in range(50, 900, 50):
        r = 0
        g = random_int(255)
        b = random_int(255)
        fill (r, g, b)
        circle(x, 350, 40)
        
    # otra forma de hacer el color de los circulos aleatorio, pero con solo la paleta de color azul    
    for x in range(50, 900, 50):
        r = 0
        g = 150
        b = random_int(120, 255)
        fill (r, g, b)
        circle(x, 450, 40)
        
    #Creamos una lista de colores predefinidos
    c = [
        color(255, 0, 240),
        color(25, 255, 40),
        color(55, 255, 200),
        ]
    
    #aqui podemos pedir cualquiera de esos colores aleatoriamente
    for x in range(50, 900, 50):
        fill(random_choice(c))
        circle(x, 550, 45)
    
    # Este es para que cuando se cree una estrella tome una forma aleatoria
    fill(0)
    for x in range (100, 900, 100):
        n = random_int(3, 7) # Este es para el numero de puntas que tendra la estrella
        r = random_choice ((10, 25, 40)) # este es para el radio
        star (x, 650, r, 50, n)

    #Este es aleatorio de seleccion con if y elif
    for x in range(100, 900, 100):
        v = random_int (3,8)
        print(v) # este es para imprimir en la consola el numero que salio en cada figura
        if v == 3: # si es igual a 3 dibujara un circulo
            circle(x, 750, 50)
        elif v == 4: # si es igual a 4 dibujara un cuadrado
            square(x, 750, 50)
        else: # y aqui dibujara el resto de opciones en forma de una estrella
            random_choice((10,25,40))
            star(x, 750, r, 30, v)
    
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
        