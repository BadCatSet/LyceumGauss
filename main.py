import pygame
import pymunk
import pymunk.pygame_util

RES = WIDTH, HEIGHT = 800, 800


def gen_balls(n: int):
    for i in range(n):
        mass = 1
        radius = 20
        moment = pymunk.moment_for_circle(mass, 0, radius)

        body = pymunk.Body(mass, moment)

        body.position = WIDTH / 2, radius + 10

        #shape = pymunk.Circle.


def gen_obstacles():
    pass


def gen_dividers():
    pass


def main():
    pygame.init()
    display = pygame.display.set_mode()
    clock = pygame.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(display)

    space = pymunk.Space()
    pymunk.pygame_util.positive_y_is_up = False
    space.gravity = 0, 1000

    while True:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        space.step(0.01)
        space.debug_draw(draw_options)


if __name__ == "__main__":
    main()
