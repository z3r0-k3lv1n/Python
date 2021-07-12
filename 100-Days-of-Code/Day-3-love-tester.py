# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-07-02 13:05:14
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-07-02 13:38:41

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

# I also added the () around the if statement 
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")