import pygame

pygame.init()

WITH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WITH, HEIGHT))

fps = 60
timer = pygame.time.Clock()

#game variables
wall_thickness = 10

class Ball:
    def __init__(self, x, y, radius, color, mass, velocity_x, velocity_y, retention,id):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.retention = retention
        self.id = id
    

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


def draw_walls():
    left= pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, (255, 255, 255), (WITH, 0), (WITH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, (255, 255, 255), (0, 0), (WITH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT), (WITH, HEIGHT), wall_thickness)

    wall_list = [left, right, top, bottom]
    return wall_list

ball1 = Ball(50, 50,30, (104, 0, 0), 100, 0, 0, 0.9,1)
ball2 = Ball(500, 500,50, (50, 0, 0), 300, 0, 0, 0.9,2)

#main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 0))

    walls = draw_walls()
    ball1.draw()
    ball2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()