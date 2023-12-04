import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

current_time = 0
button_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill("white")
            print(pygame.key.name(event.key))

    if current_time - button_press_time > 2000:
        screen.fill("black")

    current_time = pygame.time.get_ticks()
    # print(f"Current time: {current_time}\n\nButton Press Time: {button_press_time}")

    pygame.display.flip()
    clock.tick(60)
