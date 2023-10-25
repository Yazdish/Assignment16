import arcade

class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__()
        self.name = n
        self.center_x = x
        self.center_y = y
        self.color = c
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)