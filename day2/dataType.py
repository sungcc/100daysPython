#write a program that adds digits in a 2 digit number. e.g if the input was 35, then the output should be 3 + 5 = 8

#warning. Do not change the code on lines 1-3. Your program should work for different input. e.g any two-digit number.

twoDigitNumber = input('please enter a two digit number.\n')

addOn = int(twoDigitNumber[0]) + int(twoDigitNumber[1])

print('The answer is ' + str(addOn) + '.')

