import pygame
import random
num = random.randint(0, 100)
print(num)

W = 480
H = 360
SILVER = (192, 192 , 192)
BLACK = (0, 0, 0)
numeral = ""
move = 1
block = 0
start = 1
OUTSIDE_BG = (0, -100)

pygame.init()
pygame.display.set_caption("Угадай число")
sreen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont("Arial", 28, True, False)
font2 = pygame.font.SysFont("Arial", 14, True, False)
font_box = pygame.Surface((W - 20, font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))

bg = pygame.image.load("Image/room.png")
bg_rect = bg.get_rect(topleft=(0, 0))
cat = pygame.image.load("Image/cat.png")
cat_rect = cat.get_rect(topleft=(70, 220))

owl = pygame.image.load("Image/owl.png")
owl_rect = owl.get_rect(topleft=(210, 120))

dog = pygame.image.load("Image/owl.png")
dog_rect = dog.rect_rect(topleft=(410, 220))

dialog = pygame.image.load("Image/dialog.png")
dialog_rect = dialog.get_rect()
dialog_cat_pos = (cat_rect.x, cat_rect.y - dialog_rect.h)
dialog_dog_pos = (dog_rect.x - dialog_rect.w // 2, dog_rect.y - dialog_rect.h)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    screen.blit(bg, bg_rect)
    screen.blit(cat, cat_rect)
    screen.blit(dog, dog_rect)
    screen.blit(owl, owl_rect)
    screen.blit(font_box, font_rect)
    font_box.fill(SILVER)
    pygame.display.update()

            