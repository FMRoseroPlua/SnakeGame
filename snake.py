from turtle import Turtle
MOVE_DISTANCE = 10
SNAKE_START_POS = [(0, 0), (-10, 0), (-20, 0)]
# SNAKE_START_POS = [(0, 0), (-10, 0), (-20, 0), (-30, 0), (-40, 0), (-50, 0), (-60, 0)]


class Snake:
    def __init__(self):
        self.snake_new_pos = []
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for i in range(len(SNAKE_START_POS)):
            self.add_square((SNAKE_START_POS[i]))

    def add_square(self, pos=(0, 0)):
        snake_part = Turtle("square")
        snake_part.fillcolor("white")
        snake_part.penup()
        snake_part.shapesize(0.5, 0.5)
        snake_part.goto(pos)
        self.snake.append(snake_part)

    def head(self):
        return self.snake[0]

    def head_coordinates(self):
        return self.snake[0].xcor(), self.snake[0].ycor()

    def tail_coordinates(self):
        return self.snake[-1].xcor(), self.snake[-1].ycor()

    def coordinates(self):
        lista = [i.pos() for i in self.snake]
        lista.pop(0)
        return lista

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto((new_x, new_y))
        self.snake[0].forward(10)

    def up(self):
        direction = self.snake[0].heading()
        if direction != 90 and direction != 270:
            self.snake[0].setheading(90)

    def down(self):
        direction = self.snake[0].heading()
        if direction != 90 and direction != 270:
            self.snake[0].setheading(270)

    def left(self):
        direction = self.snake[0].heading()
        if direction != 0 and direction != 180:
            self.snake[0].setheading(180)

    def right(self):
        direction = self.snake[0].heading()
        if direction != 0 and direction != 180:
            self.snake[0].setheading(0)
