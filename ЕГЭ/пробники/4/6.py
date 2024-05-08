from turtle import *
m=8
tracer(0)
fd(100*m)
rt(90)
fd(100*m)
rt(30)
down()
for i in range(10):
    fd(25*m)
    rt(90)
up()
for x in range (-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'purple')
update()
exitonclick()



















