from capitals import easy, medium, hard, very_hard, combined
from random import choice

#let the user chose difficylty level
while True:
    difficulty = input("Choose a difficulty level (easy, medium, hard, very hard) (type 'q' to quit): ").lower()
    
    if difficulty.lower() in ['easy', 'medium', 'hard', 'very hard']:
        if difficulty.lower() == 'easy':
            country = choice(list(easy.keys()))
            capital = input(f"whats the capital of '{country}' ")
            
            if capital == easy[country]:
                print('correct !')
            else:
                print(f'wrong, the capital of {country} is {easy[country]}')

        elif difficulty.lower() == 'medium':
            country = choice(list(medium.keys()))
            capital = input(f"whats the capital of '{country}' ")
            if capital.lower() == medium[country].lower() :
                print('correct !')
            else:
                print(f'wrong, the capital of {country} is {medium[country]}')

        elif difficulty.lower() == 'hard':
            country = choice(list(hard.keys()))
            capital = input(f"whats the capital of '{country}' ")
            if capital.lower() == hard[country].lower() :
                print('correct !')
            else:
                print(f'wrong, the capital of {country} is {hard[country]}')

        elif difficulty.lower() == 'very hard':
            country = choice(list(very_hard.keys()))
            capital = input(f"whats the capital of '{country}' ")
            if capital.lower() == very_hard[country].lower() :
                print('correct !')
            else:
                print(f'wrong, the capital of {country} is {very_hard[country]}')

        else:
            print('that difficulty level is invalid')
            break

        again = input("wanna play again ? ('y' for yes and 'n' for no)")
        if again == 'y':
            continue
        else:
            break
    elif difficulty.lower() == 'q':
        break
    else:
        print('thats not a valid difficulty')
        again = input("wanna play again ? ('y' for yes and 'n' for no)")
        if again == 'y':
            continue
        else:
            break