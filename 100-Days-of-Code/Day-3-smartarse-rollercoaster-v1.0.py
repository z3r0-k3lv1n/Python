# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-06-29 17:53:52
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-06-29 18:05:50

# Print a greeting
print("Welcome to the smartarse rollercoaster!")
# set variable for height to assess eligibility to ride
height = int(input("What is your height in cm? "))
# set variable to store the cost of the ticket
bill = 0

# Create a condition todetermine eligibility to ride the rollercoaster
# You must be at least 120cm tall for safety
if height >= 120:
  print("Wow your taller than you look. Ok you can ride this rollercoaster!")
  # Set a variable for age. Ask the age of the participant to determine ticket price. Set as an input 
  # so the participant can enter their age in years.
  age = int(input("How old are you? "))
  # Set parameters to determine ticket price based on age 
  if age < 12:
    bill = 5
    print("Really. Are your parents freakishly tall. The child price is $5.")
  elif age <= 18:
    bill = 7
    print("WTF MF you look at least 30. 7 dollars!")
  elif age > 18:
    bill = 12
    print("You ancient f@#K tickets 12 bucks...")
  
  # Set a variable to store whether the participant also wants a photo souvenir.
  # Set the answer as either y for yes or n for no.
  souvenir = input("Do you want a photo with your ride? Type y or n: ")
  if souvenir == "y":
    # Add $3 to the price if the person says yes to a photo souvenir
    bill += 3
  # Tell the customer what the final ticket price is based on their age and whether they want a souvenir.
  print(f"Your final price is ${bill}. Enjoy your ride try not to spew all over my equipment.")

else:
  print("Sorry short arse, you'll need to grow taller to ride this rollercoaster.")
  