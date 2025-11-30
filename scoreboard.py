from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.color('white')
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, 275)

    def show_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.show_score()




