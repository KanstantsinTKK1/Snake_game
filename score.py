from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 21, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color('white')
        self.goto(0,297)
        self.points = 0
        self.high_points = 0
        self.write_point()

    def write_point(self):
        self.clear()
        self.write(f'Score: {self.points}. High score: {self.high_points}', move=False, align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f'GAME OVER', move=False, align=ALIGN, font=FONT)

    def high_score(self):
        if self.points > self.high_points:
            self.high_points = self.points
        self.points = 0
        self.write_point()
        with open("data.txt", mode='w') as file:
            file.write(f"high_score = {self.high_points}")

