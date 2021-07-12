# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-07-12 17:57:48
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-07-12 17:58:13
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

import random

hand = [rock, paper, scissors]
computer_choice = random.randint(0,2)
player_choice = int(input("Please enter your choice.\nType '0' for Rock\nType '1' for Paper\nType '2' for Scissors:\n"))

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number...\nYou lose.")
else:
    print(f"{hand[player_choice]}\nThe computer chose:\n{hand[computer_choice]}")
    if player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif computer_choice > player_choice:
        print("You Lose!")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice == player_choice:
        print("It's a draw!")


