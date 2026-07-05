from capitals import easy, medium, hard, very_hard, combined
from random import choice

#let the user chose difficylty level
while True:
    difficulty = input("Choose a difficulty level (easy, medium, hard, very hard) (type 'q' to quit): ").lower()
    if difficulty.lower() in ['easy', 'medium', 'hard', 'very hard']:
        if difficulty.lower() == 'easy':
            pass
    elif difficulty.lower() == 'q':
        break
    else:
        print('thats not a valid difficulty')
        again = input("wanna play again ? ('y' for yes and 'n' for no)")
        if again == 'y':
            continue
        else:
            break