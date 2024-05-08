from turtle import *
m=10
tracer(0)
lt(90)
for i in range(4):
    fd(10*m)
    rt(270)
up()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
down()
for l in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)
up()
for x in range(-50,50):
    for y in range(-50, 50):
        goto(x*m,y*m)
        dot(3,'black')
update()
exitonclick()
