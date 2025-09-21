import turtle as t

t.colormode(255)
tom = t.Turtle()
screen = t.Screen()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_counter_clockwise():
    tom.left(10)


def move_clockwise():
    tom.right(10)


def clear_screen():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.mainloop()
screen.exitonclick()
