# author: ravig463

import turtle

world = turtle.Screen()
world.bgcolor("black")

t = turtle.Turtle()
t.color("red")
t.left(30)
t.hideturtle()
r = turtle.Turtle()
r.left(150)
r.color("red")
r.hideturtle()


for i in range(22):
	t.left(i)
	t.forward(8)
	
for j in range(22):
	r.right(j)
	r.forward(8)
	
b = turtle.Turtle()
b.hideturtle()
b.setpos(-50, -50)
b.write(" Happy Mother's Day!!!! from Ravi =-)")
	





