import pygame

size=(640,480)

print('Setup Start')
pygame.init()
window=pygame.display.set_mode(size=size)
print('Setup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
