import turtle

class GameOver(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 0)

    def display(self):
        self.write("GAME OVER", align="center", font=("Courier", 32, "bold"))