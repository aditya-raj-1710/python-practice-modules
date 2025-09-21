from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
y_position = [-70, -40, -10, 10, 40, 70]
all_turtles = []
is_race_on = False


def set_turtle(position, t_color):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(t_color)
    new_turtle.goto(x=-230, y=position)
    return new_turtle


screen = Screen()
screen.setup(width=500, height=400)

for index in range(0, 6):
    all_turtles.append(set_turtle(y_position[index], colors[index]))

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You won! The {turtle.color()} turtle won the race!")
                break
            else:
                print(f"You lose! The {turtle.color()} turtle won the race!")
        rand_distance = random.randint(1, 20)
        turtle.forward(rand_distance)

screen.exitonclick()
