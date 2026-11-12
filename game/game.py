
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
    self.bar_height = 70  # Codex: Shared height for the button bar
    self.running = True

    self.hq_image = pygame.image.load(HQ_IMAGE).convert_alpha()
    self.hq_image = pygame.transform.scale(self.hq_image, (150, 150))

    # load fonts
    self.font = pygame.font.SysFont("arial", 15)

    # save buttons
    button_space = 150
    self.game_buttons = {
       UNITY_TYPES[0]: pygame.Rect(20, self.screen_height - 10 - 10, 140, 40),
       UNITY_TYPES[1]: pygame.Rect(20 + button_space, self.screen_height - 10 - 10, 140, 40),
       UNITY_TYPES[2]: pygame.Rect(20 + button_space * 2, self.screen_height - 10 - 10, 140, 40),
       UNITY_TYPES[3]: pygame.Rect(20 + button_space * 3, self.screen_height - 10 - 10, 140, 40),
       UNITY_TYPES[4]: pygame.Rect(20 + button_space * 4, self.screen_height - 10 - 10, 140, 40)
    }

    # Codex: BEGIN unit class mapping
    self.unit_classes = {
      "Soldier": Soldier,
      "Artillery": Artillery,
      "Sniper": Sniper,
      "Machine Gunner": MachineGunner,
      "Tank": Tank,
    }
    # Codex: END unit class mapping

    # grid slots
    self.grid_cols = 8
    self.grid_rows = 24

    self.units = []
    self.selected_unit = None  # Codex: Unit class awaiting a destination

  # draws the game
  def draw_game(self):
    # Codex: BEGIN draw the grid, placement highlights, and HQ
    self.update_layout()
    self.screen.fill(COLORS["CYAN"])
    self.draw_gird()
    self.screen.blit(self.hq_image, self.hq_rect)
    self.draw_placement_highlights()
    # Codex: END draw the grid, placement highlights, and HQ

    self.place_units()

    # calls the functions
    self.draw_buttons()


  def draw_buttons(self):
    # Codex: Draw the button bar background
    bar = pygame.Rect(
      0, self.screen_height - self.bar_height,
      self.screen_width, self.bar_height
    )
    pygame.draw.rect(self.screen, (35, 45, 60), bar)

    #draw buttons
    for label, rect in self.game_buttons.items():
      # Codex: BEGIN highlight the selected unit button
      selected = self.unit_classes[label] is self.selected_unit
      button_color = COLORS["GREEN"] if selected else COLORS["DARK_BLUE"]
      # Codex: END highlight the selected unit button
      pygame.draw.rect(
        self.screen,
        button_color,
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
    for rect in self.game_buttons.values():
      rect.bottom = self.screen_height - 10

  # Codex: BEGIN grid layout and unit placement
  def update_layout(self):
    self.resize_buttons()
    grid_height = max(0, self.screen_height - self.bar_height)
    self.slot_size = grid_height / self.grid_rows
    grid_width = self.grid_cols * self.slot_size
    self.grid_x = (self.screen_width - grid_width) / 2 - self.screen_width * 0.15
    self.grid_y = 0
    self.hq_rect = self.hq_image.get_rect(
      bottomleft=(10, self.screen_height // 2)
    )

  def grid_rect(self, col, row, size):
    left = round(self.grid_x + col * self.slot_size)
    top = round(self.grid_y + row * self.slot_size)
    right = round(self.grid_x + (col + size) * self.slot_size)
    bottom = round(self.grid_y + (row + size) * self.slot_size)
    return pygame.Rect(left, top, right - left, bottom - top)

  # Codex: BEGIN validate each occupied cell
  def valid_placements(self, unit_class):
    occupied = {
      cell
      for unit in self.units
      for cell in unit.footprint(*unit.target)
    }
    for row in range(self.grid_rows):
      for col in range(self.grid_cols):
        if all(
          x < self.grid_cols and y < self.grid_rows and (x, y) not in occupied
          for x, y in unit_class.footprint(col, row)
        ):
          yield col, row
  # Codex: END validate each occupied cell

  def draw_placement_highlights(self):
    if self.selected_unit is None or self.slot_size <= 0:
      return

    mouse_pos = pygame.mouse.get_pos()
    hovered_cell = None
    for col, row in self.valid_placements(self.selected_unit):
      cell = self.grid_rect(col, row, 1)
      pygame.draw.rect(self.screen, COLORS["GREEN"], cell, 2)
      if cell.collidepoint(mouse_pos):
        hovered_cell = (col, row)

    # Codex: BEGIN preview the exact cells the unit will occupy
    if hovered_cell is not None:
      for col, row in self.selected_unit.footprint(*hovered_cell):
        pygame.draw.rect(self.screen, COLORS["GOLD"], self.grid_rect(col, row, 1), 3)
    # Codex: END preview the exact cells the unit will occupy

  def handle_event(self, event):
    if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
      return

    self.update_layout()
    for label, rect in self.game_buttons.items():
      if rect.collidepoint(event.pos):
        self.selected_unit = self.unit_classes[label]
        return

    if self.selected_unit is None or self.slot_size <= 0:
      return

    unit_class = self.selected_unit
    for col, row in self.valid_placements(unit_class):
      if self.grid_rect(col, row, 1).collidepoint(event.pos):
        spawn_x = (self.hq_rect.centerx - self.grid_x) / self.slot_size
        spawn_y = (self.hq_rect.bottom - self.grid_y) / self.slot_size
        width = max(col for col, _ in unit_class.footprint(0, 0)) + 1
        unit = unit_class(x=spawn_x - width / 2, y=spawn_y)
        unit.target = (col, row)
        self.units.append(unit)
        self.selected_unit = None
        return
  # Codex: END grid layout and unit placement

  # Codex: BEGIN draw and update units in grid coordinates
  def place_units(self):
    for unit in self.units:
      unit.draw(self.screen, self.grid_rect)

  def update(self, dt):
    for unit in self.units:
      unit.move(dt)
  # Codex: END draw and update units in grid coordinates

  # draws grid on screen
  def draw_gird(self):
    # Codex: BEGIN use the shared grid layout
    if self.slot_size <= 0:
      return

    grid = self.grid_rect(0, 0, 1)
    grid_right = round(self.grid_x + self.grid_cols * self.slot_size)
    grid_bottom = round(self.grid_y + self.grid_rows * self.slot_size)
    # Codex: END use the shared grid layout

    for col in range(self.grid_cols + 1):
      x = self.grid_rect(col, 0, 1).left  # Codex: Align lines with cells
      line_width = 3 if col % 2 == 0 else 1

      pygame.draw.line(
        self.screen,
        COLORS["DARK_BLUE"],
        (x, grid.top),  # Codex: Use shared grid edges
        (x, grid_bottom),
        line_width
      )

    for row in range(self.grid_rows + 1):
      y = self.grid_rect(0, row, 1).top  # Codex: Align lines with cells
      line_width = 3 if row % 2 == 0 else 1

      pygame.draw.line(
        self.screen,
        COLORS["DARK_BLUE"],
        (grid.left, y),  # Codex: Use shared grid edges
        (grid_right, y),
        line_width
      )

