# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:06:42 2015
Created on Thu Mar 19 09:24:29 2015

@author: Raphael
"""

#Variaveis

Lista1=["Rock", "Paper", "Scissors", "Lizard", "Spock"]

Rock=Lista1[0]
Paper=Lista1[1]
Scissors=Lista1[2]
Lizard=Lista1[3]
Spock=Lista1[4]


contador1=0
contador2=0

import random


a="Yes"
while a=="Yes":

    while contador1<3 and contador2<3:

    
        choice1=(input("What's your move?   "))
        choice2=Lista1[random.randint(0,4)]
        
        if choice1!=Rock and choice1!=Paper and choice1!=Scissors and choice1!=Lizard and choice1!=Spock:
        
            print("Choose between Rock, Paper, Scissors, Lizard and Spock. Please, write your option with a first capital letter.")
            
        
        if choice1==Rock:
            
            if choice2==Scissors:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                
            if choice2==Paper:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
                    
            if choice2==Lizard:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                             
            if choice2==Spock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
            if choice2==Rock:
                
                print("Player 2 choosed %s"%(choice2))
                
                print("Oh it's a tie!")
                
                contador1=0
                contador2=0
                
                
        if choice1==Scissors:

            if choice2==Paper:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                
            if choice2==Rock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
                    
            if choice2==Lizard:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                             
            if choice2==Spock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
            if choice2==Scissors:
                
                print("Player 2 choosed %s"%(choice2))
                
                print("Oh it's a tie!")
                
                contador1=0
                contador2=0
   
        if choice1==Paper:

            if choice2==Rock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                
            if choice2==Scissors:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
                    
            if choice2==Spock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1+=contador1
                else:
                    contador1=0
                    contador2=0
                             
            if choice2==Lizard:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
            if choice2==Paper:
                
                print("Player 2 choosed %s"%(choice2))
                
                print("Oh it's a tie!")
                
                contador1=0
                contador2=0
                
        if choice1==Lizard:

            if choice2==Spock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                
            if choice2==Scissors:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
                    
            if choice2==Paper:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                             
            if choice2==Rock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
            if choice2==Lizard:
                
                print("Player 2 choosed %s"%(choice2))
                
                print("Oh it's a tie!")
                
                contador1=0
                contador2=0
    
        if choice1==Spock:

            if choice2==Rock:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                
            if choice2==Lizard:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
                    
            if choice2==Scissors:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Congratulations! You won this round.")
                
                if contador2==0:
    
                    contador1=contador1+1
                else:
                    contador1=0
                    contador2=0
                             
            if choice2==Paper:
        
                print("Player 2 choosed %s"%(choice2))
        
                print("Oh! You lost this round.")
                
                if contador1==0:
    
                    contador2=contador2+1
                else:
                    contador1=0
                    contador2=0
            if choice2==Spock:
                
                print("Player 2 choosed %s"%(choice2))
                
                print("Oh it's a tie!")
                
                contador1=0
                contador2=0
    if contador1==3:
        print("Congratulations Player1, you won!")
    if contador2==3:
        print("Congratulations Player2, you won!")
a=input("Would you like to play again? Yes or No?"  )
if a=="Yes":
    print("Enjoy!")
elif a=="No":
    print("See you!")
else:
    print("Please, write Yes or No with the firt letter in capital form.")
    
        
        