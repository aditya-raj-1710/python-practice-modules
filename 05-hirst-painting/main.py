import random
from turtle import *
from color_data import color_list


my_turtle = Turtle()
my_screen = Screen()
my_screen.setup(800, 600)
colormode(255)

my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.setposition(-300, -300)

for i in range(1, 101):
    color = random.choice(color_list)
    my_turtle.dot(20, color)
    my_turtle.forward(50)
    if i % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

my_screen.exitonclick()
