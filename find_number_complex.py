import random

min = 1

# Ten quinsexagintillion
max = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
user_guess = 1
program_count = 0

def find_number(user_guess, min, max, count):

    count += 1
    comp_guess = random.randint(min, max)
    guesses.append(comp_guess)
    

    if count >= 995:
        return print(f"Could not find number \nNumber of Attempts: {count} \n\n")

    elif comp_guess == user_guess:
        return print(f"\nFound it in {count} tries! The number is {comp_guess}\n")

    elif comp_guess > user_guess:
        print(f"{'{:,}'.format(comp_guess)}: LOWER")
        guesses.append("LOWER\n")
        max = comp_guess
        find_number(user_guess, min, max-1, count)

    else:
        print(f"{comp_guess}: HIGHER")
        guesses.append("HIGHER\n")
        min = comp_guess
        find_number(user_guess, min+1, max, count)

while user_guess != 0:

    guesses = []
    
    if program_count >=1:
        print("\n  0: STOP \n -1: RULES \n -2: Change Range \n")

    else:
        print("\n  0: STOP \n -1: RULES \n")

    if user_guess == -2:
        min = -1
        while min <= 0:
            min = int(input("Minimum: "))
            if min <= 0:
                print("\nInvalid number! \nThe minimum number must be a whole number greater than 0")

        bad_max = True

        while bad_max == True:
            max = int(input("Maximum: "))
            bad_max = False
            if max >= min:
                bad_max = True

    user_guess = float(input(f"\nWhat number would you like the computer to find ({'{:,}'.format(min)} - {'{:,}'.format(max)}): "))
    print()
    user_guess = int(user_guess)

    count = 0

    if user_guess >= min and user_guess <= max:
        find_number(user_guess, min, max, count)

    elif user_guess == -1:
        print(f"\n\n\n\nUSER RULES: \n\n1.) Make sure the number is between {'{:,}'.format(min)} and {'{:,}'.format(max)}\n         ^These numbers can be changed by typing -2 \n2.) Only use whole numbers \n3.) Do not use commas when typing a number. \n4.) If a number is typed with a decimal, the program will ignore everything after the decimal completely \n\nWhen creating a personalized range (by typing -2 where you would guess a number) the \nminimum number must be greater than zero. The maximum number can go as high as \nyou want it to but the computer can only guess 995 times. \n\n\n\nHOW THE COMPUTER GUESSES: \n\nWhen playing this game the computer is given hints just as you would be given. When \nthe computer guesses a number it will check if it is correct. If the guess is not \ncorrect it will be told if the number is HIGHER or LOWER. It will then guess again \nusing this new paramiter. \n\n\n\n")

    else:
        if user_guess != 0:
            print("invalid input")
        else:
            print()
    
    program_count+=1
    
