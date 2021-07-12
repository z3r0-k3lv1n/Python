# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-06-29 17:10:06
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-06-29 17:20:12

# This calculator will take a year inputed by the user and determine
# whether the year is a leap year or not. Using the following rules.
# The year entered can be divided evenly by 4
# The year is not evenly divided by 100
# Unless the year can also be divided evenly by 400

# Sets a variable called year which is then defined as an input
# entered by the user.
year = int(input("Which year do you want to check? "))

# Determine if the year entered is evenly divisible by 4 but not also
# evenly divisible by 100 using the modulo method.
if (year % 4) == 0 and (year % 100) != 0:
    print(f"{year} IS a leap year.")
    # Determine if the year is evenly divisible by both 400 and 100 using modulo. 
    if (year % 400) == (year % 100) == 0:
            print(f"The year {year} IS a leap year.")
# Print a statement indicating whether the year entered in the input is not a leap
# year if it fails the above tests.
else:
    print(f"The year {year} is NOT a leap year.")