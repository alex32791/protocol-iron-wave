import pygame
from pathlib import Path
from game import Game

# constatns 
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

#define menu buttons
BUTTON_LABELS = ["START", "CREDITS", "OPTIONS", "EXIT"]
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 60
BUTTON_SPACING = 20

# a function for the title screen
def draw_title_screen(screen, background, button_rects):

    # load fonts
    title_font = pygame.font.SysFont("arial", 48, bold=True)
    button_font = pygame.font.SysFont("arial", 32, bold=True)

    # get current window dimensions
    width, height = screen.get_size()

    # resize background image
    scaled_background = pygame.transform.scale(
        background, (width, height)
    )

    # Draw background image
    screen.blit(scaled_background, (0, 0))

    # draw game title
    title = title_font.render(
        "PROTOCOL: IRON WAVE",
        True,
        STEEL_GREY
    )

    # center title horizontally
    title_x = (width - title.get_width()) // 2

    # draw title on screen
    screen.blit(title, (title_x, 40))

    # calculate height of all buttons
    total_height = (
        len(BUTTON_LABELS) * BUTTON_HEIGHT + (len(BUTTON_LABELS) - 1) * BUTTON_SPACING
    )

    #draw menu buttons
    for index, label in enumerate(BUTTON_LABELS):

        #calculate button position
        button_x = (width - BUTTON_WIDTH) // 2

        button_y = (height - total_height) // 2 + index * (
            BUTTON_HEIGHT + BUTTON_SPACING 
        )

        #create button rectangle
        button_rect = pygame.Rect(
            button_x,
            button_y,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )

        #store button rectangle
        button_rects[label] = button_rect

        # check if mouse is over button
        mouse_pos = pygame.mouse.get_pos()
        mouse_over = button_rect.collidepoint(mouse_pos)

        #choose button colors
        if mouse_over:
            button_color = CYAN
            text_color = DARK_BLUE
        else:
            button_color = DARK_BLUE
            text_color = WHITE

        #draw button background
        pygame.draw.rect(
            screen,
            button_color,
            button_rect,
            border_radius=12
        )

        #draw button border
        pygame.draw.rect(
            screen,
            CYAN,
            button_rect,
            width=3,
            border_radius= 12
            )

        #draw button text
        button_text = button_font.render(
            label,
            True,
            text_color
        )

        #center text inside button
        text_x =(
            button_rect.centerx
            - button_text.get_width() //2
        )

        text_y = (
            button_rect.centery
            - button_text.get_height() //2
        )

        #draw text on screen
        screen.blit(button_text, (text_x, text_y))

def main():

    pygame.init()

    # get screen dimensions
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h

    # set windo dimension with some space around it
    width = int(screen_width * 0.9)
    height = int(screen_height * 0.8)

    # create resizable game window
    screen = pygame.display.set_mode(
        (width, height),
        pygame.RESIZABLE  
    )
    pygame.display.set_caption("Protocol: Iron Wave")

    # load background image
    # used Path to load the image in all os
    image_path = Path(__file__).parent / "images" / "background.png"
    background = pygame.image.load(
        image_path
    ).convert()

    # store button rectangles
    button_rects = {}

    # start main game loop
    running = True

    # first state
    state = TITLE_STATE

    while running:

        # handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #check mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    #check which button was clicked
                    for label, rect in button_rects.items():
                        if rect.collidepoint(event.pos):

                            if label == "EXIT":
                                running = False

                            elif label == "START":
                                game = Game(screen)
                                state = GAME_STATE

        if state == TITLE_STATE:
            draw_title_screen(screen, background, button_rects)

        elif state == GAME_STATE:
            game.draw() 

        # update display
        pygame.display.flip()

    # shut down pygame
    pygame.quit()


if __name__ == "__main__":
    main()

