from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Mi Snake Game")
screen.setup(500, 500)
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.head().distance(food) <= 10:
        snake.add_square(snake.tail_coordinates())
        score.refresh()
        food.refresh()
    if ((snake.head().xcor() > 230 or snake.head().xcor() < -240
        or snake.head().ycor() > 240 or snake.head().ycor() < -230)
        or (snake.head_coordinates() in snake.coordinates())):
        game_is_on = False
        score.game_over()

screen.exitonclick()
