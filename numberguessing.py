import random 

print ("hi welcome to the game , this is a number guessing game.\nyou got 7 chances to guess the number. lets start the game")

number_to_guess = random.randrange(100)

chances = 7 

guess_counter = 0 

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input('please enter your guess: '))

    if my_guess == number_to_guess:
         print(f'the number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
         break
    elif guess_counter >= chances and my_guess != number_to_guess:
          print(f'Oops sorry, the number is {number_to_guess} better luck next time')
    elif my_guess > number_to_guess:
         print('your guess is higher')
    elif my_guess < number_to_guess:
         print('your guess is lesser')