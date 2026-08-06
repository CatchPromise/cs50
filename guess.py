import random

def welcome():
    print("Welcome to guess the number")

def generate_number():
    return random.randint(1, 100)

def get_guess():
    return int(input("Guess a number between 1 and 100: "))

def check_guess(guess, number):
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High")
          

def main():
    welcome()
    number = generate_number()
    guess = get_guess()
    while guess != number:
        check_guess(guess, number)
        guess = get_guess()
    print("Bravo")

if __name__ == "__main__":
    main()