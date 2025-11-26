import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
x = 0
screen.tracer(0)

for _ in range(3):
    t = Turtle()
    t.penup()
    t.shape("square")
    t.setpos(x, 0)
    t.turtlesize(stretch_len=0.6, stretch_wid=0.6, outline=1)
    t.color("white", "white")
    segments.append(t)
    x -= 13

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())
    segments[0].forward(10)

screen.exitonclick()