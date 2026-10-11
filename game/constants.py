from pathlib import Path

# cdefine strings
TITLE_STATE = "title"
GAME_STATE = "game"

# define colors
WHITE = (255, 255, 255)
CYAN = (0, 220, 255)
DARK_BLUE = (10, 25, 45)
RED =(255,40,40)
GOLD = (255, 215, 0)
STEEL_WHITE = (232, 237, 242)
STEEL_GREY = (170, 184, 200)
GREEN = (0, 100, 0)

#define menu buttons
BUTTON_LABELS = ["START", "CREDITS", "OPTIONS", "EXIT"]
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 60
BUTTON_SPACING = 20

# paths to all images for the game
TITLE_BACKGROUND = Path(__file__).parent / "images" / "background.png"
HQ_IMAGE = Path(__file__).parent / "images" / "headquarters.png"