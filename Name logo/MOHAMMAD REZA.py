import turtle
import math
m = turtle.Turtle()

# M

def M (M):
    m.color("red")
    m.begin_fill()

    m.lt(73.68)
    m.fd(131)
    m.rt(127.73)
    m.fd(85.79)
    m.lt(110.38)
    m.fd(83.63)
    m.rt(129.51)
    m.fd(133.6)
    m.rt(106.91)
    m.fd(55.52)
    m.rt(73.08)
    m.fd(66.32)
    m.lt(129.36)
    m.fd(65.91)
    m.rt(110.41)
    m.fd(62.98)
    m.lt(128.62)
    m.fd(60.47)
    m.rt(75.52)
    m.fd(8.25)
    m.end_fill()

# O

def O (O) :
    m.color("red")
    m.begin_fill()

    # O
    # d = 132.18
    def polygon(x, n, length):
        angle = 360 / n
        for i in range(n):
            x.fd(length)
            x.lt(angle)

    m.lt(180)

    def circle(x, d):
        circumference = 2 * math.pi * d
        n = 50
        length = circumference / n
        polygon(x, n, length)

    circle(m, 132.18 / 2)

    # arc for O
    m.penup()
    m.lt(90)
    m.fd(7.45)
    m.rt(90)
    m.pendown()
    m.end_fill()

    m.color("white")
    m.begin_fill()

    def arc(x, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        for i in range(n):
            x.fd(step_length)
            x.lt(step_angle)

    arc(m, 58.84, 185)
    m.lt(86)
    m.fd(118.5)
    m.end_fill()

# H

def H (H) :
    m.color("red")
    m.begin_fill()
    m.fd(55.27)
    m.lt(90)
    m.fd(74.28)
    m.rt(89)
    m.fd(60.46)
    m.rt(91)
    m.fd(74.28)
    m.lt(90)
    m.fd(7)
    m.lt(90.5)
    m.fd(124.37)
    m.lt(89.5)
    m.fd(7)
    m.lt(90.5)
    m.fd(43.18)
    m.rt(90)
    m.fd(60.46)
    m.rt(90)
    m.fd(43.18)
    m.lt(90)
    m.fd(55.27)
    m.lt(89.5)
    m.fd(124.37)
    m.lt(90)
    m.end_fill()

# A

def A (A):
    m.color("red")
    m.begin_fill()
    m.fd(7.56)
    m.lt(55.1)
    m.fd(21.26)
    m.rt(54.5)
    m.fd(59.22)
    m.rt(56.65)
    m.fd(16.54)
    m.lt(55.5)
    m.fd(63.02)
    m.lt(118.64)
    m.fd(149.57)
    m.lt(120.86)
    m.fd(160)
    m.lt(120.5)
    m.end_fill()
    m.penup()
    m.fd(22)
    m.lt(90)
    m.fd(24.18)
    m.rt(89)
    m.pendown()
    m.color("white")
    m.begin_fill()
    m.fd(54.73)
    m.lt(118.62)
    m.fd(55.28)
    m.lt(120.83)
    m.fd(56.16)
    m.end_fill()

# D

def D (D):
    m.color("red")
    m.begin_fill()
    # D
    m.fd(54.8)

    def arc(x, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        for i in range(n):
            x.fd(step_length)
            x.lt(step_angle)

    arc(m, 62.64, 179)

    m.fd(55.27)
    m.lt(90.5)
    m.fd(127)
    m.lt(90)

    m.end_fill()

    m.penup()
    m.fd(52)
    m.lt(90)
    m.fd(7)
    m.rt(90)
    m.pendown()

    m.color("white")
    m.begin_fill()

    def arc(x, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        for i in range(n):
            x.fd(step_length)
            x.lt(step_angle)

    arc(m, 55.86, 182)

    m.lt(88)
    m.fd(114)
    m.lt(90)

    m.end_fill()

# R

def R (R):
    def arc(x, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = angle / n
        for i in range(n):
            x.fd(step_length)
            x.lt(step_angle)

    m.color("red")
    m.begin_fill()
    # R
    m.fd(55.36)
    m.lt(90)
    m.fd(31.09)
    m.rt(90)
    # arc
    arc(m, 46.64, 180)
    m.fd(55.36)
    m.lt(90)
    m.fd(124.37)
    m.penup()
    m.lt(90)
    m.fd(55.36)
    m.rt(90)
    m.bk(31.09)
    m.lt(56.15)
    m.pendown()
    m.fd(56.36)
    m.lt(123.85)
    m.fd(7.86)
    m.lt(56.9)
    m.fd(57.75)
    m.rt(146.9)
    m.end_fill()

    m.color("white")
    m.begin_fill()
    # arc for R
    arc(m, 39.73, 180)
    m.lt(90)
    m.fd(79.46)
    m.end_fill()

# E

def E (E):
    m.color("red")
    m.begin_fill()
    # E
    m.fd(103.29)
    m.lt(90)
    m.fd(6.91)
    m.lt(90)
    m.fd(48.01)
    m.rt(90)
    m.fd(76)
    m.rt(90)
    m.fd(48.01)
    m.lt(90)
    m.fd(6.91)
    m.lt(90)
    m.fd(48.01)
    m.rt(90)
    m.fd(27.5)
    m.rt(90)
    m.fd(48.01)
    m.lt(90)
    m.fd(6.91)
    m.lt(90)
    m.fd(103.29)
    m.lt(90)
    m.fd(124.37)
    m.lt(90)
    m.end_fill()

# Z

def Z (Z):
    m.color("red")
    m.begin_fill()
    # Z
    m.fd(117.46)
    m.lt(90)
    m.fd(6.91)
    m.lt(90)
    m.fd(54.82)
    m.rt(115.02)
    m.fd(129.62)
    m.lt(115.02)
    m.fd(117.46)
    m.lt(90)
    m.fd(6.91)
    m.lt(90)
    m.fd(54.82)
    m.rt(115.02)
    m.fd(129.62)
    m.lt(115.02)
    m.end_fill()


m.speed(0)
m.pensize(2)


m.penup()
m.bk(600)
m.lt(90)
m.fd(250)
m.rt(90)
m.pendown()


# MOHAMMAD

M(M)

m.penup()
m.fd(-246.09)
m.pendown()
m.end_fill()

O(O)

m.penup()
m.fd(7)
m.lt(90)
m.fd(88.09)
m.pendown()

H(H)

m.penup()
m.fd(127.05)
m.pendown()

A(A)

m.penup()
m.lt(119.8)
m.fd(134.29)
m.rt(89)
m.fd(18.43)
m.lt(90)
m.pendown()

M(M)

m.penup()
m.rt(180)
m.fd(180)
m.pendown()

M(M)

m.penup()
m.rt(178)
m.fd(176)
m.pendown()

A(A)

m.penup()
m.lt(119.8)
m.fd(134.29)
m.rt(89)
m.fd(18.43)
m.lt(89.5)
m.pendown()
D(D)


m.penup()
m.bk(850)
m.rt(90)
m.fd(161.91)
m.lt(90)
m.pendown()

# REZA

R(R)

m.penup()
m.fd(38)
m.lt(90)
m.fd(88.1)
m.pendown()

E(E)

m.penup()
m.fd(140)
m.pendown()

Z(Z)

m.penup()
m.fd(145)
m.pendown()

A(A)

m.penup()
m.fd(100)
m.pendown()

turtle . mainloop()
print(m)
