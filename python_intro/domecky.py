from turtle import *
from math import *
from random import *



def domecek(a):
    c = round(sqrt(2*a**2))
    
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    
    left(90+45)
    forward(c)
    left(90)

    forward(c/2)
    left(90)
    forward(c/2)
    left(90)

    forward(c)
    left(45)

for x in range(5):
    penup()
    goto(randint(-200, 200), randint(-200, 200))
    pendown()
    domecek(randint(20, 90))
    


exitonclick()
