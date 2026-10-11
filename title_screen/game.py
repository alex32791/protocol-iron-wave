import pygame

class Game:
  def __init__(self, screen):
    self.screen = screen
    self.running = True

  def draw(self):
      self.screen.fill((0, 0, 0))