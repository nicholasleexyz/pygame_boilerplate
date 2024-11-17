import pygame
import sys

PURPLE = pygame.color.Color("purple")
running = True
screen = None
clock = None


def initialize_game():
    global screen
    global clock

    screen = initialize_screen()
    clock = pygame.time.Clock()


def initialize_screen():
    resolution = (800, 600)
    pygame.init()
    _screen = pygame.display.set_mode(resolution)
    return _screen


def handle_events():
    global running
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False


def game(clock):
    handle_events()
    clock.tick(60)


def render(screen):
    screen.fill(PURPLE)


def render_checkerboard(screen):
    size = 64
    for y in range(8):
        for x in range(8):
            c = pygame.Color("black") if y % 2 == x % 2 else pygame.Color("white")
            r = (x * size, y * size, size, size)
            pygame.draw.rect(screen, c, r)


def main():
    global running
    global clock
    global screen

    print("running main()")

    initialize_game()

    while running:
        render(screen)
        render_checkerboard(screen)
        pygame.display.flip()
        game(clock)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
