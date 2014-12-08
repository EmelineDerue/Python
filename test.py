#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# pythonCalculIMC.py
#
# Copyright 2014 yves Mercadier <yves.mercadier@ac-montpellier.fr>
#

def entree():
#Les entrees du programme
 print ("Votre IMC \n")
 poid = int(input("Quelle est ton poid? "))
 taille = float(input("Quelle est ta taille? "))
 return poid,taille
def metier(poid,taille):
 #le calcul
 IMC = poid/taille**2 
 return IMC
def pourImpression(IMC):
 strImpression="";""
 if IMC>16.5:
  strImpression="\nTu es en famine  :-)"
 if IMC>16.5 and IMC<18.5:
  strImpression="\nTu es maigre"
 return strImpression;
print (" ---> Debut du programme.\n")
poid,taille=entree()
IMC=metier(poid,taille)
print(pourImpression(IMC))
print ("\n ---> Fin du programme.")
