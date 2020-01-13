#serpinski triangle
import turtle
a = turtle.Turtle()
a.speed(0)
a.left(180)
def triangle(l):
    for _ in range(0,3):
        a.right(120)
        a.fd(l)
        
def serpinski(l):
    if(l<4):
        return
    else:
        triangle(l)
        serpinski(l/2)
        a.penup()
        a.backward(l/2)
        a.pendown()
        serpinski(l/2)
        a.penup()
        a.fd(l/2)
        a.right(120)
        a.fd(l/2)
        a.left(120)
        a.pendown()
        serpinski(l/2)
        a.penup()
        a.left(60)
        a.fd(l/2)
        a.right(60)
        a.pendown()
        

serpinski(300)
