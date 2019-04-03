from turtle import *

screen = Screen()
screen.title("Blackstar Sketcher")
screen.bgcolor("light pink")

Blackstar = Turtle()
Blackstar.color("black")
Blackstar.pensize(2)
Blackstar.speed(0)
Blackstar.shape("turtle")

def go_up():
	Blackstar.setheading(90)
	Blackstar.forward(10)

def go_down():
	Blackstar.setheading(270)
	Blackstar.forward(10)

def go_right():
	Blackstar.setheading(0)
	Blackstar.forward(10)

def go_left():
	Blackstar.setheading(180)
	Blackstar.forward(10)

def draw_star():
	Blackstar.color("red")
	for x in range(5):
		Blackstar.forward(50)
		Blackstar.left(144)
	Blackstar.color("black")

def clear_screen(x,y):
	screen.reset()
	Blackstar.color("black")
	Blackstar.pensize(2)
	Blackstar.speed(0)

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(draw_star, "z")
screen.onclick(clear_screen)


screen.listen()

mainloop()