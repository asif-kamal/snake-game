import time
from turtle import Turtle

# COORDINATES_OF_SQUARES = [(0, 0), (-13, 0), (-26, 0)]
PACES = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.x = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for num in range(3):
            self.add_segment()

    def move_snake(self):
            for index in range(len(self.segments) - 1, 0, -1):
                self.segments[index].goto(self.segments[index - 1].xcor(), self.segments[index - 1].ycor())

            self.head.forward(PACES)

    def snake_hits_wall(self):
        if self.head.xcor() > 290 or self.head.ycor() > 290 or self.head.ycor() < -290 or self.head.xcor() < -290:
            return True
        else:
            return False

    def snake_hits_self(self):
        for segment in self.segments[3:]:
            if self.head.distance(segment) < 10:
                return True
        return False

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

    def add_segment(self):
        t = Turtle()
        t.penup()
        t.setpos(self.x - 13, 0)
        t.shape("square")
        t.turtlesize(stretch_len=0.6, stretch_wid=0.6, outline=1)
        t.color("white", "white")
        t.speed("fastest")
        self.segments.append(t)

#write the rest of the program by yourself