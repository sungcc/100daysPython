# count the bill of pizza order

chooseSize = input('what size of pizza would you like to order? Small = S, Medium = M, Large = L\n').lower()

bill = 0

if chooseSize == 's':
    bill += 15
elif chooseSize == 'm':
    bill += 20
else:
    bill += 25

extraPepperoni = input('would you like to add extra pepperoni? Y or N\n').lower()

if extraPepperoni == 'n':
    bill = bill
elif extraPepperoni == 'y' and chooseSize == 's':
    bill += 2
elif extraPepperoni == 'y' and chooseSize == 'm' or 'l':
    bill += 3

extraCheese = input('would you like to add cheese? y or n\n').lower()

if extraCheese == 'y':
    bill += 1
else: 
    bill = bill
print(f"Your final bill is ${bill}")
