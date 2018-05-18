import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
import os

"""fonction permettant l'affichage d'un menu de sélection de la musique"""
"""renvoie à la fonction principake les valeurs de jeu, jouer et musique"""

def menuson(jeu,jouer,musique):

    pygame.font.init()

    fenetre=pygame.display.set_mode((800,600)) #on initialise la fenêtre

    rouge=(200,0,0) #RGB de la couleur rouge voulue#
    gris=(200,200,200)
    couleur=[rouge,rouge,rouge,rouge] #liste stockant les couleurs des sous-titres#

    font=pygame.font.Font("arcade.ttf", 150, bold= False, italic= False) #on définit la première police
    titre=font.render("Son",0,(200,0,0)) #on applique la première police au titre

    font1S=pygame.font.Font("Bungee-Regular.ttf", 40, bold=False, italic=False) #2eme police#   

    soustitresS=["Off","Relaxant","Joyeux","Retour au menu principal"]  #liste contenant les textes des sous-titres#

    m=-1 #pas de sous-titre sélectionné#
    son= True #pour la boucle while#

    while son: #tant que son vaut True#
 
        pygame.display.flip() #rafraichissement de l'écran à chaque entrée dans la boucle#

        soustitre1S=font1S.render("Off",0,couleur[0]) #affectation des couleurs aux sous-titres# 
        soustitre2S=font1S.render("Relaxant",0,couleur[1])
        soustitre3S=font1S.render("Joyeux",0,couleur[2])
        soustitre4S=font1S.render("Retour au menu principal",0,couleur[3])

        fenetre.blit(titre,(330,100)) #affichage du titre#
        fenetre.blit(soustitre1S,(150,260)) #affichage des sous-titres#
        fenetre.blit(soustitre2S,(150,300))
        fenetre.blit(soustitre3S,(150,340))
        fenetre.blit(soustitre4S,(150,380))

        for event in pygame.event.get(): #récupération des évènements#
            if event.type==pygame.QUIT: #quitter#
                son= False #sortir de la boucle du menu son#
                jouer=0 #sortir de la boucle principale#

            elif event.type== pygame.KEYDOWN: #touche pressée#
                if event.key==pygame.K_DOWN: #flèche du bas#

                    m=m+1 #sous-titre suivant sélectionné#
                    if m>3: #dernier sous-titre sélectionné#
                        m=m-1 #impossible de descendre et d'augmenter m#
                    else:
                        couleur[m]=gris #mettre la couleur du sous-titre sélectionné en gris#

                        if m>0: #si un autre sous-titre que le premier est sélectionné il faut remettre celui du dessus en rouge en descendant#
                            couleur[m-1]=rouge #couleur du sous-titre de dessus en rouge#

                if event.key==pygame.K_UP: #flèche du haut#
                    m=m-1 #sous-titre de dessus sélectionné#
                    if m<0: #si le premier sous-titre est sélectionné#
                        m=m+1 #impossible de monter et de diminuer m#
                    else: 
                        couleur[m]=gris #mettre la couleur du sous-titre sélectionné en gris#
                        if m>0: #si un autre sous-titre que le dernier est sélectionné il faut remettre celui du dessous en rouge en montant#
                            couleur[m+1]=rouge #couleur du sous-titre du dessous en rouge#

                elif m==0 and event.key==pygame.K_RETURN: #off sélectionné et entrer#
                    musique="off" #musique sélectionnée#
                    son=False #sortir de la boucle du menu son#
                    jeu=0 #pas de jeu sélectionné# 
                elif m==1 and event.key==pygame.K_RETURN: #relaxant sélectionné et entrer#
                    musique="relaxant" #musique sélectionnée#
                    son=False #sortir de la boucle du menu son#
                    jeu=0 #pas de jeu sélectionné# 
                elif m==2 and event.key==pygame.K_RETURN: #joyeux sélectionné et entrer#
                    musique="joyeux" #musique sélectionnée#
                    son=False #sortir de la boucle du menu son#
                    jeu=0 #pas de jeu sélectionné# 
                if m==3 and event.key==pygame.K_RETURN: #retour au menu principal sélectionné et entrer#
                    son=False #sortir de la boucle du menu son#
                    jeu=0 #pas de jeu sélectionné# 

    return(jeu,jouer,musique) #renvoie les variables à la fonction principale#
