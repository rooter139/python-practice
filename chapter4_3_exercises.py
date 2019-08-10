import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
def call_turtle():
    oscar = turtle.Turtle()
    square(oscar, length=100)
    polygon(oscar, 3, 30)
    circle(oscar,100)
    #turtle.mainloop()



def polygon(t, length, n):
    """ 
    Dibuja un poligono turtle de n lados
    con una longitud length
    """
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def polygon_solution(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    length = 4
    #n = int(r*2)/length
    n = int(r*2/length)
    polygon(t,length,n)

import math
def circle_solution(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon_solution(t, n, length)

def circle_solution2(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)


print('Antes')
call_turtle()
print('Despues')
turtle.mainloop()