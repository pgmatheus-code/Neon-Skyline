import pygame

print('Setup Started')
pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print('Setup Ended')

print('Loop Started')
while True:
    # checking all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # end pygame
            quit() # close window