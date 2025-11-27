import time
from turtle import Turtle

COORDINATES_OF_SQUARES = [(0, 0), (-13, 0), (-26, 0)]
PACES = 10

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):

        for num in range(3):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.setpos(COORDINATES_OF_SQUARES[num])
            t.turtlesize(stretch_len=0.6, stretch_wid=0.6, outline=1)
            t.color("white", "white")
            self.segments.append(t)

    def move_snake(self):

            for index in range(len(self.segments) - 1, 0, -1):
                self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())

            if self.segments[0].xcor() == 270 and self.segments[0].ycor() == 270 and self.segments[1].heading == 270:
                self.segments[0].left(0)
                self.segments[0].forward(PACES)
            elif self.segments[0].xcor() == -270 and self.segments[0].ycor() == -270:
                self.segments[0].left(0)
                self.segments[0].forward(PACES)
            if self.segments[0].xcor() == 270 and self.segments[0].heading() == 0:
                self.segments[0].left(90)
                self.segments[0].forward(PACES)
            elif self.segments[0].xcor() == -270 and self.segments[0].heading() == 0:
                self.segments[0].left(0)
                self.segments[0].forward(PACES)
            elif self.segments[0].ycor() == 270 and self.segments[0].heading() == 0:
                self.segments[0].left(0)
                self.segments[0].forward(PACES)
            elif self.segments[0].ycor() == -270 and self.segments[0].heading() == 0:
                self.segments[0].left(180)
                self.segments[0].forward(PACES)
            else:
                self.segments[0].forward(PACES)



    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

#write the rest of the program by yourself