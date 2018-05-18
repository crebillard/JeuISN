import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
from notice import*

"""fonction permettant l'affichage d'un menu"""
"""permet de quitter, afficher le record et de lancer un jeu"""
"""renvoie à la fonction principale les valeurs de jeu et jouer"""

def menu(jeu,jouer):

    pygame.mixer.init() #initialisation du mixer#

    fenetre= pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de dimensions 800*600#

    fond1=pygame.image.load ("image/vague 1.jpg")   #chargement du premier fond#
    fond1=pygame.transform.scale(fond1,(800,600)) #adaptation de la taille du fond à la fenêtre#

    fond2=pygame.image.load ("image/vague 2.jpg") #chargement du deuxième fond#
    fond2=pygame.transform.scale(fond2,(800,600))

    fond3=pygame.image.load ("image/vague 3.jpg") #chargement du deuxième fond#
    fond3=pygame.transform.scale(fond3,(800,600))

    fonds=[fond1,fond2,fond3] #liste contenant les fonds pour l'animation de l'écran#

    rouge=(200,0,0) #RGB pour la couleur rouge voulue#
    vert=(0,200,0) #RGB pour la couleur verte voulue#
    bleu=(51,51,255)
    bleucyan=(51,102,255)

    font=pygame.font.Font("arcade.ttf", 75, bold= True, italic= False) #caractéristiques d'un objet de type font#
    font1=pygame.font.Font("Bungee-Regular.ttf", 28, bold= False, italic= True) #caractéristiques d'un objet de type font#
    titre=font.render("Pocket Monster Runner",0,rouge) #titre possédant les caractéristiques de font#
    message = font1.render("Appuyez sur une touche du clavier",0,vert) #message d'accueil de type font1 et vert#

    soustitres=["Record","Son","Notice","Quitter"] #liste contenant les sous titres#

    vague=pygame.mixer.Sound("vague.wav") #importation de la musique du menu#
    pygame.mixer.Channel(0).play(vague,-1) #le programme joue en boucle la musique#

    couleur_gauche=[rouge,rouge,rouge,rouge] #liste contenant les couleurs des sous-titres#
    couleur_rg=rouge #couleur du rectangle de gauche#
    couleur_rd=rouge #couleur du rectangle de droite#
    couleur_mode1=rouge #couleur du texte du mode 1#
    couleur_mode2=rouge #couleur du texte du mode 2#
    couleurs=[vert,bleu] #liste de couleurs pour faire clignoter le message d'accueil#

    r_gauche=0 #rectangle gauche non sélectionné#
    r_droite=0 #rectangle droit non sélectionné#
    k=-1 #rang du sous titre de la liste affiché#
    menu = True #pour la boucle while#
    jeu=0 #pas de jeu sélectionné#
    jouer=1
    intervalle=0 #permet de changer le fond affcihé au bout d'un certains temps#
    numero_fond=0 #numero du fond affiché#
    horloge = int(time.clock()) #temps écoulé depuis le lancement du programme#
    var=0 #rang de la couleur d'affichage du message d'accueil#

    while menu: #boucle faisant tourner le menu#

        """affichage d'un message clignotant en vert et bleu pendant les 4 premières secondes d'exécution du programme"""

        horloge=int(time.clock()) #nouvelle mesure du temps écoulé#

        if horloge < 4: #si le temps écoulé est inférieur à quatre secondes#
            for i in range (1, 8): 
                message = font1.render("Appuyez sur une flèche du clavier",0,couleurs[var]) #affectation d'une couleur au message d'accueil#
                fenetre.blit(message,(145,225)) #affichage du message d'accueil#
                pygame.display.flip() #rafraichissement de l'écran#
                if var==0: #couleur = vert#
                    var=var+1 #changement de la couleur du message en bleu#
                elif var==1: #couleur = bleu#
                    var=var-1 #changement de la couleur du message en vert#

        elif horloge < 8 and horloge>5:
        	for i in range (1,8):
        		message=font1.render("Appuyez sur entrer pour sélectionner",0,couleurs[var])
        		fenetre.blit(message,(144,225))
        		pygame.display.flip()
        		if var==0:
        			var=var+1
        		elif var==1:
        			var=var-1

        if intervalle==90: #si l'intervalle atteint 200 on change le fond#
            intervalle=0  #réinitialisation#
            if numero_fond==2:
                numero_fond=0  #retour au premier fond#
            else:
                numero_fond=numero_fond+1 #fond suivant#
        else:
            intervalle=intervalle+1 #incrémentation#

        fenetre.blit(fonds[numero_fond],(0,0)) #affichage du fond actuel#

        """affectation des couleurs aux textes, modes et rectangles et réaffichage"""

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
            menu=0 #quitter le menu#

          elif event.type== pygame.KEYDOWN: #touche pressée#

            if event.key == pygame.K_LEFT: #flèche gauche#

                couleur_gauche=[rouge,rouge,rouge,rouge] #remettre les sous-titres en rouge#
                couleur_rd=rouge #remettre le rectangle droit en rouge#
                couleur_rg=bleucyan #rectangle gauche sélectionné: sa couleur est bleu#
                couleur_mode1=bleucyan #mode 1 sélectionné: sa couleur est bleu#
                couleur_mode2=rouge #remettre le mode 2 en rouge#
                r_gauche=1 #le rectangle gauche est sélectionné#
                r_droite=0 #le rectangle droit n'est pas sélectionné#    
                k=-1 #rectangle sélectionné, pas de sous-titre sélectionné#

            if event.key == pygame.K_RIGHT: #flèche droite#
                couleur_gauche=[rouge,rouge,rouge,rouge] #remettre les sous-titres en rouge#
                couleur_rd=bleucyan #rectangle droit sélectionné: sa couleur est bleu#
                couleur_rg=rouge #remettre le rectangle gauche en rouge#
                couleur_mode1=rouge #remettre le mode 1 en rouge#
                couleur_mode2=bleucyan #mode 2 sélectionné: sa couleur est bleu#
                r_gauche=0 #rectangle gauche non sélectionné#
                r_droite=1 #rectangle droit sélectionné#
                k=-1 #rectangle sélectionné, pas de sous-titre sélectionné#

            if event.key==pygame.K_DOWN: #flèche du bas#
                couleur_rd=rouge #remettre le rectangle droit en rouge#
                couleur_rg=rouge #remettre le rectangle gauche en rouge#
                couleur_mode1=rouge #remettre le mode 1 en rouge#
                couleur_mode2=rouge #remettre le mode 2 en rouge#

                k=k+1 #sous titre suivant sélectionné#

                if k>3: #si le dernier sous titre est déjà sélectionné#
                    k=k-1 #pas possible d'augmenter k et de descendre#

                else: #si le dernier sous titre n'est pas celui sélectionné#
                    couleur_gauche[k]=bleucyan #mettre le couleur du sous-titre sélectionné en bleu#

                    if k>0: #si on selectionne un sous titre autre que le premier il faut remettre celui du dessus en rouge#
                      couleur_gauche[k-1]=rouge #remettre le sous-titre du dessus en rouge#

            if event.key==pygame.K_UP: #flèche du haut#

                k=k-1 #sous titre précédent sélectionné#

                if k<0: #si le premier sous titre est sélectionné#
                    k=k+1 #impossible de diminuer k et de monter#

                else: #si le premier n'est pas sélectionné#
                  couleur_gauche[k]=bleucyan #mettre le sous-titre sélectionné en bleu#

                  if k<3: #si on sélectionne un sous titre autre que le dernier il faut mettre celui du dessous en rouge#
                    couleur_gauche[k+1]=rouge #remettre le sous-titre du dessous en rouge#
 
            if event.key==pygame.K_RETURN and r_gauche==1: #rectangle gauche sélectionné et entrer#
                jeu=1 #le jeu choisi est le jeu 1#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and r_droite==1: #rectangle droit sélectionné et entrer#
                jeu=2 #le jeu choisi est le jeu 2#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and k==0: #le joueur appuie sur entrer et record est sélectionné#
                jeu="Record" #pas de jeu sélectionné, il faut lancer record#
                menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and k==1:#le joueur appuie sur entrer et son est sélectionné#
            	jeu="Son" #pas de jeu sélectionné, il faut lancer le menu de son#
            	menu=False #quitter la boucle du menu#

            if event.key==pygame.K_RETURN and k==2: #le joueur appuie sur entrer et notice est sélectionnée#
                menu = False #quitter la boucle du menu#
                jeu="Notice" #pas de jeu sélectionné, il faut lancer la notice#

            if event.key==pygame.K_RETURN and k==3: #le joueur appuie sur entrer et quitter est sélectionné#
                jeu=0 #pas de jeu sélectionné#
                jouer=0 #quitter la boucle principale#
                menu=False #quitter la boucle du menu#
                
    pygame.mixer.Channel(0).stop() #stopper la musique#
    return(jeu,jouer) #renvoie à la fonction principale les variables#
