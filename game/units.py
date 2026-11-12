
# a file for all units

from math import hypot  # Codex: Measure distance to the target

import pygame
from constants import COLORS

class Unit:
   # Codex: BEGIN unit position, rendering, and movement in grid coordinates
   def __init__(self, x, y, health, speed, attack, color):
      self.x = x
      self.y = y
      self.health = health
      self.speed = speed
      self.attack = attack
      self.color = color
      self.target = None

   # Codex: BEGIN define and draw the occupied cells
   @classmethod
   def footprint(cls, col, row):
      offsets = ((0, 0), (1, 0), (0, 1), (1, 1))
      return [(col + dx, row + dy) for dx, dy in offsets[:cls.size]]

   def draw(self, screen, grid_rect):
      for col, row in self.footprint(self.x, self.y):
         pygame.draw.rect(screen, self.color, grid_rect(col, row, 1))
   # Codex: END define and draw the occupied cells

   def move(self, dt):
      if self.target is None or (self.x, self.y) == self.target:
         return

      target_x, target_y = self.target
      dx = target_x - self.x
      dy = target_y - self.y
      distance = hypot(dx, dy)
      step = self.speed * dt
      if step >= distance:
         self.x, self.y = self.target
      else:
         self.x += dx * step / distance
         self.y += dy * step / distance
   # Codex: END unit position, rendering, and movement in grid coordinates

class Soldier(Unit):
    size = 1  # Codex: Number of occupied grid cells

    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health=100,
          speed=2,
          attack=10,
          color = COLORS["DARK_BLUE"],  # Codex: Temporary unit color
          #prio=None #machen!
          )

class Tank(Unit):
    size = 4  # Codex: Number of occupied grid cells

    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 2.5,
          attack = 50,
          color = COLORS["STEEL_GREY"],  # Codex: Temporary unit color
          )

# Werte
class Sniper(Unit):
    size = 1  # Codex: Number of occupied grid cells

    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 1.7,
          attack = 50,
          color = COLORS["GREEN"],  # Codex: Temporary unit color
          )

# Werte
class MachineGunner(Unit):
    size = 2  # Codex: Number of occupied grid cells

    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 1.5,
          attack = 50,
          color = COLORS["RED"],  # Codex: Temporary unit color
          )

class Artillery(Unit):
    size = 3  # Codex: Number of occupied grid cells

    def __init__(self, x, y):
       super().__init__(
          x, 
          y, 
          health = 300,
          speed = 1,
          attack = 50,
          color = COLORS["GOLD"],  # Codex: Temporary unit color
          )