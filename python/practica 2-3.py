
def setup():
    size(980, 980)
    background(255)
    
    for x in range ( 100, 1000, 100):
        for y in range (100, 800, 100):
            fill(255)
            rect_mode(CENTER)
            square(x,y, 50)
            fill(0)
            circle(x, y, 20)