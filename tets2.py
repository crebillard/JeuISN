

consigne = "Veuillez appuyer sur les flèches du clavier"
k=0
consigne1 = font1.render(consigne,0,bleu)
fenetre.blit(consigne1,(200,200))

violet=(153,51,255)
rose=(255,0,153)
bleu=(51,51,255)
rouge=(255,0,0)

for lettre in consigne:
    print(consigne[k])
    k=k+1
