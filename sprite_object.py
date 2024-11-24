import math
import pygame
import pygame as pg
from settings import *


class SpriteObject:
    def __init__(self, game, path="resources/sprites/static_sprites/candlebra.png", pos=(10.5, 3.5)):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_HEIGHT = self.IMAGE_WIDTH // 2
        self.theta = None
        self.dx = None
        self.dy = None
        self.dist = 1
        self.norm_dist = 1
        self.screen_x = None
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()  # نسبت طول به عرض
        self.sprite_half_width = None

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, proj_width, proj_height)

        self.sprite_half_width = proj_width // 2
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy   #توابع دیگر هم دسترسی داشته باشند
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau  # 2pi
        delta_rays = delta / DELTA_ANGLE  # تعداد اشعه ها
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)  # فاصله اقلیدسی یا نورم
        norm_dist = self.dist * math.cos(delta)  # اثر تنگ ماهی را از بین می برد

        if -self.IMAGE_HALF_WIDTH < (self.screen_x < self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()
