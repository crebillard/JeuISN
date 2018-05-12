"""crée le 2/05/18 avec Python 3.2"""

import pygame #importation des bibliothèques#
from pygame.locals import*
from menu import* #importation de la fonction menu#

"""fonction permettant la lecture et l'affichage du meilleur score"""
"""renvoie jeu et jouer à la fonction principale"""

def score1(jeu,jouer):

  pygame.init()
  pygame.font.init()
  continuer= True #pour la boucle infinie#

  fichier=open("score1.txt","r") #ouverture du fichier#
  fichier.seek(0) #place le curseur au début du fichier#
  record=fichier.readline() #lit le fichier#
  fichier.close() #ferme le fichier#

  font=pygame.font.SysFont("police.ttf", 100, bold= True, italic= False) #caractéristiques des objets de type font#
  font1=pygame.font.SysFont("police.ttf", 50, bold= True, italic= False)
  font2=pygame.font.SysFont("police.ttf",30,bold=False,italic=True)
  titre=font.render("Meilleur Score",0,(200,0,0)) #titre#
  meilleur_score=font.render(record,0,(200,0,0)) #score#
  retour=font1.render("Retour",0,(0,200,0)) #retour au menu#
  echap=font2.render("(Appuyez sur ECHAP pour retourner au menu)",0,(175,166,139))

  fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre 800*600#
  menucolor=(51,51,51) #couleur du fond#
  
  while continuer:

    fenetre.fill(menucolor) #remplissage du fond#
    fenetre.blit(titre,(140,100)) #affichage du titre
    fenetre.blit(meilleur_score,(300,350)) #affichage du record#
    fenetre.blit(retour,(20,550)) #affichage de retour#
    fenetre.blit(echap,(150,560))
    pygame.display.flip() #rafraichissement#

    for event in pygame.event.get(): #évènements#
      if event.type == pygame.QUIT: #quitter#
        continuer=False 
        jeu=0
        jouer=0 #quitter le jeu#

      if event.type== pygame.KEYDOWN: #touche pressée#
        if event.key==pygame.K_ESCAPE: #echap#
          continuer=False #sortie de la boucle#  
          jeu=0

  return(jeu,jouer) #retour au menu#