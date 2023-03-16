import random
import os
from time import sleep 

computerNumber = random.randrange(1,100)


while True:
  os.system("clear")
  userGuess = input("I have a number between 1 and 100, try to guess it: ")
  try:
    userGuess = int(userGuess)
  except ValueError:
    os.system("clear")
    print("Input not accepted, only integers please")
    sleep(2)
    continue
  userGuess = int(userGuess)
  if userGuess == computerNumber:
    os.system("clear")
    print("You are correct! Good Job!")
    sleep(2)
    os.system("clear")
    answer = input("Do you want to play again (Y/N): ")
    if answer == "Y":
      continue
    else:
      os.system("clear")
      print("Thank you for playing!")
      break
  elif userGuess < 0 or userGuess > 100:
    os.system("clear")
    print("Guess has to be between 0 and 100, please guess again!")
    sleep(2)
    continue
  elif userGuess<computerNumber:
    os.system("clear")
    print("Number to low, guess again!")
    sleep(2)
    continue
  elif userGuess>computerNumber:
    os.system("clear")
    print("Number to high, guess again!")
    sleep(2)
  else:
    print("Wrong input")
    continue
  

