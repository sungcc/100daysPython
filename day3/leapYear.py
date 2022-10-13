# write a program that works out whether if a given year is a leap year.

# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#       unless the year is also evenly divisible by 400

year = int(input('which year do you want to check?\n'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else: print('not a leap year')
    else: print('leap year')
else: 
    print('that is not a leap year')
