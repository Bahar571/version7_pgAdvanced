import sys
import pygame as pg
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *


class Game:
    def __init__(self):
        self.object_renderer = None
        self.raycasting = None
        self.player = None
        self.map = None
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.static_sprite = None
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps(): .1f}")

    def draw(self):
        # self.screen.fill("black")
        self.object_renderer.draw()

    @staticmethod
    def check_event():
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()