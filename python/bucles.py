def setup():
    size(980, 980)
    background(240)
    
    #ubicacion de los puntos para hacer las lineas
    # line (x1, y1, x2, y2)

    # esta es una forma de hacer lineas manuales con un array
    
    """numeros = [10, 20, 30, 40, 50, 60]

    for n in numeros:
        line (n * 10, 100, n * 10, 400) """
        
    # esta es una forma de hacer lineas con range (rango)
    # range (ni, nf, ns)
    # ni-numero con el que iniciara
    # nf-numero con el que se detendra, este no lo imprimira
    # ns-numero con el que ira saltando o sumando al numero inicial
    
    for n in range(10, 70, 10):
       line (n * 10, 100, n * 10, 500)
        
    # el margin o (margen) recorre el primer valor hasta donde definas el valor de margin    
    margin = 50    
    for i in range(20):
        line (margin + i * 10, 100, margin + i* 10, 500)
        