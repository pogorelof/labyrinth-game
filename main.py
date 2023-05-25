import pygame as pg
import maze_generator
import os


size_of_maze = 22

class Player(object):
    def __init__(self):
        self.rect = pg.Rect(32,32,size_of_maze,size_of_maze)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom


class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pg.Rect(pos[0], pos[1], size_of_maze, size_of_maze)


walls = []
player = Player()

os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((480,485))
pg.display.set_caption("Labyrinth")

maze = maze_generator.maze_generator(size_of_maze)

x = y = 0
for row in maze:
    for col in row:
        if col == '#':
            Wall((x,y))
        if col == '*':
            end_rect = pg.Rect(x, y, size_of_maze, size_of_maze)
        if col == 'P':
            player.rect = pg.Rect(x, y, size_of_maze,size_of_maze)
        x += size_of_maze
    y += size_of_maze
    x = 0

run = True
while run:

    clock.tick(60)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            run = False

    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
        player.move(-2,0)
    if key[pg.K_RIGHT]:
        player.move(2, 0)
    if key[pg.K_UP]:
        player.move(0, -2)
    if key[pg.K_DOWN]:
        player.move(0, 2)

    if player.rect.colliderect(end_rect):
        pg.quit()

    #отрисовка лабиринта
    screen.fill((0,0,0))
    for wall in walls:
        pg.draw.rect(screen, (255,255,255), wall.rect)
    pg.draw.rect(screen,(255, 200, 0), player.rect)
    pg.draw.rect(screen, (255, 0,0), end_rect)
    pg.display.flip()
    clock.tick(360)