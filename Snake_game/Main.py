import time
from turtle import Screen

from food import Food
from score_board import Score_Board
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score_Board()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
speed = 10
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.snake_head.distance(food) < 14:
        score_board.score_count()
        snake.extend()
        food.refresh()
        print(speed)
        speed += 10
    #     detect collision with wall
    if (
        snake.snake_head.xcor() > 280
        or snake.snake_head.xcor() < -280
        or snake.snake_head.ycor() > 280
        or snake.snake_head.ycor() < -280
    ):

        score_board.game_over()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()
