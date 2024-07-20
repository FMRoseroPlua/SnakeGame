from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        with open("./high_score.txt", mode="r") as file:
            val = int(file.read())
            if val > 0:
                self.high_score = val
            else:
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.count}  -  High score: {self.high_score}", align="center", font=('Arial', 12, 'bold'))
        self.count += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=('Arial', 12, 'bold'))
        self.high_score = self.count - 1 if self.count > self.high_score else self.high_score
        with open("./high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def continuar(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Presiona c para reiniciar el juego", align="center", font=('Arial', 12, 'bold'))
        self.high_score = self.count - 1

