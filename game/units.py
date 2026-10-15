
# a file for all units

import pygame
from constants import COLORS

class Unit:
   def __init__(self, x, y, health, speed, attack, color):
      self.rect = pygame.Rect(x, y, 40, 40)
      self.x = x
      self.y = y
      self.health = health
      self.speed = speed
      self.attack = attack
      self.color = color

   def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.rect)


class Soldier(Unit):
    def __init__(self, x, y, health, speed, attack):
       super().__init__(
          x, 
          y, 
          health = health,
          speed = speed,
          attack = attack,
          color = COLORS["DARK_BLUE"]
          )

class Tank(Unit):
    def __init__(self, x, y, health, speed, attack):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 4,
          attack = 50,
          color = COLORS["STEEL_GREY"]
          )