import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#emoji =  [rock, paper, scissors]
# emoji = [0,       1,       2  ]

emoji = [rock, paper, scissors]

user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_answer >= 3 or user_answer < 0:
    print("The number must be between 0 and 2, you loose!")
else:
    print(f"You choose: {emoji[user_answer]}")

    computer_choice = random.randint(0, 2)

    print("Computer chose:")
    print(emoji[computer_choice])

    if user_answer == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_answer == 2:
        print("You lose!")
    elif computer_choice > user_answer:
        print("You lose!")
    elif user_answer > computer_choice:
        print("You win!")
    elif user_answer == computer_choice:
        print("It's a draw!")
