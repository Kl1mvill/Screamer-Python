import pygame

pygame.init()
screen = pygame.display.set_mode()
image = pygame.image.load("background.png").convert()
music = pygame.mixer.Sound("music.ogg")

music.play()  # Воспроизведение звука
screen.blit(image, (0, 0))
pygame.time.delay(100)  # Задержка на 0.1 секунды
pygame.display.set_caption("0")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ...
    screen.blit(image, (0, 0))
    pygame.display.flip()
