import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
import os
from obstacles import*


def notice(jeu,jouer):

  pygame.font.init()
  fenetre=pygame.display.set_mode((800,600)) # on initialise la fenetre

  notice = True

  while notice :

    pygame.display.flip()
    taillefont=22
    font = pygame.font.SysFont("comicsansms",85, bold=True, italic=False) #on définit la police du titre
    font1 = pygame.font.SysFont("comicsansms",taillefont, bold=False, italic=False) #on définit la police du paragraphe
    titre = font.render("Notice",0,(200,200,200)) #on applique la police au titre

    fenetre.blit(titre,(290,80)) # on affiche le titre dans notre fenêtre
    x =0

    with open("notice.txt","r") as noticeT: #on ouvre le fichier "notice" pour le lire
        for line in noticeT: #pour chaque ligne de notre fichier "notice"
            line=line[0:-1]
            paragraphe = font1.render(line,0,(200,200,200)) #on applique la police à la ligne lue
            x = x + taillefont + 10
            fenetre.blit(paragraphe,(10,175+x)) #on affiche la ligne lue à une certaine position dans la fenêtre
                
        for event in pygame.event.get():
            if event.type == QUIT:
                notice = False
                jouer=0
            elif event.type == pygame.K_ESCAPE:
                notice = False
                jeu=0
  return(jeu,jouer)


       


