from random import randrange

import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

RES = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h


def gen_balls(n: int, space: pymunk.Space):
    for i in range(n):
        mass = 1
        radius = 20
        moment = pymunk.moment_for_circle(mass, 0, radius)

        body = pymunk.Body(mass, moment)

        body.position = WIDTH / 2, radius + 10

        shape = pymunk.Circle(body, radius, (0, 0))

        shape.elasticity = 0.9

        shape.color = [randrange(256) for i in range(4)]
        space.add(body, shape)


def gen_obstacles(space: pymunk.Space, a, layers):
    pass


def gen_dividers(space: pymunk.Space):
    segment_shape = pymunk.Segment(space.static_body, (2, HEIGHT), (WIDTH, HEIGHT), 26)
    space.add(segment_shape)
    segment_shape.elasticity = 0.8
    segment_shape.friction = 1.0
    
    #for space.


def main():
    display = pygame.display.set_mode()
    clock = pygame.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(display)

    space = pymunk.Space()
    pymunk.pygame_util.positive_y_is_up = False
    space.gravity = 0, 1000

    a = 100
    layers = 5

    gen_dividers(space)
    gen_obstacles(space, a, layers)
    gen_balls(10, space)

    while True:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        display.fill((0, 0, 0))
        space.step(0.01)
        space.debug_draw(draw_options)
        pygame.display.flip()


if __name__ == "__main__":
    main()
