from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)

screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    # tim.setheading(tim.heading() + 10)
    # OR
    tim.left(10)

def turn_right():
    # tim.right(10)
    tim.setheading(tim.heading() - 10)

def clear_screen():
    tim.reset()
    # OR
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()

screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=clear_screen, key="c")


screen.exitonclick()