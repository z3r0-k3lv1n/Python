# -*- coding: utf-8 -*-
# @Author: zero_kelvin && Dr. Angela Yu (London App Brewery)
# @Date:   2021-07-02 12:55:30
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-07-02 12:56:04


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

name_1 = name1.lower()
name_2 = name2.lower()
count_t = name_1.count("t") + name_2.count("t")
count_r = name_1.count("r") + name_2.count("r")
count_u = name_1.count("u") + name_2.count("u")
count_e = name_1.count("e") + name_2.count("e")
count_l = name_1.count("l") + name_2.count("l")
count_o = name_1.count("o") + name_2.count("o")
count_v = name_1.count("v") + name_2.count("v")
score_true = count_t + count_r + count_u + count_e
score_love = count_l + count_o + count_v + count_e

# The only thing that was not a part of my original code was encasing this 
# variable in an int()
score = int(str(score_true) + str(score_love))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:60]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

  def test_2(self):
    self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

  def test_3(self):
    self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

  def test_4(self):
    self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
