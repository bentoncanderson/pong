import pygame
from controller import Controller

# initialize pygame
pygame.init()

# create display surface
window = pygame.display.set_mode((1200, 800))

# fill screen white
window.fill("black")

# draw table
pygame.draw.rect(window, "white", [50, 50, 1100, 700], 2)

# draw line down middle
pygame.draw.line(window, "white", [600, 50], [600, 750], 2)

# # draw player one's paddle
# pygame.draw.rect(window, "blue", [100, 100, 10, 100], 5)

# # draw player two's paddle 
# pygame.draw.rect(window, "blue", [1100, 100, 10, 100], 5)

# update pygame
c = Controller()
while True: 

    # update controller
    c.update()

    # draw player one's paddle
    pygame.draw.rect(window, "blue", [100, c.top, 10, 100], 5)

    # draw player two's paddle 
    pygame.draw.rect(window, "blue", [1100, c.top, 10, 100], 5)

    # update display
    pygame.display.update()