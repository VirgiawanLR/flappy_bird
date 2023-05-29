from turtle import Turtle, Screen

ground = "./images/ground2.gif"
pipe = "./images/tunnel1.gif"
pipe_upside_down = "./images/tunnel1_upsidedown.gif"
position = (0, -300)
object_speed = 10

class GroundObject(Turtle):
    def __init__(self, xcord, ycord):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.goto(xcord, ycord)
        self.shape(ground)


class GroundManager():
    def __init__(self, ground_amount):
        self.ground_list = [GroundObject(n*1400, -300) for n in range(ground_amount)]
        self.screen = Screen()

    def move(self):
        self.screen.tracer(0)
        for theobject in self.ground_list:
            theobject.fd(object_speed)
        self.screen.update()

    def remove_and_add(self):
        self.ground_list.remove(self.ground_list[0])
        self.ground_list.append(GroundObject(1400, -300))

class PipeObject(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.setheading(180)
        self.shape(pipe)

class PipeObjectUpsideDown(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.setheading(180)
        self.shape(pipe_upside_down)


class PipeManager:
    def __init__(self, position1, position2):
        self.tunnel_list = [[PipeObject(position1), PipeObjectUpsideDown(position2)]]
        self.screen = Screen()
        self.pipemoved = 10

    def move(self):
        self.screen.tracer(0)
        for objects in self.tunnel_list:
            for sub_objects in objects:
                sub_objects.forward(object_speed)
        self.screen.update()

    def addpipe(self, position1, position2):
        self.tunnel_list.append([PipeObject(position1), PipeObjectUpsideDown(position2)])
