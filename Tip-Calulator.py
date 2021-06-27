# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-06-27 11:56:30
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-06-27 14:14:01
# This is a simple tip calculator written in python

print("Welcome to our Tip Calculator.\nWe hope you enjoyed your meal.\nIn order to calculate the appropriate Tip for your server we will need some information.")
bill = input("What was the total cost of the bill? $")
party_size = input("How many people in your party? ")
tip = input("What percentage tip do you wish to leave for your server? ")
bill_tip = float(tip) / 100 + 1 
total = str(round(float(bill) * float(bill_tip), 2))
even_share = str(round(float(total) / float(party_size), 2))
print(f"Each person should pay an even split of ${even_share}\nA tip of {tip}% makes the total bill ${total}")