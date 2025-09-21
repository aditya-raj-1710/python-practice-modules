from turtle import Turtle, Screen, colormode
import random

colormode(255)
right_angles = [1, 2, 3, 4]

my_turtle = Turtle()
screen = Screen()
my_turtle.shape()
my_turtle.dot()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def dotted_line(total_length):
    for i in range(total_length):
        my_turtle.pendown()
        my_turtle.forward(5)
        my_turtle.penup()
        my_turtle.forward(5)


def draw_polygon(edges):
    angle = 360 / edges
    for _ in range(edges):
        my_turtle.forward(100)
        # dotted_line(10)
        my_turtle.left(angle)


def draw_polygons(edges):
    for polygon in range(3, 10):
        my_turtle.pencolor(random_color())
        draw_polygon(polygon)


def draw_random_path():
    my_turtle.speed(10)
    while True:
        my_turtle.pencolor(random_color())
        my_turtle.pensize(10)
        my_turtle.forward(50)
        my_turtle.right(90 * random.choice(right_angles))


# draw_random_path()

def draw_circles(size_of_gap):
    my_turtle.speed(0)
    for tilt in range(int(360 / size_of_gap)):
        my_turtle.pencolor(random_color())
        my_turtle.circle(radius=100)
        my_turtle.left(tilt)


draw_circles(5)
screen.exitonclick()
