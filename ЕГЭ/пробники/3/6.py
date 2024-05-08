from turtle import *
m=8
tracer(0)
down()
for i in range(7):
    rt(90)
    fd(4*m)
    for j in range(2):
        rt(270)
        fd(3*m)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'black')
update()
exitonclick()









