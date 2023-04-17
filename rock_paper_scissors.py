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

#Write your code below this line 👇

list = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choice_word = list[choice]

computer_choice = random.randint(0,2)
computer_word = list[computer_choice]

print(f"You choose {choice_word}, the computer chose {computer_word}.")

if choice == 0 and computer_choice == 2:
    print("Rock beats Scissors. You win!")
elif choice == 1 and computer_choice == 0:
    print("Paper beats Rock. You win!")
elif choice == 2 and computer_choice == 1:
    print("Scissors beats Paper. You win!")
elif computer_choice == 0 and choice == 2:
    print("Rock beats Scissors. You lose.")
elif computer_choice == 1 and choice == 0:
    print("Paper beats Rock. You lose.")
elif computer_choice == 2 and choice == 1:
    print("Scissors beats Paper. You lose")
elif computer_choice == choice:
    print("It's a tie!")
else:
    print("Please choose again.")