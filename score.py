from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)

    def write_score(self):
        self.clear()
        self.write(f"Score - {self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def score_increase(self, x_cord):
        if x_cord < 0 :
            self.l_score += 1
        else:
            self.r_score += 1




