from turtle import Turtle

getready = "./images/getready2.gif"
intro = "./images/flappy-bird-logo.gif"

class Intro(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(intro)
        self.goto(0, 180)

class GetReady(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(getready)
        self.goto(0, 90)

class Start(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.ht()
        self.write("Click Anywhere to Start", align="center", font=("Courier", 15, "bold"))
        self.goto(0, 30)
        self.write("Press 'Up' key to fly the Bird", align="center", font=("Courier", 15, "bold"))
