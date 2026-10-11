
# file for the game part

import pygame
from constants import HQ_IMAGE, GREEN

# a class for the game
class Game:
  def __init__(self, screen, width, height):
    self.screen = screen
    self.screen_width = width
    self.screen_height = height
    self.running = True

    self.hq_image = pygame.image.load(HQ_IMAGE).convert_alpha()
    self.hq_image = pygame.transform.scale(self.hq_image, (150, 150))

  # draws the game
  def draw(self):
      self.screen.fill(GREEN)

      # load headquaters image into game
      self.screen.blit(self.hq_image, (10, self.screen_height / 2))