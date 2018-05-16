import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time

"""fonction permettant l'affichage d'un menu"""
"""permet de quitter, afficher le record et de lancer un jeu"""
"""renvoie à la fonction principale les valeurs de jeu et jouer"""

def menu(jeu,jouer):

    pygame.mixer.init()

    fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de dimensions 800*600#

    fond1=pygame.image.load ("image/vague 1.jpg")   #chargement du premier fond#
    fond1=pygame.transform.scale(fond1,(800,600)) #adaptation de la taille du fond à la fenêtre#

    fond2=pygame.image.load ("image/vague 2.jpg") #chargement du deuxième fond#
    fond2=pygame.transform.scale(fond2,(800,600))

    fond3=pygame.image.load ("image/vague 3.jpg") #chargement du deuxième fond#
    fond3=pygame.transform.scale(fond3,(800,600))

    fonds=[fond1,fond2,fond3]

    rouge=(200,0,0) #RGB pour la couleur rouge voulue#
    vert=(0,200,0) #RGB pour la couleur verte voulue#
    bleu=(51,51,255)
    bleucyan=(51,102,255)

    font=pygame.font.Font("arcade.ttf", 75, bold= True, italic= False) #caractéristiques d'un objet de type font#
    font1=pygame.font.Font("Bungee-Regular.ttf", 28, bold= False, italic= True) #caractéristiques d'un objet de type font#
    titre=font.render("Pocket Monster Runner",0,rouge) #titre possédant les caractéristiques de font#
    message = font1.render("Appuyez sur une touche du clavier",0,vert)

    soustitres=["Record","Son","Notice","Quitter"] #liste contenant les sous titres#

    vague=pygame.mixer.Sound("vague.wav")
    pygame.mixer.Channel(0).play(vague,-1)

    couleur_gauche=[rouge,rouge,rouge,rouge]
    couleur_rg=rouge
    couleur_rd=rouge
    couleur_mode1=rouge
    couleur_mode2=rouge
    couleurs=[vert,bleu] #liste de couleurs

    r_gauche=0 #rectangle gauche non sélectionné#
    r_droite=0 #rectangle droit non sélectionné#
    k=-1 #rang du sous titre de la liste affiché#
    menu = True #pour la boucle while#
    jeu=0 #pas de jeu sélectionné#
    intervalle=0
    numero_fond=0
    horloge = int(time.clock())
    var=0

    while menu: #boucle faisant tourner le menu#

        if horloge < 4:
            for i in range (1, 8):
                message = font1.render("Appuyez sur une flèche du clavier",0,couleurs[var])
                fenetre.blit(message,(145,225))
                pygame.display.flip()
                if var==0:
                    var=var+1
                elif var==1:
                    var=var-1
            horloge = int(time.clock())

        if intervalle==90: #si l'intervalle atteint 200 on change le fond#
            intervalle=0  #réinitialisation#
            if numero_fond==2:
                numero_fond=0  #retour au premier fond#
            else:
                numero_fond=numero_fond+1 #fond suivant#
        else:
            intervalle=intervalle+1 #incrémentation#

        fenetre.blit(fonds[numero_fond],(0,0))

        soustitre1=font1.render("Record",0,couleur_gauche[0])  #texte "record" possédant les caractéristiques de font1#
        soustitre2=font1.render("Son",0,couleur_gauche[1])  #texte "quitter" possédant les caractéristiques de font1#
        soustitre3=font1.render("Notice",0,couleur_gauche[2])
        soustitre4=font1.render("Quitter",0,couleur_gauche[3])

        mode1= font1.render("Normal",0,couleur_mode1)
        mode2=font1.render("Hardcore",0,couleur_mode2)

        fenetre.blit(titre,(25,50)) #affichage du titre#
        fenetre.blit(soustitre1,(150,420)) #affichage des sous titres#
        fenetre.blit(soustitre2,(150, 450))
        fenetre.blit(soustitre3,(150,480))
        fenetre.blit(soustitre4,(150,510))
        fenetre.blit(mode1,(200,300))
        fenetre.blit(mode2,(550,300))

        rectangle1=pygame.draw.rect(fenetre,couleur_rg,(145,275,300,75),5) #affichage d'un rectangle à gauche en rouge#
        rectangle2=pygame.draw.rect(fenetre,couleur_rd,(495,275,300,75),5) #affichage d'un rectangle à droite en rouge#

        pygame.display.flip() #rafraichissement de l'écran à chaque boucle#        

        for event in pygame.event.get(): #récupération des évènements#

          if event.type == pygame.QUIT: #quitter#
            jouer=0 #quitter la boucle principale#
            menu=0

          elif event.type== pygame.KEYDOWN: #touche pressée#

            if event.key == pygame.K_LEFT: #flèche gauche#

                couleur_gauche=[rouge,rouge,rouge,rouge]
                couleur_rd=rouge
                couleur_rg=bleucyan
                couleur_mode1=bleucyan
                couleur_mode2=rouge
                r_gauche=1 #le rectangle gauche est sélectionné#
                r_droite=0 #le rectangle droit n'est pas sélectionné#    
                k=-1      

            if event.key == pygame.K_RIGHT: #flèche droite#
                couleur_gauche=[rouge,rouge,rouge,rouge]
                couleur_rd=bleucyan
                couleur_rg=rouge
                couleur_mode1=rouge
                couleur_mode2=bleucyan
                fenetre.blit(mode1,(200,300))
                fenetre.blit(mode2,(550,300))
                r_gauche=0 #rectangle gauche non sélectionné#
                r_droite=1 #rectangle droit sélectionné#
                k=-1

            if event.key==pygame.K_DOWN:
                couleur_rd=rouge
                couleur_rg=rouge
                couleur_mode1=rouge
                couleur_mode2=rouge

                k=k+1 #sous titre suivant sélectionné#

                if k>3: #si le dernier sous titre est déjà sélectionné#
                    k=k-1 #pas possible d'augmenter k et de descendre#

                else: #si le dernier sous titre n'est pas celui sélectionné#
                    couleur_gauche[k]=bleucyan

                    if k>0: #si on selectionne un sous titre autre que le premier il faut remettre celui du dessus en rouge#
                      couleur_gauche[k-1]=rouge

            if event.key==pygame.K_UP:

                k=k-1 #sous titre précédent sélectionné#

                if k<0: #si le premier sous titre est sélectionné#
                    k=k+1 #impossible de diminuer k et de monter#

                else: #si le premier n'est pas sélectionné#
                  couleur_gauche[k]=bleucyan

                  if k<3: #si on sélectionne un sous titre autre que le dernier il faut mettre celui du dessous en rouge#
                    couleur_gauche[k+1]=rouge

            if event.key==pygame.K_RETURN and r_gauche==1: #rectangle gauche sélectionné et flèche du bas#
                jeu=1 #le jeu choisi est le jeu 1#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and r_droite==1: #rectangle droit sélectionné et flèche du bas#
                jeu=2 #le jeu choisi est le jeu 2#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and k==0: #rectangle gauche sélectionné, le joueur appuie sur entrée et record est sélectionné#
                jeu="Record" #pas de jeu sélectionné, il faut lancer record#
                menu=False #quitte la boucle du menu#

            if event.key==pygame.K_RETURN and k==1:
            	jeu="Son"
            	menu=False

            if event.key==pygame.K_RETURN and k==2:
                menu = False #quitte la boucle du menu#
                jeu="Notice" #pas de jeu sélectionné, il faut lancer la notice#

            if event.key==pygame.K_RETURN and k==3: #rectangle gauche sélectionné, le joueur appuie sur entrée et quitter est sélectionné#
                jeu=0 #pas de jeu sélectionné#
                jouer=0 #quitter la boucle principale#
                menu=False #quitte la boucle du menu#
                
    pygame.mixer.Channel(0).stop()
    return(jeu,jouer) #renvoie à la fonction principale les variables#
