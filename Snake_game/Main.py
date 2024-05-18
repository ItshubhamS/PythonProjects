import time
from turtle import Screen

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()
