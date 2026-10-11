import pygame
from pathlib import Path

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

# load fonts
title_font = pygame.font.SysFont("arial", 48, bold=True)
button_font = pygame.font.SysFont("arial", 32, bold=True)

# define colors
white = (255, 255, 255)
cyan = (0, 220, 255)
dark_blue = (10, 25, 45)
red =(255,40,40)
gold = (255, 215, 0)
steel_white = (232, 237, 242)
steel_grey = (170, 184, 200)

# load background image
# used Path to load the image in all os
image_path = Path(__file__).parent / "images" / "background.png"
background = pygame.image.load(
    image_path
).convert()

#define menu buttons
button_labels = ["START", "CREDITS", "OPTIONS", "EXIT"]
button_width = 300
button_height = 60
button_spacing = 20

# store button rectangles
button_rects = {}

# start main game loop
running = True

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
        steel_grey
    )

    # center title horizontally
    title_x = (width - title.get_width()) // 2

    # draw title on screen
    screen.blit(title, (title_x, 40))

    # calculate height of all buttons
    total_height = (
        len(button_labels) *button_height+ (len(button_labels) - 1) * button_spacing
    )

    #draw menu buttons
    for index, label in enumerate(button_labels):

        #calculate button position
        button_x = (width - button_width) // 2

        button_y = (height - total_height) // 2 + index * (
            button_height + button_spacing 
        )

        #create button rectangle
        button_rect = pygame.Rect(
            button_x,
            button_y,
            button_width,
            button_height
        )

        #store button rectangle
        button_rects[label] = button_rect

        # check if mouse is over button
        mouse_pos = pygame.mouse.get_pos()
        mouse_over = button_rect.collidepoint(mouse_pos)

        #choose button colors
        if mouse_over:
            button_color = cyan
            text_color = dark_blue
        else:
            button_color = dark_blue
            text_color = white

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
            cyan,
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

    # update display
    pygame.display.flip()

# shut down pygame
pygame.quit()


