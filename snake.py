import time
from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.screen = Screen()
        self.segments = []
        self.x = 0

    def create_snake(self):

        for _ in range(3):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.setpos(self.x, 0)
            t.turtlesize(stretch_len=0.6, stretch_wid=0.6, outline=1)
            t.color("white", "white")
            self.segments.append(t)
            self.x -= 13

    def move_snake(self):

        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            for index in range(len(self.segments) - 1, 0, -1):
                self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())

            if self.segments[0].xcor() == 270 and self.segments[0].ycor() == 270:
                self.segments[0].left(0)
                self.segments[0].forward(10)
            elif self.segments[0].xcor() == -270 and self.segments[0].ycor() == -270:
                self.segments[0].left(0)
                self.segments[0].forward(10)
            elif self.segments[0].xcor() == 270:
                self.segments[0].left(90)
                self.segments[0].forward(10)
            elif self.segments[0].xcor() == -270:
                self.segments[0].left(0)
                self.segments[0].forward(10)
            elif self.segments[0].ycor() == 270:
                self.segments[0].left(0)
                self.segments[0].forward(10)
            elif self.segments[0].ycor() == -270:
                self.segments[0].left(180)
                self.segments[0].forward(10)
            else:
                self.segments[0].forward(10)

#write the rest of the program by yourself