from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

x = 0
for _ in range(3):
    t = Turtle()
    t.penup()
    t.shape("square")
    t.setpos(x, 0)
    t.turtlesize(stretch_len=0.6, stretch_wid=0.6, outline=1)
    t.color("white", "white")
    x -= 13



screen.exitonclick()