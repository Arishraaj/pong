from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score_board=Score()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game=True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #ball collision and bouncing
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.y_bounce()

    #ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    #if r_paddle missed theball missed
    if ball.xcor() > 400:
        ball.reset_ball()
        score_board.l_point()
        
    #if l_paddle missed theball missed
    if ball.xcor() < -400:
        ball.reset_ball()
        score_board.r_point()
        

    

screen.exitonclick()