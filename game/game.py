
# file for the game part

import pygame
from constants import HQ_IMAGE, COLORS, UNITY_TYPES
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
       UNITY_TYPES[0]: pygame.Rect(20, self.screen_height - 10 - 10, 160, 50)
    }

    # grid slots
    self.slot_size = 64
    self.grid_cols = 8
    self.grid_rows = 24

    self.units = []

  # draws the game
  def draw_game(self):
    self.resize_buttons()

    self.screen.fill(COLORS["CYAN"])
    self.draw_gird()

    # load headquaters image into game
    hq_map_palcement = self.screen_height / 2 - 150
    self.screen.blit(self.hq_image, (10, hq_map_palcement))

    self.unit_place_x = 75
    self.unit_place_y = hq_map_palcement + 150

    self.place_units()

    # calls the functions
    self.draw_buttons()


  def draw_buttons(self):
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

  def resize_buttons(self):
    # get new screen size
    self.screen_width, self.screen_height = self.screen.get_size()

    # place button 
    self.game_buttons["Soldier"].bottom = self.screen_height - 10

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if self.game_buttons[UNITY_TYPES[0]].collidepoint(event.pos):
          soldier = Soldier(x=self.unit_place_x, y=self.unit_place_y)
          self.units.append(soldier)

  # places units
  def place_units(self):
    for unit in self.units:
      unit.draw(self.screen)
  
  # moves all units
  def update(self):
    for unit in self.units:
      unit.move()

  # draws grid on screen
  def draw_gird(self):
    # place grid
    width, height = self.screen.get_size()
    self.slot_size = height / self.grid_rows
    grid_width = self.grid_cols * self.slot_size
    grid_heigth = height
    self.grid_y = 0
    self.grid_x = (width - grid_width) / 2 - width * 0.15

    for col in range(self.grid_cols + 1):
      x = self.grid_x + col * self.slot_size
      line_width = 3 if col % 2 == 0 else 1

      pygame.draw.line(
        self.screen,
        COLORS["DARK_BLUE"],
        (x, self.grid_y),
        (x, self.grid_y + grid_heigth),
        line_width
      )

    for row in range(self.grid_rows + 1):
      y = self.grid_y + row * self.slot_size
      line_width = 3 if row % 2 == 0 else 1

      pygame.draw.line(
        self.screen,
        COLORS["DARK_BLUE"],
        (self.grid_x, y),
        (self.grid_x + grid_width, y),
        line_width
      )

