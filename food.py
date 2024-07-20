from turtle import Turtle
import random
SCREEN_SIZE = 240


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.4, 0.4)
        self.penup()
        self.color("yellowgreen")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        dim_x = random.randint(-SCREEN_SIZE, SCREEN_SIZE)
        dim_y = random.randint(-SCREEN_SIZE, SCREEN_SIZE-20)
        self.goto(dim_x, dim_y)
