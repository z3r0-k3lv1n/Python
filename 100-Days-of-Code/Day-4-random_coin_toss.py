# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-07-04 15:59:14
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-07-04 16:03:17

# Random coint toss generator
# Two up game basis
# 

import random

toss1 = random.randint(1, 2)
toss2 = random.randint(1, 2)

print("Ladies and Gentlemen place your bets...")
print("")
play = input("Type play to play: \n")
print("")

if play == play:
  if toss1 == 1:
    print("Heads")
  else:
    print("Tails")
  if toss2 == 1:
    print("Heads")
  else:
    print("Tails")