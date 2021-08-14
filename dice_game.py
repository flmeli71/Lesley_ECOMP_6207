# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 01:26:11 2021

@author: Flora
"""



#import random module
import random

#simulate a series of n die rolls, returned as a list
def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,6))
    return dice

#calculate the average of the die rolls
def average_dice_rolls(dice_list):
    return sum(dice_list)/len(dice_list)

#determine which player obtained the higher average
def determine_winner(avg1, avg2):
    if (avg1>avg2):
        print ("Player 1, you won!")
        return 1
    elif (avg1<avg2):
        print ("Player 2, you won!")
        return 2
    else: 
        print ("It's a tie!")
        return 0

#set up a die rolling event as a function
def die_rolling_game():

    num_rolls_player1 = input("Player 1, how many times would you like to roll the die? ")
    num_rolls_player2 = input("Player 2, how many times would you like to roll the die? ")

    player1_avg = average_dice_rolls(roll_dice(int(num_rolls_player1)))
    player2_avg = average_dice_rolls(roll_dice(int(num_rolls_player2)))

    print("Player 1, your rolls' average is", player1_avg, "!")
    print("Player 2, your rolls' average is", player2_avg, "!")

    determine_winner(player1_avg, player2_avg)
    
#start the game
die_rolling_game()

#ask the users if they would like to play again
play_again = input("Would you like to play again? y/n: " )

#keep playing until the user indicates they would not like to play anymore
while (play_again == "y"):
    die_rolling_game()
    play_again = input("Would you like to play again? y/n: " )

#goodbye
print("See you next time!")
    






    