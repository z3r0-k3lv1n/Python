# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-06-27 11:56:30
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-06-27 18:08:13
# This is a simple tip calculator written in python

print("Welcome to our Tip Calculator.\nWe hope you enjoyed your meal.\nIn order to calculate the appropriate Tip for your server we will need some information.")
bill = input("What was the total cost of the bill? $")
party_size = int(input("How many people in your party? "))
tip = input("What percentage tip do you wish to leave for your server? ")
bill_tip = float(tip) / 100 + 1 
total = round(float(bill) * float(bill_tip), 2)
bill_per_person = round(float(total) / float(party_size), 2)
# Formatting is usde to properly format the rounding of floats to 2 decimal
# places when dealing with a zero amount in the last place eg 33.60
even_share = "{:.2f}".format(bill_per_person)
final_bill = "{:.2f}".format(total)
print(f"Each person should pay an even split of ${even_share}\nA tip of {tip}% makes the total bill ${final_bill}")
