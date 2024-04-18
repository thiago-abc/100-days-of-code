import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice >=3:
    print("You lose! Invalid number.")
else:
    computer_choice = random.randint(0, len(rock_paper_scissors_list) - 1)
    print(rock_paper_scissors_list[user_choice])
    print(f"Computer chose: {computer_choice}")
    print(rock_paper_scissors_list[computer_choice])

    if user_choice == 0:
        if computer_choice == 0:
            print("It's a draw.")
        elif computer_choice == 1:
            print("You lose.")
        else:
            print("You win!")

    elif user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        elif computer_choice == 1:
            print("It's a draw.")
        else:
            print("You lose!")

    else:
        if computer_choice == 0:
            print("You lose!")
        elif computer_choice == 1:
            print("You win!")
        else:
            print("It's a draw.")