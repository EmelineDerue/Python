#/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pythonBoucleFonctionLineaire.py
#  
#  Ecrire un programme qui affiche la table de multiplication d'un nombre entier des 15 premiers
#  Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#  

#specifications
#parametre : 
#	aucun
#retour : 
#	a un nombre reel 
#	b un nombre reel 
def entree():
	#Les entrees du programme
	print ("table de multiplication :x15\n")
	a = float(input("Indiquez la table de multiplication voulut:"))
	return a
	
#specifications
#Calcul d'une table de multiplication
#parametre : 
#	x un nombre reel representant la valeur de l'abscisse'
#	a un nombre reel 	 
#retour
#	y un nombre reel representant la valeur de l'ordonnee'
def fonction(x,a):
	y=  a*x
	return y

#specifications
#parametre : 
#	a un nombre reel 
#	b un nombre reel 
#retour
#	aucun
def pourImpression(a):
	for x in range(0,16):
		print (str(a)+" x "+str(x)+"  "+"= "+str(fonction(x,a))+"\n")

print ("   ---> Debut du programme.\n")
coefA=entree()
pourImpression (coefA)
print ("\n   ---> Fin du programme.")
