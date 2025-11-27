from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
snake.create_snake()
snake.move_snake()

screen.exitonclick()

#write the rest of the program by yourself