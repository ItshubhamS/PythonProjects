from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 14, "bold")


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score_maintain()

    def score_maintain(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="Center", font=("Arial", 14, "bold"))
