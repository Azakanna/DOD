from turtle import *
m=8
tracer(0)
for i in range(10000):
    fd(10*m)
    rt(30)
    lt(210)
    fd(10*m)
    lt(90)
    fd(25*m)
    lt(180)
    fd(5*m)
    rt(180)
    fd(5*m)
    lt(90)
    fd(10*m)
    lt(90)
    fd(20*m)
    fd(5*m)
up()
for x in range (-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'purple')
update()
exitonclick()
