import time
from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.bgcolor("green")
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
scoreboard_1 = Scoreboard((-150, 200))
scoreboard_2 = Scoreboard((150, 200))

screen.listen()
screen.onkeypress(player_1.go_up, "w")
screen.onkeypress(player_1.go_down, "s")
screen.onkeypress(player_2.go_up, "Up")
screen.onkeypress(player_2.go_down, "Down")

ball = Ball()
game_is_on = True
on_play = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # detect  collision with the paddle
    if ball.distance(player_1) < 60 and ball.xcor() == -320 or ball.distance(player_2) < 60 and ball.xcor() == 320:
        ball.bounce_x()

    if ball.xcor() < -340:
        on_play = False
        scoreboard_2.increase_score()
        ball.reset_position()

    if ball.xcor() > 340:
        on_play = False
        scoreboard_1.increase_score()
        ball.reset_position()


screen.exitonclick()
