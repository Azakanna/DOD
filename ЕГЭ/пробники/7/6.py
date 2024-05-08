from turtle import *
m=8
tracer(0)
for i in range(12):
    for l in range(15):
        fd(2*m)
        rt(90)
    fd(5*m)
up()
for x in range (-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'purple')
update()
exitonclick()
