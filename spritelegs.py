# author: ravig463

import turtle

t = turtle.Turtle()
t.shape("circle")

n = int(input("How many legs should this sprite have"))
angle = 360 / n

for i in range(n):
