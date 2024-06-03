import random
art = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) ''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

game = [0,1,2]
computer = random.choice(game)

user = int(input('Enter your choice. 0 for Rock, 1 for Paper, 2 for Scissor? \n'))

if user >= len(game):
    print('Invalid selection.')
    exit()

print(f'you chose:\n{art[user]} \ncomputer chose:\n{art[computer]}')

if user == computer:
    print('It\'s a Draw')
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print('YAHOO!!! You won!!!')
else:
    print('Computer won. You lose.')
