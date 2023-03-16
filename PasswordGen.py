import random
import string
import os

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numbers = list(string.digits)
punct = list(string.punctuation)

while True:
  passLengthInput = input("How many characters do you want in password: ")
  try:
    passLength = int(passLengthInput)
    break
  except ValueError:
    os.system("clear")
    print("Please enter a number")
    continue

os.system("clear")
    
random.shuffle(lower)
random.shuffle(upper)
random.shuffle(numbers)
random.shuffle(punct)

part1 = round(passLength * (30/100))
part2 = round(passLength * (20/100))

password = []

for x in range(part1):
  password.append(lower[x])
  password.append(upper[x])

for x in range(part2):
  password.append(numbers[x])
  password.append(punct[x])

random.shuffle(password)

result = len(password)

print("Your strong password is: ", end="")
for i in range(result):
  print(password[i], end="")
