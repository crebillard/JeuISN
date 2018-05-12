import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
import os
from obstacles import*

pygame.init()
pygame.font.init()
pygame.mixer.init()
fenetre=pygame.display.set_mode((800,600))
violet=(153,51,255)
rose=(255,0,153)
bleu=(51,51,255)
rouge=(255,0,0)



rouge=(200,0,0) #RGB pour la couleur rouge voulue#
vert=(0,200,0) #RGB pour la couleur verte voulue#
menucolor=(0,0,0) #couleur du fond#
