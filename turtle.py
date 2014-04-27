# author: ravig463

import turtle

t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

numbers = range(1,100)
for number in numbers:
    t.forward(2)
	t.left(10)
