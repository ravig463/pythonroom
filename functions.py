# author: ravig463

import turtle

shape = input("What should I draw?")


def makeShape(sides):
	t = turtle.Turtle()
	for i in range(0, 90):
		t.forward(3)
		t.left(3)
		

	t = turtle.Turtle()
	for i in range(4):
		t.forward(100)
		t.left(90)
		
if shape == "triangle":
	t = turtle.Turtle()
	for i in range(3):
		t.forward(100)
		t.left(120)
		
if shape == "pentagon":
	t = turtle.Turtle()
	for i in range(5):
		t.forward(100)
		t.left(72)
	