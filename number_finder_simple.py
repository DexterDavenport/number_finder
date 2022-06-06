import random

go = True

min = 1
max = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def find_num(min, max, guess, count):
    comp_guess = random.randint(min, max)
    count += 1
    if comp_guess < guess:
        print(f"{'{:,}'.format(comp_guess)}: HIGHER")
        min = comp_guess
        find_num(min, max, guess, count)
    elif comp_guess > guess:
        print(f"{'{:,}'.format(comp_guess)}: LOWER")
        max = comp_guess
        find_num(min, max, guess, count)
    elif comp_guess == guess:
        return print(f"\nComputer found it in {count} guesses! \nComputer Guess: {'{:,}'.format(comp_guess)}\nUser Number: {'{:,}'.format(guess)}\n")

while go == True:
    count = 0
    guess = int(input(f"\nNumber for computer to find between {min} and {'{:,}'.format(max)}: "))
    print()

    if guess == 0:
        go = False
    
    else:
        find_num(min, max, guess, count)

    