"""crée le 14/04/18 en Python 3.2"""

import pygame #chargement des bibliothèques#
from pygame.locals import*
import random
from random import randint
import time
from fonctions_jeu import* #chargement des fonctions#
from menu import*
from menupause import*
from menuperdu import*

"""fonction de jeu prenant pour paramètres jouer, jeu et score"""

def jeu1(jouer,jeu,score,musique):

  """Chargement de la fenêtre, du fond et des images"""
  pygame.mixer.pre_init(44100,-16,2, 1024) 
  fenetre=pygame.display.set_mode((800,600)) #ouverture d'une fenêtre de 800*600#

  fond=pygame.image.load ("fond3.jpg")   #chargement du premier fond#
  fond=pygame.transform.scale(fond,(800,600)) #adaptation de la taille du fond à la fenêtre#

  fond1=pygame.image.load ("fond2.jpg") #chargement du deuxième fond#
  fond1=pygame.transform.scale(fond1,(800,600))

  fond2=pygame.image.load ("fond1.jpg") #chargement du troisième fond#
  fond2=pygame.transform.scale(fond2,(800,600))

  position_fond=pygame.Rect(395,0,800,600) #coordonnées des fonds stockées dans des rectangles#
  position_fond1=pygame.Rect(-200,0,800,600)
  position_fond2=pygame.Rect(-629,0,800,600)

  fonds=[fond,fond1,fond2] #création d'une liste contenant les fonds#

  obstacle_bas1=pygame.image.load("Tortank.png") #chargement du premier obstacle bas#
  obstacle_bas1=pygame.transform.scale(obstacle_bas1,(80,80)) #modification de sa taille#

  obstacle_bas2=pygame.image.load("Raichu.png") #chargement du deuxième obstacle bas#
  obstacle_bas2=pygame.transform.scale(obstacle_bas2,(80,80))

  obstacle_bas=[obstacle_bas1,obstacle_bas2] #création d'une liste contenant les obstacles bas#
  position_obstacle_bas=pygame.Rect(730,320,40,40) #création d'un rectangle contenant les coordonnées de l'obstacle bas#
 
  obstacle_haut1=pygame.image.load("Dracaufeu.png")  #chargement du premier obstacle haut#
  obstacle_haut1=pygame.transform.scale(obstacle_haut1,(80,80)) #création d'un rectangle contenant les coordonnées afin de faciliter les manipulations des coordonnées#

  obstacle_haut2=pygame.image.load("Abra.png")  #chargement du deuxième obstacle haut#
  obstacle_haut2=pygame.transform.scale(obstacle_haut2,(80,80))

  obstacle_haut=[obstacle_haut1,obstacle_haut2] #création d'une liste contenant les obstacles hauts#
  position_obstacle_haut=pygame.Rect(730,250,40,40) #coordonnées de l'obstacle bas dans un rectangle#
 
  perso=pygame.image.load("perso.png")  #chargement du personnage#
  perso=pygame.transform.scale(perso,(50,50)) #modification de sa taille#
  perso.set_colorkey((255,255,255))
  position_perso=pygame.Rect(220,235,25,25) #création d'un rectangle contenant les coordonnées afin de faciliter les manipulations des coordonnées#

  perso1=pygame.image.load("perso1.png") 
  perso1=pygame.transform.scale(perso1,(50,50))
  perso1.set_colorkey((255,255,255))

  piece=pygame.image.load("Pokeball.png") #chargement de la pièce#
  piece=pygame.transform.scale(piece,(30,30)) #modification de sa taille#
  position_piece=pygame.Rect(-20,580,15,15) #création d'un rectangle contenant ses coordonnées#

  vie=pygame.image.load("vie.jpg") #chargement de la vie#
  vie=pygame.transform.scale(vie,(30,30))
  vie.set_colorkey((252,252,252))
  position_vie=pygame.Rect(10,10,30,30) #coornonnées#
  vie1=vie #deuxième vie, identique à la première#
  vies=[vie,vie1] #liste contenant les deux vies#
  position_vies=[position_vie,(position_vie[0]+40,position_vie[1])] #liste contenant les positions des vies#

  compte=pygame.font.Font("arcade.ttf", 400, bold= True, italic= False) #création d'un objet de type font pour le compte à rebours#
  font=pygame.font.Font("Bungee-Regular.ttf",30,bold=False,italic=True)

  decompte3=compte.render("3",0,(84,0,255)) #décompte (3,2,1,0) reprenant les caractéristiques de l'objet compte#
  decompte2=compte.render("2",0,(84,0,255))
  decompte1=compte.render("1",0,(84,0,255))
  decompte0=compte.render("0",0,(84,0,255))
  
  decompte=[decompte3,decompte2,decompte1,decompte0] #création d'une liste contenant les chiffres du décompte#
  
  """initialisation des variables"""

  score=0
  score_piece=0 #score ajouté par la récupération d'une pièce#
  delai=0 #temps passé à chaque fois dans le menu de pause#
  duree_pause=0 #temps total passé dans le menu de pause#

  continuer=1  #pour la boucle infinie#
  rebours=1 #permet l'activation du compte à rebours#
  crash=0    #test de collision#
  perdu=0 #indique si le joueur a perdu#
  obstacle=0 #obstacle affiché#
  position_obstacle=0 #position de l'obstacle#
  type_obstacle=0 #type d'obstacle, haut ou bas#
  present=0   #pas d'obstacle initialement#
  pixels=3  #nombre de pixels soustraits à l'abscisse de l'obstacle#
  nb_vies=2 
  
  crash1=0 #test de collision avec la pièce#
  present1=0 #pas de pièce initialement#
  
  pygame.mixer.init()#initialisation du module gérant la musique#
  
  if musique==0 or musique=="joyeux": 
    son=pygame.mixer.Sound("jeu.wav") #chargement de la musique "joyeuse"#
  elif musique=="relaxant":
    son=pygame.mixer.Sound("vague.wav") #chargement de la musique "relaxante"#

  pas=pygame.mixer.Sound("bruit pas.wav") #chargement du bruit de pas#
  collecter=pygame.mixer.Sound("coin.wav") #chargement du son de récupération d'une pièce#

  if not(musique=="off"): #si le joueur n'a pas choisi off#
    pygame.mixer.Channel(0).play(son,-1) #joue la musique en boucle#

  '''génération du premier obstacle'''

  obstacle,position_obstacle,type_obstacle=creation_obstacle(obstacle_bas,position_obstacle_bas,obstacle_haut,position_obstacle_haut,obstacle,position_obstacle,type_obstacle)


  pygame.key.set_repeat(1,30) #permet la répétition de déplacement en restant appuyé sur une touche#

  while continuer:  #boucle infinie#
  
    if rebours==1: #affichage une unique fois du compte à rebours#

      for chiffre in range(4): #boucle permettant l'affichage des 4 chiffres du compte à rebours#

        fenetre.blit(fonds[1],position_fond1) #affichage des images du fond#
        fenetre.blit(fonds[2],position_fond2)
        fenetre.blit(fonds[0],position_fond)
        fenetre.blit(decompte[chiffre],(300,100)) #affichage d'un des chiffres sur l'écran#
        fenetre.blit(perso,position_perso) #réaffichage du personnage#
        pygame.display.flip() #rafraichissement de l'écran#
        pygame.time.wait(500) #attente avant d'afficher le chiffre suivant#

      rebours=0 #permet de ne plus rentrer dans la condition et de ne plus afficher le compte à rebours#
      debut=time.clock()  #début de la mesure du temps# 

    """a chaque entrée dans la boucle, mesure du score pour pouvoir l'envoyer aux fonctions"""
    fin=time.clock()
    score=int(round(fin-debut-duree_pause))+score_piece
    affichage_score=font.render(str(score),0,(255,0,0))
    fenetre.blit(affichage_score,(700,10))

    """à chaque entrée dans la boucle, affichage des images à leur position actuelle"""

    pygame.display.flip() #rafraichissement de l'écran#
    fenetre.blit(fonds[1],position_fond1) #affichage des images du fond#
    fenetre.blit(fonds[2],position_fond2)
    fenetre.blit(fonds[0],position_fond)
    fenetre.blit(perso,position_perso) #affichage du personnage#
    fenetre.blit(obstacle,position_obstacle) #affichage de l'obstacle#
    fenetre.blit(piece,position_piece) #affichage de la pièce#
    for loop in range(nb_vies): #affichage des vies#
      fenetre.blit(vies[loop],position_vies[loop])

    '''Obstacle : présence, sélection, défilement et collision'''
    
    present=presence_obstacle(position_obstacle[0],present)  #vérification de la présence d'un obstacle#
    
    if present==0: #pas d'obstacle#
        
      obstacle,position_obstacle,type_obstacle=creation_obstacle(obstacle_bas,position_obstacle_bas,obstacle_haut,position_obstacle_haut,obstacle,position_obstacle,type_obstacle) #choix aléatoire d'un obstacle#
      position_obstacle=spawn(position_obstacle,type_obstacle) #affichage d'un obstacle à droite de l'écran#
      pixels=vitesse(pixels,score) #sélection aléatoire d'une vitesse de défilement de l'obstacle#
      present=1 #obstacle présent#
        
    elif present==1: #sinon si l'obstacle est présent#

      position_obstacle=defilement_obstacle(position_obstacle,pixels) #défilement vers la gauche#        

    crash=crash_test(position_obstacle,position_perso,crash)  #vérification de la collision#

    if crash==1: #collision#
      fenetre.fill((255,255,255)) #affichage écran blanc#
      pygame.display.flip()
      pygame.time.wait(1000) #attente#
      position_obstacle=pygame.Rect(-200,0,25,25) #retirer l'obstacle de l'écran#
      perso=perso1 #changement du personnage affiché#
      nb_vies=nb_vies-1 #vie perdue#
      if nb_vies==0:
        continuer=0  #quitter la boucle#
        perdu=1 #le joueur a perdu#      

    """pièce: présence, défilement et collision"""

    present1=presence_piece(position_piece[0],present1) #vérification de la présence de la pièce#

    if present1==0: #pas de pièce#
      position_piece=piece_spawn(position_piece,type_obstacle) #pièce à droite de l'écran#
      present1=1 #pièce présente#

    elif present1==1: #pièce présente: défilement#
      position_piece=defilement_piece(position_piece) 

    crash1=crash_test(position_piece,position_perso,crash1) #vérification de la collision avec une pièce#
    
    if crash1==1:	#collision#
      if not(musique=="off"):
        pygame.mixer.Channel(2).play(collecter,0) #son de récupération de pièce#
      position_piece[0]=-40 #retirer la pièce de l'écran#      
      score_piece=score_piece+10 #augmentation du score#

    for event in pygame.event.get(): #vérification des évènements#

      if event.type==QUIT: #évènement quitter#
        continuer=0   #sortie de la boucle jeu#
        jouer=0 #sortie de la boucle principale#   
            
      if event.type==KEYDOWN: #touche pressée#

        if event.key==K_UP and position_perso[1]>=220: #flèche du haut#
            position_perso=haut(position_perso) #mouvement vers le haut du personnage#  
            if not(musique=="off"):
                pygame.mixer.Channel(1).play(pas,0) #bruit de pas#

        if event.key==K_DOWN and position_perso[1]<338:     #flèche du bas#             
            position_perso=bas(position_perso) #déplacement vers le bas du personnage#  
            if not(musique=="off"):
                pygame.mixer.Channel(1).play(pas,0)       #bruit de pas#   
           
        if event.key==K_RIGHT and position_perso[0]<=768: #flèche de droite : déplacement#
          position_perso=droite(position_perso) #déplacement avec la fonction droite#
          position_fond,position_fond1,position_fond2=defilement_fond_gauche(position_fond,position_fond1,position_fond2) #défilement du fond vers la gauche#
          if not(musique=="off"):
              pygame.mixer.Channel(1).play(pas,0) #bruit de pas#

        if event.key==K_LEFT and position_perso[0]>=0: #flèche de gauche: déplacement#
          position_perso=gauche(position_perso) #déplacement vers la gauche#
          position_fond,position_fond1,position_fond2=defilement_fond_droite(position_fond,position_fond1,position_fond2) #défilement du fond vers la droite#
          if not(musique=="off"):
              pygame.mixer.Channel(1).play(pas,0) #bruit de pas#

        if event.key==K_ESCAPE: #échap: ouverture du menu pause#
          fin=time.clock() #temps depuis le lancement du programme#
          score=int(round(fin-debut-duree_pause))+score_piece #calcul du score#
          pygame.mixer.Channel(0).pause() #pause de la musique#
          pygame.key.set_repeat(0,0) 
          continuer,jouer,jeu,delai=menupause(continuer,jouer,jeu,score,delai) #ouverture du menu pause#
          pygame.key.set_repeat(1,20) 
          pygame.mixer.Channel(0).unpause() #remet la musique#
          duree_pause=duree_pause+delai #calcul du temps total passé en pause#

  """sortie de la boucle while"""

  if perdu==1: #le joueur a perdu#
    fin=time.clock() #temps depuis l'exécution du programme#
    score=int(round(fin-debut-duree_pause))+score_piece #calcul du score#
    pygame.key.set_repeat(0,0)
    pygame.mixer.Channel(0).stop() #stopper la musique#
    continuer,jouer,jeu,score=menu_perdu(continuer,jouer,jeu,score) #menu perdu#
    pygame.key.set_repeat(1,20)

  pygame.mixer.Channel(0).stop() #stopper la musique#
  pygame.key.set_repeat(0,0)
  return(jouer,jeu,score) #renvoie à la fonction principale les variables#

  
  
  
