"""crée le 09/04/18 avec Python 3.2"""
"""Module fonctions jeu permettant les différentes actions
sur les obstacles, le personnage et les fonds: création, déplacement et collision"""

from random import randint #importation des bibliothèques#
import pygame 
from pygame.locals import*
import random

"""fonction permettant la création aléatoire d'un obstacle"""
"""prend comme paramètres les différents obstacles et leur position et retourne l'obstacle sélectionné, sa position et son type"""

def creation_obstacle(obstacle_bas,position_obstacle_bas,obstacle_haut,position_obstacle_haut,obstacle,position_obstacle,type_obstacle):
    n=randint(1,2)   #choix aléatoire d'un type d'obstacle#
    if n==1:   #obstacle bas# 
      n=randint(0,1) #choix d"un obstacle bas parmi les deux existant#
      obstacle=obstacle_bas[n]  #affectation aux variables des caractéristiques de l'obstacle sélectionné#
      position_obstacle=position_obstacle_bas
      type_obstacle=1
    else: #obstacle haut#
      n=randint(0,1) #choix d"un obstacle haut parmi les deux existant#
      obstacle=obstacle_haut[n]  #affectation aux variables des caractéristiques de l'obstacle sélectionné#
      position_obstacle=position_obstacle_haut
      type_obstacle=2
    return(obstacle,position_obstacle,type_obstacle)

"""fonction permettant l'affichage d'un obstacle tout à droite de l'écran"""
"""prend pour paramètres le type d'obstacle et renvoie la position"""     

def spawn(position_obstacle,type_obstacle): #affichage d'un obstacle à sa position d'origine#
    if type_obstacle==1: #obstacle bas#
        y=randint(270,320)
    else: #obstacle haut#
        y=randint(220,280)
    rect=(750,y,40,40) 
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
      pixels=2 #vitesse basse#
    if score>30:
      pixels=4
    if score>80:
      pixels=5
    if score>120:
      pixels=6
    if score>180:
      pixels=7
    if score>220:
      pixels=8
    if score>280:
      pixels=9
    if score>340:
      pixels=10 
    if score>400:  #score haut#
      pixels=11 #vitesse maximale#
    return(pixels)

"""fonction vérifiant la collision avec l'obstacle et la pièce"""
"""prend comme paramètres la position de l'objet et du personnage et renvoie crash"""

def crash_test(objet,perso,crash):
    if objet.colliderect(perso):   #vérification de la collision entre le personnage et l'objet#
        crash=1 #collision#
    else:
        crash=0 #collision#
    return(crash)

"""vérification de la présence de la pièce"""
"""prend la position de la pièce et renvoie présent"""

def presence_piece(position,present):
    n=randint(1,250) #entier aléatoire permettant une apparition irrégulière des pièces#
    if position<=-20 and n==1:   #vérification de la sortie de l'écran#
        present=0 #si la pièce est sortie et que l'entier aléatoire vaut 1#
    else:
        present=1
    return(present)

"""fonction permettant l'affichage de la pièce tout à droite de l'écran"""
"""prend comme paramètres la position de la pièce et le type d'obstacle"""

def piece_spawn(position_piece,type_obstacle):
    if type_obstacle==1: #obstacle bas#
      y=randint(220,260) #affichage de la pièce en haut#
    else: #obstacle haut#
      y=randint(270,340)  #affiche de la pièce en bas#
    return pygame.Rect((780,y,15,15))

"""fonction permettant le défilement de l'obstacle"""
"""prend pour paramètres l'obstacle, sa position et la vitesse de déplacement"""

def defilement_obstacle(position_obstacle,pixels): 
  position_obstacle=position_obstacle.move(-pixels,0) #modification de l'abscisse#
  return(position_obstacle) #renvoie la nouvelle position au programme#

"""fonction de défilement de la pièce"""
"""prend pour paramètre la piece et sa position"""

def defilement_piece(position_piece): 
  position_piece=position_piece.move(-3,0) #modification de l'abscisse#
  return(position_piece) #renvoie la nouvelle position#

"""fonction de déplacement vers le haut du personnage"""
"""prend pour paramètres le personnage et sa position"""

def haut(position_perso):
  position_perso=position_perso.move(0,-5) #modification de l'ordonnée du personnage#
  return(position_perso) #renvoie la nouvelle position#

"""fonction faisant redescendre le personnage"""
"""prend pour paramètres le personnage et sa position"""

def bas(position_perso):
  position_perso=position_perso.move(0,5) #modification de l'ordonnée du personnage#
  return(position_perso) #renvoie la nouvelle position#

"""fonction déplaçant le personnage vers la droite"""
"""prend comme paramètres le personnage et sa position"""

def droite(position_perso):
  position_perso=position_perso.move(5,0) #modification de l'abscisse#
  return(position_perso) #renvoie la nouvelle position#

"""fonction déplaçant le personnage vers la gauche"""
"""prend comme paramètres le personnage et sa position"""

def gauche(position_perso):
  position_perso=position_perso.move(-5,0) #modification de l'abscisse#
  return(position_perso) #renvoie la nouvelle position#

"""fonction permettant le défilement du fond vers la droite"""
"""prend comme paramètre les positions des trois images du fond et les renvoi"""

def defilement_fond_droite(position_fond,position_fond1,position_fond2):
  position_fond=position_fond.move((5/2),0) #augmentation de 2,5 pixels de l'abscisse de l'image#
  position_fond1=position_fond1.move((5/2),0)
  position_fond2=position_fond2.move((5/2),0)
  return(position_fond,position_fond1,position_fond2) #renvoie les nouvelles positions#

"""fonction permettant le défilement du fond vers la gauche"""
"""prend comme paramètre les positions des trois images du fond et les renvoi"""

def defilement_fond_gauche(position_fond,position_fond1,position_fond2):
  position_fond=position_fond.move((-5/2),0) #diminution de 2,5 pixels de l'abscisse de l'image#
  position_fond1=position_fond1.move((-5/2),0)
  position_fond2=position_fond2.move((-5/2),0)
  return(position_fond,position_fond1,position_fond2) #renvoie les nouvelles positions#
  
    
