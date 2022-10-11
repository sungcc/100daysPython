#PEMDAS
#Paretheses
#Exponents
#Multiplication
#Division
#Addition
#Subtraction

#Write a program that calculates the Body Mass Index from a user's weight and height.

weight = int(input('enter your weight in kg.\n'))
height = float(input('enter your height in m.\n'))
BMI = round(weight / (height ** 2), 2)

print('Your BMI is ' + str(BMI) + '.')

if BMI < 18.5:
    print('you are underweight')
elif BMI < 25:
    print('normal weight')
elif BMI <30:
    print('overweight')
elif BMI <35:
    print('obese')
else:
    print('clinically obese')


