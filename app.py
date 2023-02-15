#importations
import easygui
import random

#first window
mc='minecraft'
msg = "Minecraft Mais"
title="/Minecraft Mais/"
choices = ["Generer"]
reply = easygui.buttonbox(msg, title , choices)
#2nd window
if reply == "Generer":

    #definition des listes
    a=["poser un bloc ","sauter ","dormir ","aller a droite ","aller a gauche "]
    b=["suprime un item de l'inventaire","divise tous les stacks d'items par 2","provoque la mort","me tp a 1000 blocks haut"]

    #calculs des minecraft mais
    c=random.randint(1,len(a)-1)
    d=random.randint(1,len(b)-1)
        
    #affichage du resultat #LESPROBLEMES
    text="Minecraft Mais: ", a[c] , b[d] ,"."
    title="minecraft_mais" 
    easygui.textbox("Générateur",title,text)
