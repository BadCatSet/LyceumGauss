from random import randrange

import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

RES = WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
a = 50
layers = 2


def gen_balls(n: int, space: pymunk.Space):
    for i in range(n):
        mass = 1
        radius = 20
        moment = pymunk.moment_for_circle(mass, 0, radius)

        body = pymunk.Body(mass, moment)

        body.position = WIDTH / 2, radius + 10

        shape = pymunk.Circle(body, radius, (0, 0))

        shape.elasticity = 0.9

        shape.color = [randrange(256) for _ in range(4)]
        space.add(body, shape)


def gen_obstacles(space: pymunk.Space):
    dx, dy = WIDTH / 2, HEIGHT * 0.3
    for layer in range(layers):
        for pos in range(layer + 1):
            body = pymunk.Body()
            body.position = int(dx - a * layer / 2 + a * pos), \
                            int(dy + a * layer)
            shape = pymunk.Circle(body, 20, (0, 0))
            shape.color = [randrange(256) for _ in range(4)]

            space.add(shape, body)


def gen_dividers(space: pymunk.Space):
    segment_shape = pymunk.Segment(space.static_body, (2, HEIGHT), (WIDTH, HEIGHT), 26)
    space.add(segment_shape)
    segment_shape.elasticity = 0.8
    segment_shape.friction = 1.0

    for i in range(a):
        segment_shape = pymunk.Segment(space.static_body,
                                       (WIDTH / layers * i, HEIGHT * 0.9),
                                       (WIDTH / layers * i, HEIGHT), 26)
        space.add(segment_shape)
        segment_shape.elasticity = 0.8
        segment_shape.friction = 1.0


def main():
    display = pygame.display.set_mode()
    clock = pygame.time.Clock()
    draw_options = pymunk.pygame_util.DrawOptions(display)

    space = pymunk.Space()
    pymunk.pygame_util.positive_y_is_up = False
    space.gravity = 0, 1000

    gen_dividers(space)
    gen_obstacles(space)
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
