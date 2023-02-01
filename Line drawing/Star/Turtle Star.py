import turtle
a = turtle.Turtle()
a.speed(0 )
a.pensize(2)
angle = [0, 2.21,4.65,7.37,10.38,13.74,17.46,21.57,26.1,31.05,36.38,42.04,47.96,54
         ,60.04,65.96,71.62,76.95,81.9,86.43,90.54,94.26,97.62,100.63,103.35,105.79, 108]

distance = [416, 395.35, 375.35, 356.11, 337.75, 320.44, 304.35, 289.68, 276.67, 265.54, 256.56, 249.94, 245.89, 244.52, 245.89, 249.94, 256.56
            , 265.54, 276.67, 289.68, 304.35, 320.44, 337.75, 356.11, 375.35, 395.35, 400]
#c = ['red', 'red','red','orange','orange','orange', 'yellow','yellow','yellow', 'yellow green','yellow green','yellow green'
    # , 'green', 'green', 'green', 'blue','blue','blue','blue violet','blue violet','blue violet', 'violet','violet','violet', 'pink', 'pink', 'pink']

a.penup()
a.lt(90)
a.fd(400)
a.rt(180)
a.pendown()

def d(a):
    for i in range(26):
       # a.color(c[i])
        a.lt(angle[i])
        a.fd(distance[i])
        a.penup()
        a.bk(distance[i])
        a.rt(angle[i])
        a.fd(16)
        a.pendown()

def di(a):
    for i in range(26):
       # a.color(c[i])
        a.rt(angle[i])
        a.fd(distance[i])
        a.penup()
        a.bk(distance[i])
        a.lt(angle[i])
        a.fd(16)
        a.pendown()
# 1
d(a)
a.lt(108)
a.fd(400)
a.bk(400)
a.rt(108)
a.bk(416)
# 2
di(a)
a.lt(72)
a.bk(416)
# 3
di(a)
a.lt(72)
a.bk(416)
# 4
di(a)
a.lt(72)
a.bk(416)
#5
di(a)
a.penup()
a.fd(1000)
turtle.mainloop()

