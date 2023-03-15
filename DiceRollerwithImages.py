import random
import os

#set images or ascii art to the variables
dice1 = '''-----
|   |
| o |
|   |
----- '''

dice2 = '''-----
|o  |
|   |
|  o|
-----'''

dice3 = '''-----
|o  |
| o |
|  o|
-----'''

dice4 = '''-----
|o o|
|   |
|o o|
-----'''

dice5 = '''-----
|o o|
| o |
|o o|
-----'''

dice6 = '''-----
|o o|
|o o|
|o o|
-----'''

#function to find maximum dice roll
def maxDiceRollFunc(maxMinDiceRoll):
  start = maxMinDiceRoll[0]
  for i in range(len(maxMinDiceRoll)):
    if start < maxMinDiceRoll[i]:
      start = maxMinDiceRoll[i]
  return start

#function to find minimum dice roll
def minDiceRollFunc(maxMinDiceRoll):
  start = maxMinDiceRoll[0]
  for i in range(len(maxMinDiceRoll)):
    if start > maxMinDiceRoll[i]:
      start = maxMinDiceRoll[i]
  return start


#set variables and clear the terminal after 
numberOfDice = int(input("How many dice do you want to roll?: "))
sumOfDiceRoll = 0 #for the sum of dice rolls
maxMinDiceRoll = [] #to find the max and min of the dice rolls
os.system("clear")

#header
print("Here are your dice rolls: \n")

#prints out all of the dice images
for i in range(numberOfDice):
  diceRoll = [dice1, dice2, dice3, dice4, dice5, dice6]
  diceRollIndex = random.randrange(0,5)
  print(diceRoll[diceRollIndex])
  diceRoll = [1,2,3,4,5,6]#convert to numbers for easy calculations
  maxMinDiceRoll.append(diceRoll[diceRollIndex])
  sumOfDiceRoll += diceRoll[diceRollIndex]

#print out all of the info
print(f'\nThe highest dice roll is:  {maxDiceRollFunc(maxMinDiceRoll)}')
print(f'\nThe lowest dice roll is:  {minDiceRollFunc(maxMinDiceRoll)}')
print(f'\nThe sum of the dice rolls is:  {sumOfDiceRoll}')



    

