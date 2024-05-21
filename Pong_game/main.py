import time
from turtle import *

from ball import Ball
from pedal import Paddle
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
score = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.speed_movement)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() > -320
    ):
        ball.bounce_x()
    #     if right misses
    if ball.xcor() > 380:
        ball.misses()
        score.l_point()
    #       if left misses
    if ball.xcor() < -380:
        ball.misses()
        score.r_point()

screen.exitonclick()
