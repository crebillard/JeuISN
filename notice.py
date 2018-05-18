import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
import os

"""fonction permettan l'affichage de la notice"""
"""renvoie les valeurs de jeu et jouer"""

def notice(jeu,jouer):

  pygame.font.init()
  fenetre=pygame.display.set_mode((800,600)) # on initialise la fenetre

  notice = True #pour la boucle while#

  while notice : #tant que notice vaut True#

    pygame.display.flip() #rafraichissement de l'écran à chaque entrée dans la boucle#
    taillefont=22 
    font = pygame.font.SysFont("comicsansms",85, bold=True, italic=False) #on définit la police du titre
    font1 = pygame.font.SysFont("comicsansms",taillefont, bold=False, italic=False) #on définit la police du paragraphe
    titre = font.render("Notice",0,(200,200,200)) #on applique la police au titre

    fenetre.blit(titre,(290,80)) # on affiche le titre dans notre fenêtre
    x =0

    with open("notice.txt","r") as noticeT: #on ouvre le fichier "notice" pour le lire
        for line in noticeT: #pour chaque ligne de notre fichier "notice"
            line=line[0:-1] #suppression du dernier cractère de la ligne
            paragraphe = font1.render(line,0,(200,200,200)) #on applique la police à la ligne lue
            x = x + taillefont + 10 #position en dessous
            fenetre.blit(paragraphe,(10,175+x)) #on affiche la ligne lue à une certaine position dans la fenêtre
                
        for event in pygame.event.get(): #récupération des évènements
            if event.type == QUIT: #quitter
                notice = False #sortir de la boucle de la notice
                jouer=0 #sortir de la boucle principale
            elif event.type == pygame.KEYDOWN: #touche pressée
                if event.key==K_ESCAPE: #échap
                  notice = False #sortir de la notice
                  jeu=0 #pas de jeu sélectionné
  return(jeu,jouer) #renvoie les valeurs de variables


       


