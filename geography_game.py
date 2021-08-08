# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 17:31:16 2021

@author: Flora
"""


# text-based geography game

#initial greetins and introduction to the game
print("Hello, welcome to the Balkans!")
print("There are multiple countries to visit in this peninsula. " \
      "Here, we will play a game to get to Greece and learn some geography along the way!")
print("Let's get traveling!") 

#ask the user which direction to move, starting from Croatia
start = "Croatia"
print("Your plane landed in " + start + ". It's beautiful here, but we are trying to get to Greece.")
direction = input("Would you want to travel north or south of " + start +"? ")

#only accept north or south as valid directions. Keep prompting the user for a valid direction
allowed_directions_from_Croatia = ["north", "south"]
while direction not in allowed_directions_from_Croatia:
    direction = input("Please enter either south or north: ")
 
#first checkpoint, the correct direction to go is south    
if direction == "south":
   allowed_directions_from_Montenegro = ["south", "west"] #potential directions from Montenegro
   direction = input("You are in Montenegro now! Would you like to travel south or west? ")
   while direction not in allowed_directions_from_Montenegro:
    direction = input("Please enter either south or west: ") #keep asking for valid directions from Montenegro
    #second checkpoint, the correct direction to go is south
    if direction == "south":
       allowed_directions_from_Albania = ["south", "east"] #potential directions from Albania
       direction = input("You made it to Albania now! Where do we go from here, south or east? ")
       while direction not in allowed_directions_from_Albania:
           direction = input("Please enter either south or east: ") #keep asking for valid directions from Albania
       #third checkpoint, the correct direction is to go south
       if direction == "south":
           print("You made it to Greece! Enjoy your stay!") #if the user gets here, they win the game
       else:
           print("You were close, but you ended up in North Macedonia! Try the game again!") #matches the third if statement
   else:
       print("Uh oh! You are in the Mediterranean sea now! Try the game again!") #matches the second if statement
else:
    print("Oops, you might want to go the other way. Try the game again!") #matches the first if statement
        
        
        




