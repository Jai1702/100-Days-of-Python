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



game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You Chose:")
print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(game_images[computer_choice])

#Rock
if user_choice == 0 and computer_choice == 0:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win.")
#Paper
if user_choice == 1 and computer_choice == 1:
    print("It's a draw.")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
#Scissors
if user_choice == 2 and computer_choice == 2:
    print("It's a draw.")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
