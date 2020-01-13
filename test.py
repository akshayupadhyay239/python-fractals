import turtle
import math
a = turtle.Turtle()
class cn:
    def __init__(self,a,b):
        self.real = a
        self.imag = b

    def __add__(self,o):
        res = cn(self.real+o.real,self.imag+o.imag)
        return res
    def __mul__(self,o):
        res = cn(self.real*self.real-o.imag*o.imag,2*self.real*o.imag)
        return cn

def mod(comp):
    return math.sqrt(comp.real*comp.real+comp.imag*comp.imag)

    #z = z sq.+c
a.penup()
a.pensize(1)
a.speed(0)
for x in range(-200,200,2):
    for y in range(-200,200,2):
        a.goto(x,y)
        z=cn(x/100,y/100)
        c=z
        n = 0
        while(n<1):
            z.real = z.real*z.real-z.imag*z.imag+z.real
            z.imag = 2*z.real*z.imag+z.imag
            if(mod(z)>5):
                break
            else:
                a.dot(2,"black")

            n = n+1

                
            
        
    
