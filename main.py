from turtle import Screen
from bird import BirdF, birdimage, birdup, bird_down
from User_interface import Intro, GetReady, Start, getready, intro
from object import GroundManager, PipeManager, ground, pipe, pipe_upside_down, object_speed
from scoreboard import ScoreCounterManager, number_list, gameover
import time
import random

x = 0
y = 0
void_height = 165
dist_between_pipe = 390


def mouseclick(x1, y1):
    global x
    global y
    screen.tracer(1, 20)
    x = x1
    y = y1


# screen setup ----------------------
screen = Screen()
screen.setup(width=900, height=500)
screen.tracer(0)
bg_image = "./images/bg1.gif"
screen.bgpic(bg_image)
# -----------------------------------

# screen shape register -------------
screen.register_shape(birdimage)
screen.register_shape(getready)
screen.register_shape(intro)
screen.register_shape(ground)
screen.register_shape(birdup)
screen.register_shape(pipe)
screen.register_shape(pipe_upside_down)
screen.register_shape(gameover)
for n in range(len(bird_down)):
    screen.register_shape(bird_down[n])
for n in range(len(number_list)):
    screen.register_shape(number_list[n])
# -----------------------------------
object_ground = GroundManager(2)
bird = BirdF()
intro = Intro()
get_ready = GetReady()
start = Start()
ypipe = random.randint(-110, 110)
pipes = PipeManager(position1=(550, ypipe-(void_height+430)/2), position2=(550, ypipe+(void_height+430)/2))
screen.update()
screen.onscreenclick(mouseclick)
while x == 0:
    screen.tracer(1, 20)
    bird.beforestart()

screen.tracer(0)
start.ht()
intro.ht()
start.clear()
get_ready.ht()
scoreboard = ScoreCounterManager((6, 200), (-6, 200))
screen.update()

screen.listen()
screen.onkeypress(fun=bird.go_up, key="Up")

game_should_continue = True
while game_should_continue:
    ypipe = random.randint(-105, 125)
    bird.dist -= 3
    bird.state()
    object_ground.move()
    pipes.move()
    bird.fd(bird.dist)
    if pipes.tunnel_list[0][0].xcor() == -510:
        pipes.tunnel_list[0][0].ht()
        pipes.tunnel_list[0][1].ht()
        pipes.tunnel_list.remove(pipes.tunnel_list[0])
    if pipes.pipemoved % dist_between_pipe == 0:
        pipes.addpipe(position1=(550, ypipe-(void_height+461)/2), position2=(550, ypipe+(void_height+432)/2))
    if object_ground.ground_list[0].xcor() == -1400:
        object_ground.ground_list[0].ht()
        object_ground.remove_and_add()
    for thepipe in pipes.tunnel_list[0]:
        if abs(bird.xcor()-thepipe.xcor()) <= 65 and abs(bird.ycor()-thepipe.ycor()) <= 456/2:
            screen.tracer(1, 25)
            screen.onkeypress(fun=print(" "), key="Up")
            bird.goto(-250, -270)
            bird.clone()
            game_should_continue = False
    if bird.ycor() <= -200:
        screen.tracer(1, 25)
        screen.onkeypress(fun=print(" "), key="Up")
        bird.goto(-250, -270)
        game_should_continue = False
    if bird.xcor() == pipes.tunnel_list[0][0].xcor():
        scoreboard.counting_showing()
    time.sleep(0.0275)
    pipes.pipemoved += object_speed
screen.tracer(0)
scoreboard.game_over()
screen.update()
screen.exitonclick()
