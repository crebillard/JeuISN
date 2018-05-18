import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
from menu import*

"""fonction permettant l'affichage du menu perdu"""
"""prend comme paramètres le jeu en cours et le score"""
"""renvoie continuer, jeu et jouer"""

def menu_perdu(continuer,jouer,jeu,points):

  fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de taille 800*600#
  pygame.font.init()

  """ouverture et lecture du fichier contenant le record"""

  if jeu==1: #le jeu est le 1#
    fichier="score1.txt" #le fichier est celui du score du jeu 1#
  else: #le jeu est le 2#
    fichier="score2.txt" #le fichier est celui du score du jeu 2#
    
  classement=open(fichier,"r") #ouverture en lecture simple du fichier#
  classement.seek(0) #positionne le curseur au début du fichier#
  meilleur_score=classement.readline() #lecture du fichier#
  classement.close() #fermeture du fichier#
  
  nouveau_record=0
  if int(meilleur_score)<points: #si le joueur a battu le meilleur score#
    classement=open(fichier,"w") #ouverture du fichier en mode écriture#
    classement.write(str(points)) #remplacement du meilleur score#
    classement.close() #fermeture du fichier#  
    nouveau_record=1

  blanc=(200,200,200) #RGB de la couleur blanche choisie#
  rouge=(200,0,0) #RGB de la couleur rouge choisie#
  jaune=(255,255,0)
  couleur=[blanc,blanc,blanc]
  clignote=[rouge,jaune]

  font= pygame.font.SysFont("arcade.ttf",85, bold=True, italic=False) #caractéristiques d'un objet de type font#
  titre= font.render("Game Over",0,blanc) #titre possédant les caractéristiques de font#
  font1=pygame.font.SysFont("Bungee-Regular.ttf",40, bold=False, italic=False) #caractéristiques d'un objet de type font1#
  font2=pygame.font.SysFont("Bungee-Regular.ttf",40, bold=False, italic=True) #caractéristiques d'un objet de type font2#

  titre= font.render("Game Over",0,blanc) #texte "Game over" possédant les caractéristiques de font et la couleur blanche#

  soustitres=["Rejouer","Menu","Quitter"] #création d'une liste contenant les textes des sous titres#

  score=font2.render("Score :",0,rouge)  #affectation au texte "score" des caractéristiques de font2 et de la couleur rouge#
  valeur_score=font2.render(str(points),0,rouge) #affectation au score actuel des caractéristiques de font2 et de la couleur rouge#
  record=font2.render("Record :",0,rouge) #affectation au texte "record" des caractéristiques de font2 et de la couleur rouge#
  valeur_record=font2.render(meilleur_score,0,rouge) #affectation au record des caractéristiques de font2 et de la couleur rouge#

  j=-1 #rang du sous titre sélectionné#
  rang_couleur=0
  perdre = True #pour la bouche while faisant tourner le menu#
  debut=int(time.clock())

  while perdre:

    soustitre1=font1.render(soustitres[0],0,couleur[0]) #affectation aux sous titres de la liste des caractéristiques de font1 et de la couleur blanche#
    soustitre2=font1.render(soustitres[1],0,couleur[1])
    soustitre3=font1.render(soustitres[2],0,couleur[2])
    new=font2.render("Nouveau Record !",0,clignote[rang_couleur])

    fenetre.blit(titre,(340,150)) #affichage du titre#
    fenetre.blit(soustitre1,(350,260)) #affichage des sous titres#
    fenetre.blit(soustitre2,(350,295))
    fenetre.blit(soustitre3,(350,330))
    fenetre.blit(score,(30,30)) #affichage de "score"#
    fenetre.blit(valeur_score,(155,30)) #affichage de la valeur du score#
    fenetre.blit(record,(30,65)) #affichage de "record"#
    fenetre.blit(valeur_record,(175,65)) #affichage de la valeur du record#

    if nouveau_record==1: #nouveau record#

      fenetre.blit(new,(30,100)) #afficher le message de nouveau record#
      fin=int(time.clock()-debut) #mesure du temps#
      if fin>=0.5: #toutes les demis secondes#
        debut=int(time.clock()) 
        if rang_couleur==0: #changement de la couleur du message#
          rang_couleur=1
        else:
          rang_couleur=0

    pygame.display.flip() #rafraichissement de l'écran à chaque tour de la boucle#

    for event in pygame.event.get(): #évènements#

        if event.type == pygame.QUIT: #quitter#
            jouer=0 #quitter la boucle principale#
            continuer=0 #quitter la boucle du jeu#
            return(continuer,jouer,jeu,points)

        elif event.type== pygame.KEYDOWN: #touche pressée#

            if event.key==pygame.K_DOWN: #flèche du bas#

                j=j+1 #sélection du sous titre suivant#

                if j>2: #si le sous titre sélectionné est le dernier#
                    j=j-1 #impossible d'augmenter j et de descendre#$

                else: #si le sous titre sélectionné n'est pas le dernier#
                    couleur[j]=rouge
                    
                    if j>0: #si on selectionne un sous titre autre que le premier il faut remettre celui du dessus en blanc#
                        couleur[j-1]=blanc

            if event.key==pygame.K_UP: #flèche du haut#

                j=j-1 #sous titre précédent sélectionné#

                if j<0: #si le sous titre sélectionné est le premier#
                    j=j+1 #impossible de diminuer j et de monter#

                else: #si le sous titre sélectionné n'est pas le premier#
                  couleur[j]=rouge

                  if j<2: #si on selectionne un sous titre autre que le dernier il faut remettre celui du dessous en blanc#
                    couleur[j+1]=blanc

            if event.key==pygame.K_RETURN and j==0: #si le joueur appuie sur entrée et que rejouer est sélectionné#
                continuer=0 #sortir de la boucle du jeu#
                return(continuer,jouer,jeu,points) #renvoie les variables à la fonction jeu en cours#

            if event.key==pygame.K_RETURN and j==1: #si le joueur appuie sur entrée et que menu est sélectionné#
                continuer=0 #quitter la boucle du jeu en cours#
                jeu=0 #pas de jeu sélectionné#
                return(continuer,jouer,jeu,points) #renvoie les variables au jeu en cours#
                    
            if event.key==pygame.K_RETURN and j==2: #si le joueur appuie sur entrée et que quitter est sélectionné#
                continuer=0 #quitter la boucle du jeu en cours#
                jouer=0 #quitter la boucle principale#
                return(continuer,jouer,jeu,points) #renvoie le variables à la fonction jeu en cours#
