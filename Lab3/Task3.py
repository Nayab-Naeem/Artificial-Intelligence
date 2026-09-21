import random
target = random.randint(1, 9 )

while True:
    guess = int ( input("Guess the number from 1 to 9"))
    if guess == target:
        print ("Win ")
        break
    else:
        print("Lose")
        