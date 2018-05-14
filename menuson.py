import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
import os

def menuson(jeu,jouer,musique):

    pygame.font.init()

    fenetre=pygame.display.set_mode((800,600)) #on initialise la fenêtre

    rouge=(200,0,0)
    gris=(200,200,200)
    couleur=[rouge,rouge,rouge,rouge]

    font=pygame.font.Font("arcade.ttf", 150, bold= False, italic= False) #on définit la première police
    titre=font.render("Son",0,(200,0,0)) #on applique la première police au titre

    font1S=pygame.font.Font("Bungee-Regular.ttf", 40, bold=False, italic=False) #2eme police    

    soustitresS=["Off","Relaxant","Joyeux","Retour au menu principal"]  

    m=-1
    son= True
    musique=0

    while son:
 
        pygame.display.flip()

        soustitre1S=font1S.render("Off",0,couleur[0]) #on applique la 2eme police à tous les sous titres
        soustitre2S=font1S.render("Relaxant",0,couleur[1])
        soustitre3S=font1S.render("Joyeux",0,couleur[2])
        soustitre4S=font1S.render("Retour au menu principal",0,couleur[3])

        fenetre.blit(titre,(330,100))
        fenetre.blit(soustitre1S,(150,260))
        fenetre.blit(soustitre2S,(150,300))
        fenetre.blit(soustitre3S,(150,340))
        fenetre.blit(soustitre4S,(150,380))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                son= False
                jouer=0

            elif event.type== pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:

                    m=m+1
                    if m>3:
                        m=m-1
                    else:
                        couleur[m]=gris

                        if m>0:
                            couleur[m-1]=rouge

                if event.key==pygame.K_UP:
                    m=m-1
                    if m<0:
                        m=m+1
                    else:
                        couleur[m]=gris
                        if m<3:
                            couleur[m+1]=rouge

                elif m==0 and event.key==pygame.K_RETURN:
                    musique="off"
                    son=False
                    jeu=0
                elif m==1 and event.key==pygame.K_RETURN:
                    musique="relaxant"
                    son=False
                    jeu=0
                elif m==2 and event.key==pygame.K_RETURN:
                    musique="joyeux"
                    son=False
                    jeu=0
                if m==3 and event.key==pygame.K_RETURN:
                    son=False
                    jeu=0

    return(jeu,jouer,musique)
