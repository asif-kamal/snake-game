import time
from turtle import Turtle

COORDINATES_OF_SQUARES = [(0, 0), (-13, 0), (-26, 0)]
PACES = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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

            if self.head.xcor() == 270 and self.head.ycor() == 270 and self.segments[1].heading == 270:
                self.head.left(0)
                self.head.forward(PACES)
            elif self.head.xcor() == -270 and self.head.ycor() == -270:
                self.head.left(0)
                self.head.forward(PACES)
            if self.head.xcor() == 270 and self.head.heading() == 0:
                self.head.left(90)
                self.head.forward(PACES)
            elif self.head.xcor() == -270 and self.head.heading() == 0:
                self.head.left(0)
                self.head.forward(PACES)
            elif self.head.ycor() == 270 and self.head.heading() == 0:
                self.head.left(0)
                self.head.forward(PACES)
            elif self.head.ycor() == -270 and self.head.heading() == 0:
                self.head.left(180)
                self.head.forward(PACES)
            else:
                self.head.forward(PACES)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

#write the rest of the program by yourself