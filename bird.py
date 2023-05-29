from turtle import Turtle

position = (-250, 0)
birdimage = "./images/bird3.gif"
birdup = "./images/bird3_up.gif"
bird_down = [
    "./images/bird3_down1.gif",
    "./images/bird3_down2.gif",
    "./images/bird3_down3.gif",
    "./images/bird3_down4.gif",
    "./images/bird3_down5.gif",
    "./images/bird3_down6.gif",
    "./images/bird3_down7.gif"
]


class BirdF(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fast")
        self.shape(birdimage)
        self.setheading(90)
        self.goto(position)
        self.dist = 20


    def beforestart(self):
        for i in range(6):
            self.fd(self.dist)
            self.dist -= 3
        for i in range(6):
            self.bk(self.dist)
            self.dist += 3
        for i in range(6):
            self.bk(self.dist)
            self.dist -= 3
        for i in range(6):
            self.fd(self.dist)
            self.dist += 3

    def go_up(self):
        self.dist = 0
        self.shape(birdup)
        self.goto(self.xcor(), self.ycor() +70)


    def state(self):
        if self.dist <= -32:
            self.shape(bird_down[6])
        elif self.dist <= -30:
            self.shape(bird_down[5])
        elif self.dist <= -28:
            self.shape(bird_down[4])
        elif self.dist <= -26:
            self.shape(bird_down[3])
        elif self.dist <= -24:
            self.shape(bird_down[2])
        elif self.dist <= -20:
            self.shape(bird_down[1])
        elif self.dist <= -18:
            self.shape(bird_down[0])
        else:
            self.shape(birdup)
