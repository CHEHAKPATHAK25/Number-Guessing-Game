#import random

#title = "Number guessing game"
        #print(title)
#print("Number guessing game")
#chances = 0

#randomnumber = random.randint(1,5)

#number = int(input("Guess the number between 1 - 5 :-"))
#print(number)

#if randomnumber == number:
        #print("Congratulation! You have won")

#elif number > 4:
        #print("You are so close! Keep guessing until you find the correct number")

#elif number > 3:
        #print("Hint : If you add one plus one to me, you get the desired number. Now type out what am I")

#else:
        #print("Keep trying your best, that's more important being correct :)")

#while chances >5:
        #print("You lose :( Better luck next time!!")

#if not chances <5:
        #print("Oops! The number to be guessed was 5")

import random

print("Number Guessing Game")
number= random.randint(1,9)
chances=0
print("Guess a number(between 1 and 9) :")
while chances <5:
    guess = int(input("Enter your guess :-"))

if guess == number :
    print("Yay! You have won the game :)")

elif guess > number :
    print("Oopsies! You were so close. Guess a number lower than", guess)
    chances+=1

elif guess < number :
    print("Oh no! Guess a number highher than", guess, "Keep going!!")
    chances+=1

if chances > 5:
    print("You lose :( The number was ", number, "Better luck next time!")

