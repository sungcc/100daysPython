#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder

number = float(input('Which name you want to check?\n'))

if number % 2 == 0:
    print('This is an even number')
else:
    print('This is an Odd number')
