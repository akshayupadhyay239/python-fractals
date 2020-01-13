import turtle
a = turtle.Turtle()
a.speed(0)
#leaf
def leaf(l):
    if(l<3):
        return
    else:
        a.fd(l/2)
        a.right(30)
        leaf(l/2)
        a.left(30)
        a.fd(l/2)
        a.left(30)
        leaf(l/2)
        a.right(30)
        a.penup()
        a.backward(l)
        a.pendown()

leaf(400)
        
