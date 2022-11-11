import random

while True:
    my_answer = input('do your choise--->stone/paper/scessior/quit:')
    my_answer = my_answer.lower()

    if my_answer == 'quit':
        break
    if my_answer != 'stone' and my_answer != 'paper' and my_answer != 'scessior':
        print("enter correct choise")
        continue

    computer_answer = random.choice(['stone', 'paper', 'scessior'])
    print(f"computer choise is:{computer_answer}")
    if my_answer == computer_answer:
        print("Its a tie")
    elif my_answer == 'stone' and computer_answer == 'scessior':
        print('you win')
        continue
    elif my_answer == 'paper' and computer_answer == 'stone':
        print('you win')
        continue
    elif my_answer == 'scessior' and computer_answer == 'paper':
        print('you win')
        continue
    else:
        print('you lost')
