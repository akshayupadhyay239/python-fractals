import turtle,math

a = turtle.Turtle()
a.speed(0)
a.left(90)
def draw(l):
    if(l<10):
        return
    else:
        a.fd(l)
        a.left(45)
        draw(l*3/4)
        a.right(90)
        draw(l*3/4)
        a.left(45)
        a.backward(l)

draw(100)
