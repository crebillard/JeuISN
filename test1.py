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

couleurs=[vert,bleu]
noir=(0,0,0)
var=0

font=pygame.font.Font("arcade.ttf", 102, bold= True, italic= False) #caractéristiques d'un objet de type font#
titre=font.render("Arcade Games",0,bleu) #titre possédant les caractéristiques de font#

fontbis= pygame.font.Font("arcade.ttf", 100, bold= False, italic=False)
titrebis= fontbis.render("Arcade Games",0, vert)

font1=pygame.font.Font("Bungee-Regular.ttf", 35, bold= False, italic= True) #caractéristiques d'un objet de type font#
font1bis=pygame.font.Font("Bungee-Regular.ttf",37, bold=True,italic=True)

soustitre1=font1.render("Jouer",0,bleu) #texte "jouer" possédant les caractéristiques de font1#
soustitre2=font1.render("Record",0,bleu)  #texte "record" possédant les caractéristiques de font1#
soustitre3=font1.render("Sons",0,bleu)
soustitre4=font1.render("Notice",0,bleu)
soustitre5=font1.render("Quitter",0,bleu)  #texte "quitter" possédant les caractéristiques de font1#

soustitre1bis=font1bis.render("Jouer",0,vert) #texte "jouer" possédant les caractéristiques de font1#
soustitre2bis=font1bis.render("Record",0,vert)  #texte "record" possédant les caractéristiques de font1#
soustitre3bis=font1bis.render("Sons",0,vert)
soustitre4bis=font1bis.render("Notice",0,vert)
soustitre5bis=font1bis.render("Quitter",0,vert)

message = font1.render("Appuyez sur une touche du clavier",0,vert)

soustitres=["Jouer","Record","Sons","Notice","Quitter"] #liste contenant les sous titres#

fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de dimensions 800*600#

fenetre.fill(menucolor) #remplissage du fond#
fenetre.blit(titre,(115,100)) #affichage du titre#
fenetre.blit(soustitre1bis,(75,420))
fenetre.blit(soustitre2bis,(75,450))
fenetre.blit(soustitre3bis,(75,480))
fenetre.blit(soustitre4bis,(75,510))
fenetre.blit(soustitre5bis,(75,540))
fenetre.blit(soustitre1,(75,420)) #affichage des sous titres#
fenetre.blit(soustitre2,(75, 450))
fenetre.blit(soustitre3,(75,480))
fenetre.blit(soustitre4,(75,510))
fenetre.blit(soustitre5,(75,540))
fenetre.blit(soustitre1,(425,420))
fenetre.blit(soustitre2,(425, 450))
fenetre.blit(soustitre3,(425,480))
fenetre.blit(soustitre4,(425,510))
fenetre.blit(soustitre5,(425,540))
fenetre.blit(titrebis,(115,100))
rectangle1=pygame.draw.rect(fenetre,bleu,(75,300,300,75),5) #affichage d'un rectangle à gauche en rouge#
rectangle2=pygame.draw.rect(fenetre,bleu,(425,300,300,75),5) #affichage d'un rectangle à droite en rouge#


r_gauche=0 #rectangle gauche non sélectionné#
r_droite=0 #rectangle droit non sélectionné#
k=-1 #rang du sous titre de la liste affiché#
menu = True #pour la boucle while#
jeu=0 #pas de jeu sélectionné#
p=8
horloge = int(time.clock())

while menu: #boucle faisant tourner le menu#

    pygame.display.flip() #rafraichissement de l'écran à chaque boucle#

    if horloge < 3:
        for i in range (1, p):
            message = font1.render("Appuyez sur une flèche du clavier",0,couleurs[var])
            fenetre.blit(message,(50,200))
            pygame.display.flip()
            if var==0:
                var=var+1
            elif var==1:
                var=var-1
        horloge = int(time.clock())
    else:
        fenetre.fill(menucolor) #remplissage du fond#
        fenetre.blit(titre,(115,100)) #affichage du titre#
        fenetre.blit(soustitre1bis,(75,420))
        fenetre.blit(soustitre2bis,(75,450))
        fenetre.blit(soustitre3bis,(75,480))
        fenetre.blit(soustitre4bis,(75,510))
        fenetre.blit(soustitre5bis,(75,540))
        fenetre.blit(soustitre1,(75,420)) #affichage des sous titres#
        fenetre.blit(soustitre2,(75, 450))
        fenetre.blit(soustitre3,(75,480))
        fenetre.blit(soustitre4,(75,510))
        fenetre.blit(soustitre5,(75,540))
        fenetre.blit(soustitre1,(425,420))
        fenetre.blit(soustitre2,(425, 450))
        fenetre.blit(soustitre3,(425,480))
        fenetre.blit(soustitre4,(425,510))
        fenetre.blit(soustitre5,(425,540))
        fenetre.blit(titrebis,(115,100))
        rectangle1=pygame.draw.rect(fenetre,bleu,(75,300,300,75),5) #affichage d'un rectangle à gauche en rouge#
        rectangle2=pygame.draw.rect(fenetre,bleu,(425,300,300,75),5) #affichage d'un rectangle à droite en rouge#

        pygame.display.flip()



    for event in pygame.event.get(): #récupération des évènements#

        if event.type == pygame.QUIT: #quitter#
            jouer=0 #quitter la boucle principale#
            menu=0

        elif event.type== pygame.KEYDOWN: #touche pressée#

            if event.key == pygame.K_LEFT: #flèche gauche#

                fenetre.blit(soustitre1bis,(75,420))
                fenetre.blit(soustitre2bis,(75,450))
                fenetre.blit(soustitre3bis,(75,480))
                fenetre.blit(soustitre4bis,(75,510))
                fenetre.blit(soustitre5bis,(75,540))
                fenetre.blit(soustitre1,(75,420)) #réaffichage de tous les sous titres en rouge#
                fenetre.blit(soustitre2,(75, 450))
                fenetre.blit(soustitre3,(75,480))
                fenetre.blit(soustitre4,(75,510))
                fenetre.blit(soustitre5,(75,540))
                fenetre.blit(soustitre1,(425,420))
                fenetre.blit(soustitre2,(425, 450))
                fenetre.blit(soustitre3,(425,480))
                fenetre.blit(soustitre4,(425,510))
                fenetre.blit(soustitre5,(425,540))
                fenetre.blit(titrebis,(115,100))
                rectangle1=pygame.draw.rect(fenetre,violet,(75,300,300,75),5) #affichage du rectangle gauche en vert#
                rectangle2=pygame.draw.rect(fenetre,bleu,(425,300,300,75),5) #affichage du rectangle droit en rouge#
                r_gauche=1 #le rectangle gauche est sélectionné#
                r_droite=0 #le rectangle droit n'est pas sélectionné#
                k=-1 #pas encore de sous titres selectionné#
                y=390 #ordonnée du sous titre#

            if event.key==pygame.K_DOWN and r_gauche==1: #rectangle gauche sélectionné et flèche du bas#

                k=k+1 #sous titre suivant sélectionné#

                if k>4: #si le dernier sous titre est déjà sélectionné#
                    k=k-1 #pas possible d'augmenter k et de descendre#

                else: #si le dernier sous titre n'est pas celui sélectionné#
                    y=y+30 #augmente l'ordonnée de 30 pour qu'elle corresponde avec celle du sous titre sélectionné#
                    soustitre=font1bis.render(soustitres[k],0,rouge) #modifie la couleur du sous titre sélectionné#
                    soustitrebis=font1.render(soustitres[k],0,bleu)
                    fenetre.blit(soustitre,(75,y)) #affichage du sous titre#
                    fenetre.blit(soustitrebis,(75,y))
                    rectangle1=pygame.draw.rect(fenetre,bleu,(75,300,300,75),5) #remet le rectangle gauche en rouge#

                    if k>0: #si on selectionne un sous titre autre que le premier il faut remettre celui du dessus en rouge#
                      vieux=font1bis.render(soustitres[k-1],0,vert) #modification de la couleur du sous titre précédent en rouge#
                      fenetre.blit(vieux,(75,y-30)) #affichage à la position précédente#


            if event.key==pygame.K_UP and r_gauche==1: #rectangle gauche sélectionné et flèche du haut#

                k=k-1 #sous titre précédent sélectionné#

                if k<0: #si le premier sous titre est sélectionné#
                    k=k+1 #impossible de diminuer k et de monter#

                else: #si le premier n'est pas sélectionné#
                  y=y-30 #diminue l'ordonnée de 30 pour qu'elle corresponde avec celle du sous titre sélectionné#
                  soustitre=font1.render(soustitres[k],0,violet) #modifie en vert la couleur du sous titre#
                  fenetre.blit(soustitre,(75,y)) #affichage#
                  rectangle1=pygame.draw.rect(fenetre,bleu,(75,300,300,75),5) #remet le rectangle gauche en rouge#

                  if k<4: #si on sélectionne un sous titre autre que le dernier il faut mettre celui du dessous en rouge#
                    vieux=font1.render(soustitres[k+1],0,bleu) #modifie en rouge la couleur du sous titre précédent#
                    fenetre.blit(vieux,(75,y+30)) #affichage à la position précédente#


            if event.key==pygame.K_RETURN and r_gauche==1 and k==0: #rectangle gauche sélectionné, le joueur appuie sur entrée et jouer est sélectionné#
                jeu=1 #le jeu choisi est le jeu 1#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and r_gauche==1 and k==1: #rectangle gauche sélectionné, le joueur appuie sur entrée et record est sélectionné#
                jeu="Record" #pas de jeu sélectionné, il faut lancer record#
                menu=False #quitte la boucle du menu#


            if event.key==pygame.K_RETURN and r_gauche==1 and k==2: #rectangle gauche sélectionné, le joueur appuie sur entrée et quitter est sélectionné#
                jeu=0 #pas de jeu sélectionné#
                jouer=0 #quitter la boucle principale#
                menu=False #quitte la boucle du menu#

            if event.key == pygame.K_RIGHT: #flèche droite#

                fenetre.blit(soustitre1bis,(75,420))
                fenetre.blit(soustitre2bis,(75,450))
                fenetre.blit(soustitre3bis,(75,480))
                fenetre.blit(soustitre4bis,(75,510))
                fenetre.blit(soustitre5bis,(75,540))
                fenetre.blit(soustitre1,(75,420)) #affiche l'ensemble des sous titres en rouge#
                fenetre.blit(soustitre2,(75, 450))
                fenetre.blit(soustitre3,(75,480))
                fenetre.blit(soustitre1,(425,420))
                fenetre.blit(soustitre2,(425, 450))
                fenetre.blit(soustitre3,(425,480))
                rectangle2=pygame.draw.rect(fenetre,violet,(425,300,300,75),5) #affichage du rectangle droit en vert#
                rectangle1=pygame.draw.rect(fenetre,bleu,(75,300,300,75),5) #affichage du rectangle gauche en rouge#
                r_gauche=0 #rectangle gauche non sélectionné#
                r_droite=1 #rectangle droit sélectionné#
                k=-1 #pas encore de sous titre sélectionné#
                y=390 #ordonnée des sous titres#


            if event.key==pygame.K_DOWN and r_droite==1: #rectangle droit sélectionné et flèche du bas#

                k=k+1 #sous titre suivant sélectionné#
                if k>4: #si le dernier sous titre est déjà sélectionné#
                    k=k-1 #pas possible d'augmenter k et de descendre#

                else: #si le dernier soustitre n'est pas celui sélectionné#
                  y=y+30 #augmente l'ordonnée de 30 pour qu'elle corresponde avec celle du sous titre sélectionné#
                  soustitre=font1.render(soustitres[k],0,violet) #modifie la couleur du sous titre sélectionné#
                  fenetre.blit(soustitre,(425,y)) #affichage du sous titre#
                  rectangle2=pygame.draw.rect(fenetre,bleu,(425,300,300,75),5) #remet le rectangle droit en rouge#

                  if k>0: #si on sélectionne un sous titre autre que le premier il faut remettre celui du dessus en rouge#
                    vieux=font1.render(soustitres[k-1],0,bleu) #modification de la couleur du sous titre précédent en rouge#
                    fenetre.blit(vieux,(425,y-30)) #affichage à la position précédente#


            if event.key==pygame.K_UP and r_droite==1:  #rectangle droit sélectionné et flèche du haut#

                k=k-1 #sous titre précédent sélectionné#

                if k<0:  #si le premier sous titre est sélectionné#
                    k=k+1 #impossible de diminuer k et de monter#

                else: #si le premier sous titre n'est pas sélectionné#
                  y=y-30 #diminue l'ordonnée de 30 pour qu'elle corresponde avec celle du sous titre sélectionné#
                  soustitre=font1.render(soustitres[k],0,violet) #modifie en vert la couleur du sous titre#
                  fenetre.blit(soustitre,(425,y)) #affichage#
                  rectangle2=pygame.draw.rect(fenetre,bleu,(425,300,300,75),5) #remet le rectangle droit en rouge#

                  if k<4: #si on sélectionne un sous titre autre que le dernier il faut mettre celui du dessous en rouge#
                    vieux=font1.render(soustitres[k+1],0,bleu) #modifie en rouge la couleur du sous titre précédent#
                    fenetre.blit(vieux,(425,y+30)) #affichage à la position précédente#

            if event.key==pygame.K_RETURN and r_droite==1 and k==0: #rectangle droit sélectionné, le joueur appuie sur entrée et jouer est sélectionné#
                jeu=2 #le jeu choisi est le jeu 2#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and r_droite==1 and k==2: #rectangle droit sélectionné, le joueur appuie sur entrée et quitter est sélectionné#
                jeu=0 #pas de jeu sélectionné#
                jouer=0 #pour quitter la boucle principale#
                menu=False   #quitter la boucle du menu#
