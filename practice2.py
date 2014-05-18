# author: ravig463

import turtle 

shape = input("What should I draw?")
if shape == "square":
	t = turtle.Turtle()
	t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
    t.forward(100)
	t.left(90)
	t.forward(100)
	t.left(90)
if shape == "triangle":
	t = turtle.Turtle()
	t.forward(100)
	t.left(120)
	t.forward(100)
	t.left(120)
	t.forward(100)
	t.left(120)
	
if shape == "circle":
	t = turtle.Turtle()
	for n in range(1, 121):
		t.forward(3)
		t.left(3)
		
	