#PEMDAS
#Paretheses
#Exponents
#Multiplication
#Division
#Addition
#Subtraction

#Write a program that calculates the Body Mass Index from a user's weight and height.

weight = float(input('enter your weight in kg.\n'))
height = float(input('enter your height in m.\n'))
BMI = round(weight / height ** 2)

print('Your BMI is ' + str(BMI) + '.')

