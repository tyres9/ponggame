from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 50, "normal")
GAME_OVER = ("Arial", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGN, font=GAME_OVER)
        self.goto(0, -30)
        self.write(f"Score: {self.score}", align=ALIGN, font=GAME_OVER)





