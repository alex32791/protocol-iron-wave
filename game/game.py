
# file for the game part

import pygame
from constants import HQ_IMAGE, COLORS
from units import *

# a class for the game
class Game:
  def __init__(self, screen, width, height):
    self.screen = screen
    self.screen_width = width
    self.screen_height = height
    self.running = True

    self.hq_image = pygame.image.load(HQ_IMAGE).convert_alpha()
    self.hq_image = pygame.transform.scale(self.hq_image, (150, 150))

    # load fonts
    self.font = pygame.font.SysFont("arial", 15)

    # save buttons
    self.game_buttons = {
       "Soldier": pygame.Rect(20, self.screen_height - 10 - 10, 160, 50)
    }

    self.units = [
       
    ]

  # draws the game
  def draw(self):
    self.screen.fill(COLORS["CYAN"])

    # load headquaters image into game
    hq_map_palcement = self.screen_height / 2
    self.screen.blit(self.hq_image, (10, hq_map_palcement))

    #draw buttons
    for label, rect in self.game_buttons.items():
      pygame.draw.rect(
        self.screen,
        COLORS["DARK_BLUE"],
        rect,
        border_radius=10
      )

    text = self.font.render(label, True, COLORS["WHITE"])
    text_rect = text.get_rect(center=rect.center)
    self.screen.blit(text, text_rect)
