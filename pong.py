import pygame

# initialize pygame
pygame.init()

# create display surface
window = pygame.display.set_mode((1200, 800))

# fill screen white
window.fill("black")

# draw outlined rectangle
pygame.draw.rect(window, "white", [50, 50, 1100, 700], 2)

# draw line
pygame.draw.line(window, "white", [600, 50], [600, 750], 2)

# update pygame
while True: 
    pygame.display.update()