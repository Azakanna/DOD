# from turtle import *
# m=15
# tracer(0)
# for i in range (2):
#     fd(10*m)
#     rt(90)
#     fd(18*m)
#     rt(90)
# up()
# bk(6*m)
# rt(90)
# fd(9*m)
# lt(90)
# down()
# for k in range (2):
#     fd(17*m)
#     rt(90)
#     fd(5*m)
#     rt(90)
# up()
# for x in range (-50,50):
#     for y in range(-50,50):
#         goto(x*m,y*m)
#         dot(5, 'Purple')
# update()
# exitonclick()

from turtle import *
m=8
# tracer(0)
for i in range(4):
    fd(10*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
fd(7*m)
rt(90)
fd(3*m)
lt(90)
down()
for k in range(2):
    fd(70*m)
    rt(90)
    fd(80*m)
    rt(90)
up()
for x in range (-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3,'purple')
update()
exitonclick()

