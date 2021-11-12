import random

user = input("Who is this playing: \n")


def guessing_game():
    number = random.randint(10, 30)

    while True:
        user_guess = int(input(f'Whats your guess {user}: \n'))

        if user_guess == number:
            print(f'Right ! The answer is {user_guess}')
            break
        elif user_guess < number:
            print(f'Your guess of {user_guess} is too low')
        else:
            print(f'Your guess of {user_guess} is too high!')


guessing_game()
