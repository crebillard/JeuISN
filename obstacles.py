"""crée le 09/04/18 avec Python 3.2"""
"""Module obstacle permettant les différentes actions
sur les obstacles: création, déplacement et collision"""

from random import randint #importation des bibliothèques#
import pygame 
from pygame.locals import*
import random

"""fonction permettant la création aléatoire d'un obstacle"""
"""prend comme paramètres les différents obstacles et leur position et retourne l'obstacle sélectionné, sa position et son type"""

def creation_obstacle(obstacle_bas,position_obstacle_bas,obstacle_haut,position_obstacle_haut,obstacle,position_obstacle,type_obstacle):
    n=randint(1,3)   #choix aléatoire d'un type d'obstacle#
    if n==1 or n==2:   #obstacle bas# 
      n=randint(0,2) #choix d"un obstacle bas parmi les trois existant#
      obstacle=obstacle_bas[n]  #affectation aux variables des caractéristiques de l'obstacle sélectionné#
      position_obstacle=position_obstacle_bas[n]
      type_obstacle=1
    else: #obstacle haut#
      n=randint(0,1) #choix d"un obstacle haut parmi les deux existant#
      obstacle=obstacle_haut[n]  #affectation aux variables des caractéristiques de l'obstacle sélectionné#
      position_obstacle=position_obstacle_haut[n]
      type_obstacle=2
    return(obstacle,position_obstacle,type_obstacle)

"""fonction permettant l'affichage d'un obstacle tout à droite de l'écran"""
"""prend pour paramètres le type d'obstacle et renvoie la position"""     

def spawn(position_obstacle,type_obstacle): #affichage d'un obstacle à sa position d'origine#
    if type_obstacle==1: #obstacle bas#
        rect=(700,530,25,25) #position#
    else: #obstacle ahut#
        rect=(700,400,25,25) 
    return pygame.Rect(rect)

"""fonction vérifiant la présence d'un obstacle sur l'écran"""

def presence_obstacle(position,present): 
    if position<=-100:   #vérification de la sorie de l'écran#
        present=0 
    else:
        present=1
    return(present)

"""fonction augmentant la vitesse en fonction du score"""
"""prend comme paramètre le score et renvoie le nombre de pixels"""

def vitesse(pixels,score):
    if score<30: #score bas#
      pixels=3 #vitesse basse#
    elif score<40:
      pixels=4
    elif score<70:
      pixels=5
    elif score<100:
      pixels=6
    elif score<150:
      pixels=7
    elif score<180:
      pixels=8
    elif score<220:
      pixels=9
    elif score>250: #score haut#
      pixels=10 #vitesse maximale#
    return(pixels)

"""fonction vérifiant la collision avec l'obstacle et la pièce"""
"""predn comme paramètres la position de l'objet et du personnage et renvoie crash"""

def crash_test(objet,perso,crash):
    if objet.colliderect(perso):   #vérification de la collision entre le personnage et l'objet#
        crash=1 #collision#
    else:
        crash=0 #collision#
    return(crash)

"""vérification de la présence de la pièce"""
"""prend la position de la pièce et renvoie présent"""

def presence_piece(position,present):
    n=randint(1,350) #entier aléatoire permettant une apparition irrégulière des pièces#
    if position<=-20 and n==1:   #vérification de la sortie de l'écran#
        present=0 #si la pièce est sortie et que l'entier aléatoire vaut 1#
    else:
        present=1
    return(present)

"""fonction permettant l'affichage de la pièce tout à droite de l'écran"""
"""prend comme paramètres la position de la pièce et le type d'obstacle"""

def piece_spawn(position_piece,type_obstacle):
    if type_obstacle==1: #obstacle bas#
      y=randint(300,480) #affichage de la pièce en haut#
    else: #obstacle haut#
      y=randint(480,500)  #affiche de la pièce en bas#
    return pygame.Rect((780,y,20,20))


    
