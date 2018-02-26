#Ray Tso
#2/18/18
#GuessingGame.py


from random import randint
attempts = 0
number = randint(1,100)
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    attempts = attempts + 1
    if guess>number:
        print('Your guess is too high')
    elif guess<number:
        print('Your guess is too low')
    else:
        break
        
print('You got it in', attempts,'attempts')

