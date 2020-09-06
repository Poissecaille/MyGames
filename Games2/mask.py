import pygame, sys, random
pygame.init()
window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.font.init()
pygame.mixer.init()

chat = pygame.image.load("D:/DEVOP/MyGames/Games2/images/cat.png").convert_alpha()
rectChat = chat.get_rect()
# vChat = int(round(150/FPS))

souris = pygame.image.load("D:/DEVOP/MyGames/Games2/images/mouse.png").convert_alpha()
rectSouris = souris.get_rect()
rectSouris.center = rectScreen.center

police = pygame.font.Font(None,50)
texte = police.render("Collision",True,pygame.Color("#000000"))
rectTexte = texte.get_rect()
rectTexte.midtop = rectScreen.midtop

keys = pygame.key.get_pressed()

# ... A COMPLETER AVEC LE CODE DE VOTRE JEU ...
vxChat = 0
vyChat = 0

if keys[pygame.K_RIGHT]:
    vxChat = vChat

if keys[pygame.K_LEFT]:
    vxChat = -vChat

if keys[pygame.K_UP]:
    vyChat = -vChat

if keys[pygame.K_DOWN]:
    vyChat = vChat

rectChat = rectChat.move(vxChat, vyChat).clamp(rectScreen)

screen.fill(pygame.Color("#FF0000"))

screen.blit(souris, rectSouris)
screen.blit(chat, rectChat)

if rectChat.colliderect(rectSouris):
    # Code executé si les rectangles se chevauchent
    screen.blit(texte, rectTexte)