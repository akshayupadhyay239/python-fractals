import turtle
a = turtle.Turtle()
a.speed(0)
a.penup()
a.backward(800)
a.pendown()
def fractal(l):
    if(l<3):
        return
    else:
        a.fd(l/6)
        fractal(2*l/9)
        a.fd(l/6)
        a.left(60)
        a.fd(l/4)
        fractal(2*l/9)
        a.fd(l/6)
        a.right(120)
        a.fd(l/6)
        fractal(2*l/9)
        a.fd(l/6)
        a.left(60)
        a.fd(l/6)
        fractal(2*l/9)
        a.fd(l/6)

fractal(600)
        
