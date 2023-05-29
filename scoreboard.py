from turtle import Turtle
number_list = [
    "./images/0.gif",
    "./images/1.gif",
    "./images/2.gif",
    "./images/3.gif",
    "./images/4.gif",
    "./images/5.gif",
    "./images/6.gif",
    "./images/7.gif",
    "./images/8.gif",
    "./images/9.gif"
]

scoresboard = "./images/scoreboard.gif"
gameover = "./images/GameOver.gif"

class ScoreCounter(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape(number_list[0])
        self.stamp()


class ScoreCounterManager:
    def __init__(self, position1, position2):
        self.count_list = [ScoreCounter(position1), ScoreCounter(position2)]
        self.counter = 0

    def counting_showing(self):
        self.counter += 1
        self.number_lists = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.position = 1
        self.show = f"{self.counter}"
        if self.counter < 10:
            self.show = f"0{self.counter}"
            for letters in self.show:
                for item in self.number_lists:
                    if letters == item:
                        self.count_list[self.position].clear()
                        self.count_list[self.position].shape(number_list[int(letters)])
                        self.count_list[self.position].stamp()
                        break
                self.position -= 1
        else:
            for letters in self.show:
                for item in self.number_lists:
                    if letters == item:
                        self.count_list[self.position].clear()
                        self.count_list[self.position].shape(number_list[int(letters)])
                        self.count_list[self.position].stamp()
                        break
                self.position -= 1

    def game_over(self):
        self.count_list[0].goto(0, 0)
        self.count_list[0].shape(gameover)
        self.count_list[0].stamp()
