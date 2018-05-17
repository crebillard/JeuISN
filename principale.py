"""crée le 17/04/18 avec Python 3.2"""

import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
from fonctions_jeu import* #importation des fonctions#
from menu import*
from jeu1 import*
from jeu2 import*
from menupause import*
from menuperdu import*
from score1 import*
from notice import*
from menuson import*

pygame.init() #initialisation de pygame#
jouer=1 #pour la boucle while#
jeu=0 #jeu sélectionné#
score=0 
musique=0

while jouer: #boucle faisant tourner le programme#
  
  if jeu==0: #pas de jeu sélectionné#
    jeu,jouer=menu(jeu,jouer) #ouverture du menu#

  if jeu==1: #jeu 1#
    jouer,jeu,score=jeu1(jouer,jeu,score,musique) #ouverture du jeu 1#

  if jeu==2:
    jouer,jeu,score=jeu2(jouer,jeu,score,musique)

  if jeu=="Record": #record sélectionné#
  	jeu,jouer=score1(jeu,jouer) #ouverture de la fenêtre de score#

  if jeu=="Son":
    jeu,jouer,musique=menuson(jeu,jouer,musique)

  if jeu=="Notice":
  	jeu,jouer=notice(jeu,jouer)

pygame.quit() #quitte pygame#
