bill = float(input('What was the total bill?\n'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15?\n'))

tipRound = (100 + tip) / 100 
people = int(input('How many people to split the bill?\n'))

total = round(bill * tipRound)
roundUp = total // people 
print(f'The total bill is {total}.\nEach person should pay: {roundUp}')
