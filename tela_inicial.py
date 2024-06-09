import pygame 
from pygame.locals import *
from sys import exit
pygame.init()

largura = 600
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo Forca')

# Carrega a música
#music = pygame.mixer.Sound("audios\supermario.mp3")

# Toca a música
#music.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()