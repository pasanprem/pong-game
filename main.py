# Pong Game - Part of the 100 Days of Code Udemy course

from turtle import Turtle, Screen

# from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")


paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")



screen.exitonclick()
