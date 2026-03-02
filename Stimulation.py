import pygame

pygame.init()

WITH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WITH, HEIGHT))

fps = 60
timer = pygame.time.Clock()

#game variables
wall_thickness = 10

def draw_walls():
    left= pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, (255, 255, 255), (WITH, 0), (WITH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, (255, 255, 255), (0, 0), (WITH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WITH, HEIGHT), wall_thickness)

    wall_list = [left, right, top, bottom]
    return wall_list

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))

    walls = draw_walls()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()