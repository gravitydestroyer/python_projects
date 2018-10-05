#!/usr/bin/env python3

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

# Define colours
black = (0, 0, 0)
white = (255, 255, 255)

# Car image size
car_width = 40
car_height = 80

# Debris image size
debris_width = 35
debris_height = 32

# Settings for display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racing')

# For FPS
gameClock = pygame.time.Clock()

# Car Image
carImage = pygame.image.load('../docs/Car.png')

# Debris Image
debrisImage = pygame.image.load('../docs/Debris.png')

# Debris dodged
def debrisDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


# Display messages to the screen
def text_objects(text, font):

    # The arguments are (what we want to render, anti-aliasing, colour)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(textToPrint):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(textToPrint, largeText)
    TextRect.center = ((display_width/2), (display_height/2))

    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    # Wait for 2 seconds before restarting the game
    time.sleep(1)


# Function for debris
def debris(debris_x, debris_y):
    gameDisplay.blit(debrisImage, (debris_x, debris_y))


# Functions for location of car image
def carLocation(x, y):
    gameDisplay.blit(carImage, (x, y))


# Crash definition
def carCrashed(debrisCounter):
    message_display(('You Crashed !!!' + str(debrisCounter)))

    # Restart the game
    game_loop()


# Quit game
def quitGame():
    message_display('Game Over')
    pygame.quit()
    quit()


# The game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.45)

    x_change = 0
    y_change = 0

    debris_x = random.randrange(0, display_width)
    debris_y = -600

    debris_speed = 5

    dodgedDebrisCounter = 0

    # For if the car crashes
    gameExit = False

    # Game loop
    while not gameExit:

        # Event handling loop
        for event in pygame.event.get():

            # Checks if you close the window by pressing the x on the window menu
            if event.type == pygame.QUIT:
                quitGame()

            # For movement keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or(event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                    x_change = 0
                    y_change = 0

        x += x_change
        y += y_change

        # Completely overwrite the window with white
        gameDisplay.fill(white)

        # Display the debris
        debris(debris_x, debris_y)
        debris_y += debris_speed

        # Display the car
        carLocation(x, y)

        # Dodge counter
        debrisDodged(dodgedDebrisCounter)

        # Crash parameters
        if x > (display_width - car_width) or x < 0:
            carCrashed(dodgedDebrisCounter)
        if y > (display_height - car_height) or y < 0:
            carCrashed(dodgedDebrisCounter)

        # Debris respawn
        if debris_y > display_height:
            # -32 is the image height
            debris_y = -32
            debris_x = random.randrange(0, display_width)
            dodgedDebrisCounter += 1
            debris_speed += 1

        # Collision parameters
        if y < (debris_y + debris_height):
            if (x > debris_x) and (x < (debris_x + debris_width)) or (x + car_width > debris_x) and (x + car_width < (debris_x + debris_width)):
                carCrashed(dodgedDebrisCounter)

        # Updates the display, and the diff. b/w this and flip() is that this would
        # always update the whole screen while update() is only the required parts
        pygame.display.update()

        # Moving on to the next frame (tick(FPS))
        gameClock.tick(120)


# Running the game
game_loop()
