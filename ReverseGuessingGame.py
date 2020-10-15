#This program tries to guess a number between 1 and 100 that you have in your head!
import random #this program uses pseudo-random choices between an intelligent range to guess your number in an efficient manner
print("Think of an integer between 1 and 100.  I will attempt to guess that number with your help!")

unguessed = True #boolean that determines whether the game is active
next_guess = random.choice(range(1,101))
guess_count = 0 #sets counter to 0
max_numbers = [100] #creates a list of numbers so the program does not guess higher than a number it knows is too high
min_numbers = [1] #likewise creates a list of numbers to as to not guess lower than a number it knows is too low

try: #this is here just in case someone says to guess higher than 1 and lower than 2, ie to prevent an empty sequence IndexError
    while unguessed is True:
        correct = input("My guess is " + str(next_guess) + ".  Is this right (Y/N)?  ") #program makes its guess
        if any(character in correct.lower() for character in "yes"): #allows user to input y or yes.
            unguessed = False #keeps game going
            guess_count = guess_count + 1 #keeps track of guesses
            if guess_count == 1: #for grammatical reasons
                print("I guessed it in 1 try!")
            else:
                print("I guessed it in " + str(guess_count) + " tries!  Thank you for playing!")
        elif any(character in correct.lower() for character in "no"): #allows user to enter n or no
            guess_count = guess_count + 1
            direction = input("Oh.  Should I guess higher or lower (H/L)?  ")
            if any(character in direction.lower() for character in "low"): #allows user to input l , low or lower
                max_numbers.append(next_guess - 1) #subtract 1 because random.choice could select the same number again
                next_guess_lower = random.choice(range(max(min_numbers), min(max_numbers) + 1)) #generates random number in range, add 1 because range does not include the endpoint
                next_guess = next_guess_lower #on to the next guess
            elif any(character in direction.lower() for character in "high"): #allows user to input H , HIGH or HIGHER
                min_numbers.append(next_guess + 1)
                next_guess_higher = random.choice(range(max(min_numbers), min(max_numbers) + 1))
                next_guess = next_guess_higher
            else: #someone entered something other than a direction
                print("Please use only H/L , HIGHER/LOWER or HIGH/LOW in either upper or lowercase.")
        else: #someone entered something other than yes/no or y/n
            print("Please use only Y/N or YES/NO in either upper or lowercase.")
except IndexError: #in case someone tries cheating the CPU
    print("You lied!  Your number is " + str(max_numbers[-1]) + " or " + str(max_numbers[-1] + 1))