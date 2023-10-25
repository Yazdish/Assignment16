
from typing import Optional, Tuple
import arcade
from ball import Ball
from rocket import Rocket
import pyglet

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 800, height= 500, title= "Pong 2023")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player1 = Rocket(40, self.height // 2, arcade.color.RED, "Yazdan")
        self.player2 = Rocket(self.width - 40, self.height // 2, arcade.color.BLUE, "MAMMAD")
        self.ball = Ball(self)
    
    def on_draw(self):
        arcade.start_render()
            
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30, self.height - 30, arcade.color.WHITE, border_width= 10)            
        arcade.draw_line(self.width // 2, 30, self.width // 2, self.height - 30, arcade.color.WHITE, line_width= 10)
            
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
            
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # self.player1.center_x = x
        if self.player1.height < y < self.height - self.player1.height:
            self.player1.center_y = y
        
    def on_update(self, delta_time: float):
        self.ball.move()

game = Game()
arcade.run()