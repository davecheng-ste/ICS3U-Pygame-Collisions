"""
Description: Example of mouse event handling.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Examples")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize variables to track moues states
mouse_x, mouse_y = 0, 0
button_left, button_middle, button_right = False, False, False

# Define main loop
running = True
clock = pygame.time.Clock()  # Initialize clock object to cap frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position, unpack tuple of coordinates (int)
            mouse_x, mouse_y = pygame.mouse.get_pos()  
            # Get mouse button states, unpack tuple of button states (bool)
            button_left, button_middle, button_right = pygame.mouse.get_pressed() 

    # Draw graphics and output
    screen.fill(WHITE)

    if button_left:
        print(f"Left button pressed at position ({mouse_x}, {mouse_y})", end="\r")
    if button_right:
        print(f"Right button pressed at position ({mouse_x}, {mouse_y})", end="\r")

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()