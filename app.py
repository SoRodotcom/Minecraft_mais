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
    a=["poser un bloc","sauter","dormir","aller a droite","aller a gauche","pour chaque cube parcourue le jeu","tuer un zombie","prendre un dégat","miner un dianmant","battre le jeu","frapper un mob","mourrir","parler","regarder le ciel","toucher de l'eau","trouver uns structure en bois","marcher",]

    b=["suprime un item de l'inventaire","divise tous les stacks d'items par 2","provoque la mort","me tp a 1000 blocks haut""fait que je loot une canne a sucre","fait que je ne peut jouer qu'au clavier","donne 5 € a une association au hasard","fait disparaitre 3/4 de ton stuff","fait spawn un creeper","change mon FOV aleatoirement""fait crasher mon jeu","me rend aveugle pendant 5sec","fait spawn 100 vex au dessus de moi","me fait perdre","diminue ma taille","fait varier la gravité","m'oblige a boire de l'eau","stop la video","rajoute un mod","modifie ma coupe de cheveux""m'oblige a prendre une douche","fait apparaitre de la tnt la ou je regarde","éteint mon écran"]

    #calculs des minecraft mais
    c=random.randint(1,len(a)-1)
    d=random.randint(1,len(b)-1)
        
    #affichage du resultat #LESPROBLEMES
    text="Minecraft Mais: ", a[c]," " , b[d] ,"."
    title="minecraft_mais" 
    easygui.textbox("Résultat:",title,text)
