"""crée le 2/05/18 avec Python 3.2"""
#Ajout commentaite pour test github

import pygame #importation des bibliothèques#
from pygame.locals import*
from menu import* #importation de la fonction menu#

"""fonction permettant la lecture et l'affichage du meilleur score"""
"""renvoie jeu et jouer à la fonction principale"""

def score1(jeu,jouer):
  
  pygame.init()
  pygame.font.init()
  continuer= True #pour la boucle infinie#

  fichier1=open("score1.txt","r") #ouverture du fichier mode normal#
  fichier1.seek(0) #place le curseur au début du fichier#
  record1=fichier1.readline() #lit le fichier#
  fichier1.close() #ferme le fichier#

  fichier2=open("score2.txt","r") #ouverture du fichier mode hardcore#
  fichier2.seek(0) #place le curseur au début du fichier#
  record2=fichier2.readline() #lit le fichier#
  fichier2.close() #ferme le fichier#


  font=pygame.font.Font("Bungee-Regular.ttf", 75, bold= True, italic= False) #caractéristiques des objets de type font#
  font1=pygame.font.Font("Bungee-Regular.ttf", 20, bold= True, italic= False)
  font2=pygame.font.Font("Bungee-Regular.ttf",10,bold=False,italic=True)
  titre=font.render("Meilleurs Scores",0,(200,200,200)) #titre#
  mode1=font1.render("Mode normal :",0,(51,102,255))
  mode2=font1.render("Mode hardcore :",0,(51,102,255))
  meilleur_score1=font1.render(record1,0,(200,0,0)) #score mode normal#
  meilleur_score2=font1.render(record2,0,(200,0,0)) #score mode hardcore
  retour=font1.render("Retour",0,(51,102,255)) #retour au menu#
  echap=font2.render("(Appuyez sur ECHAP pour retourner au menu)",0,(175,166,139))

  fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre 800*600#
  menucolor=(0,0,0) #couleur du fond#

  while continuer:

    fenetre.fill(menucolor) #remplissage du fond#
    fenetre.blit(titre,(10,100)) #affichage du titre
    fenetre.blit(mode1,(100,350)) #affichage mode1
    fenetre.blit(mode2,(100,400)) #affichage mode2
    fenetre.blit(meilleur_score1,(290,350)) #affichage du record mode normal#
    fenetre.blit(meilleur_score2,(310,400)) #affichage du record mode hardcore
    fenetre.blit(retour,(20,550)) #affichage de retour#
    fenetre.blit(echap,(150,560)) #affichage d'echap
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
