from turtle import Turtle

# Inheritance from Turtle superclass
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))

    def my_score(self):
        # Increase score by one on every food consumption
        self.score += 1
        # To clear earlier score and rewrite new score
        self.clear()
        self.update_score()