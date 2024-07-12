from turtle import Turtle

ALIGNMENT = "center"
FONT = ("times_new_roman", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score_board()

    # below code will write the 'Game over' on the screen when the game gets over:
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # below code will help to display the code on the screen:
    def score_board(self):
        self.clear()
        self.write(f"Score = {self.score}     High score = {self.high_score} ", align=ALIGNMENT, font=FONT)

    def highest_score(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.score_board()

    # below code is to keep track of the most recent score when the game runs:
    def score_increase(self):
        self.score += 1
        self.score_board()
