#write a program using maths and f-strings tells us how many days, weeks, month we have left if we live until 90 years old

#Your have x days, y weeks, and z months left.

age = int(input('Your current age: \n'))
totalAge = 90
totalMonth = 90 * 12
totalWeeks = 90 * 52
totalDays = 90*365

currentDays = age * 365
currentMonth = age * 12
currentWeeks = age * 52

daysLeft = totalDays - currentDays
weeksLeft = totalWeeks - currentWeeks
monthLeft = totalMonth - currentMonth

print(f'You have {daysLeft} days, {weeksLeft} weeks, and {monthLeft} months left.')
