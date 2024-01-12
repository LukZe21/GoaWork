import random
import numpy

nums = numpy.arange(1, 7)

username = input('Enter your username > ')

user_score = 0
computer_score = 0


while True:
    actual = random.choice(nums)
    user_choice = input('Enter a number > ')

    if user_choice in ['break', 'stop', 'exit']:
        break

    random.shuffle(nums)
    computer_choice = random.choice(nums)


    if user_choice == actual:
        user_score += 1
        print(f'{username} got it right!\n user_score - {user_score}\n computer_score - {computer_score}')
    elif computer_choice == actual:
        computer_score += 1
        print(f'Computer got it right!\n user_score - {user_score}\n computer_score - {computer_score}')
    elif user_choice == actual and computer_choice == actual:
        user_score += 1
        computer_score += 1
        print(f'User and Computer got it right!\n user_score - {user_score}\n computer_score - {computer_score}')
        
    print(f'It was {actual}')


    if user_score >= 3:
        print(f'{username} Won!')
        break
    elif computer_score >= 3:
        print('Computer Won!')
        break
    elif computer_score >= 3 and user_score >= 3:
        print("It's a draw.")
        break