import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
from menu import*
from jeu1 import*

"""fonction permettant l'affichage du menu de pause"""
"""prend comme arguments le jeu en cours et le score actuel"""
"""renvoie continuer, jouer et le temps passé dans le menu"""

def menupause(continuer,jouer,jeu,points,delai):

  debut=time.clock() #début de la mesure du temps passé dans le menu#

  """ouverture et lecture du fichier contenant le record"""

  if jeu==1: #le jeu est le 1#
    fichier="score1.txt" #sélection du fichier contenant le record du jeu 1#
  else: #le jeu est le 2#
    fichier="score2.txt" #sélection du fichier contenant le record du jeu 2#
    
  classement=open(fichier,"r") #ouverture du fichier#
  classement.seek(0) #place le curseur au début du fichier#
  meilleur_score=classement.readline() #lit le fichier#
  classement.close() #ferme le fichier#

  blanc=(200,200,200) #RGB de la couleur blanche voulue#
  rouge=(200,0,0) #RGB de la couleur rouge voulue#
  couleur=[blanc,blanc,blanc]
  
  fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de taille 800*600#
  font= pygame.font.Font("Arcade.ttf",85, bold=True, italic=False) #caractéristiques des objets de type font#
  titre=font.render("Game Paused",0,blanc) #titre possédant les caractéristiques de font#

  font1=pygame.font.Font("Bungee-Regular.ttf",30, bold=False, italic=False) #caractéristiques des objets de type font1#
  font2=pygame.font.Font("Bungee-Regular.ttf",30, bold=False, italic=True) #caractéristiques des objets de type font2#

  soustitres=["Reprendre","Menu","Quitter"] #création d'une liste contenant le texte des sous titres#
  
  score=font2.render(("Score :"),0,rouge) #affectation au texte "score" des caractéristiques de font2 et de la couleur rouge#
  score_actuel=font2.render(str(points),0,rouge) #affectation au score actuel des caractéristiques de font2 et de la couleur rouge#
  record=font2.render("Record :",0,rouge) #affectation au texte "record" des caractéristiques de font2 et de la couleur rouge#
  record_valeur=font2.render(meilleur_score,0,rouge) #affectation au record des caractéristiques de font2 et de la couleur rouge#

  pause = True #pour la boucle du menu#
  l=-1 #rang du sous titre de la liste actuellement affiché#
  delai=0 #temps passé dans le menu de pause#

  while pause:

        soustitre1=font1.render(soustitres[0],0,couleur[0]) #affectation aux sous titres des caractéristiques de font1 et la couleur#
        soustitre2=font1.render(soustitres[1],0,couleur[1])
        soustitre3=font1.render(soustitres[2],0,couleur[2])
        fenetre.blit(titre,(250,150)) #affichage du titre#
        fenetre.blit(soustitre1,(350,260)) #affichage des sous titres#
        fenetre.blit(soustitre2,(350,295))
        fenetre.blit(soustitre3,(350,330))
        fenetre.blit(score,(30,30)) #affichage de "score"#
        fenetre.blit(score_actuel,(180,30)) #affichage de la valeur du score#
        fenetre.blit(record,(30,65)) #affichage de "record"#
        fenetre.blit(record_valeur,(190,65)) #affichage de la valeur du record#

        pygame.display.flip() #rafraichissiment de l'écran à chaque tour de la boucle# 

        for event in pygame.event.get(): #évènements#

            if event.type == QUIT: #quitter#
                jouer=0 #quitter la boucle principale#
                continuer=0 #quitter la boucle du jeu#
                return(continuer,jouer,jeu,delai) #renvoie les variables à la fonction jeu#

            elif event.type== pygame.KEYDOWN: #touche pressée#

                if event.key==pygame.K_DOWN: #flèche du bas#

                    l=l+1 #sous titre suivant sélectionné#

                    if l>2: #si le sous titre sélectionné est le dernier#
                        l=l-1 #impossible d'augmenter l et de descendre#

                    else: #si le sous titre sélectionné n'est pas le dernier#
                        couleur[l]=rouge
                  
                        if l>0: #si on sélectionne un sous titre autre que le premier il faut remettre celui du dessus en blanc#
                            couleur[l-1]=blanc

                if event.key==pygame.K_UP: #flèche du haut#

                    l=l-1 #sous titre précédent sélectionné#

                    if l<0: #si le sous titre sélectionné est le premier#
                        l=l+1 #impossible de diminuer l et de monter#

                    else: #si le sous titre sélectionné n'est pas le premier#
                        couleur[l]=rouge

                        if l<2: #si on sélectionne un sous titre autre que le dernier il faut remettre celui du dessous en blanc#
                            couleur[l+1]=blanc

                if event.key==pygame.K_RETURN and l==0: #si le joueur appuie sur entrée et que continuer est sélectionné#
                    fin=time.clock() #fin de la mesure du temps passé dans le menu#
                    delai=fin-debut #calcul du temps passé dans le menu#
                    return(continuer,jouer,jeu,delai) #renvoie des variables au jeu qui continue#
                  
                if event.key==pygame.K_RETURN and l==1:  #si le joueur appuie sur entrée et que menu est sélectionné#
                    continuer=0 #quiter la boucle du jeu en cours#
                    jeu=0 #pas de jeu sélectionné#
                    return(continuer,jouer,jeu,delai) #renvoie les variables à la fonction de jeu#                    
                  
                if event.key==pygame.K_RETURN and l==2:  #si le joueur appuie sur entrée et que quitter est sélectionné#
                    jouer=0 #quitter la boucle principale#
                    continuer=0 #quitter la boucle du jeu en cours#
                    return(continuer,jouer,jeu,delai) #renvoie les variables à la fonction jeu# 
