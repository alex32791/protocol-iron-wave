
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

   # draws the unit
   def draw(self, screen):
      pygame.draw.rect(screen, self.color, self.rect)

   # moves the unit
   def move(self):
      self.rect.x += self.speed

class Soldier(Unit):
    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health=100,
          speed=2,
          attack=10,
          color = COLORS["DARK_BLUE"],
          prio=None #machen!
          )

class Tank(Unit):
    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 4,
          attack = 50,
          color = COLORS["STEEL_GREY"]
          )

# Werte
class Sniper(Unit):
    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 4,
          attack = 50,
          color = COLORS["STEEL_GREY"]
          )

# Werte
class GatlingSoldier(Unit):
    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 4,
          attack = 50,
          color = COLORS["STEEL_GREY"]
          )

class Artillery(Unit):
    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 4,
          attack = 50,
          color = COLORS["STEEL_GREY"]
          )