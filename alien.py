import pygame
import random  
import math

from pygame.sprite import Sprite
from math import atan2, cos, sin, radians, sqrt  


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien2.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)  
        self.y = float(self.rect.y)

    #def check_edges(self):
     #   """Return True if alien is at edge of screen."""
      #  screen_rect = self.screen.get_rect()
       # return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):  
        """Move the alien towards the ship."""  
        dx = self.ship.rect.x - self.rect.x  
        dy = self.ship.rect.y - self.rect.y  
  
        # 直接计算到飞船的角度  
        angle_to_ship = math.atan2(dy, dx)  
  
        # 不再添加随机角度，直接朝向飞船移动  
        # 但可以添加一个小的随机因子以保持一些不可预测性（如果需要）  
        random_factor = random.uniform(0.95, 1.05)  # 小范围随机因子  
        speed_x = math.cos(angle_to_ship) * self.settings.alien_speed * random_factor  
        speed_y = math.sin(angle_to_ship) * self.settings.alien_speed * random_factor  
  
        # 更新位置  
        self.rect.x += speed_x  
        self.rect.y += speed_y  
  
        # 确保外星人不会移出屏幕（如果需要）  
        if self.rect.left < 0:  
            self.rect.left = 0  
        if self.rect.right > self.screen.get_rect().right:  
            self.rect.right = self.screen.get_rect().right  
        if self.rect.top < 0:  
            self.rect.top = 0  
        # 底部通常不需要限制，因为外星人向下移动通常是为了进入屏幕  
  
        # 更新x和y属性以匹配rect的位置（如果需要）  
        self.x = self.rect.x  
        self.y = self.rect.y