# calculate BMI

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = height/ weight ** 2
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normalweight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# calculate Leap Year

year = int(input("Which year do you want to check? "))

#Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")