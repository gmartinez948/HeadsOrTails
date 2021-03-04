# headsortales.py

import random


print("Let's play Heads or Tails")

random_int = random.randint(0,1)

user = input("Please type 'Heads' or 'Tails': ").lower()

if user == 'heads':
    random_int
    if random_int == 0:
        print('Heads')
    else:
        print("Tails")
elif user == 'tails':
    random_int
    if random_int == 1:
        print('Tails')
    else:
        print('Heads')
else:
    print("Please input 'Heads' or 'Tails'")






