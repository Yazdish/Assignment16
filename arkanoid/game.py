from typing import Optional, Tuple
import arcade
import pyglet

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500, height= 800, title="Arkanoid")

    def on_draw(self):
        arcade.start_render()

        arcade.finish_render()

    def on_update(self):
        ...

    def on_key_release(self):
        ...

    def on_mouse_motion(self):
        ...

game = Game()
arcade.run()