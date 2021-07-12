# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-06-27 19:44:28
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-06-27 20:34:52

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

weight_as_float = float(weight)
height_as_float = float(height)
bmi = round(weight_as_float / (height_as_float ** 2))

if bmi < 18.5:
  print(f"Your BMI is {bmi}. You are considered underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}. You are within a normal weight range.")
elif bmi < 30:
  print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}. You are obese.")
elif bmi > 35:
  print(f"DAMN. Your BMI is {bmi}. Step away from the cupcake. You are clinically obese.")