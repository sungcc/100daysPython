# create a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.

# don't change the code below
print("Welcome to the Love Calculator!")
name1 = input('What is your name? \n').lower()
name2 = input('What is their name? \n').lower()
###not change above

#write your code below

cname = name1 + name2 

TCount = cname.count('t')
RCount = cname.count('r')
UCount = cname.count('u')
ECount = cname.count('e')
trueTotal = TCount + RCount + UCount + ECount

LCount = cname.count('l')
OCount = cname.count('o')
VCount = cname.count('v')
ECount = cname.count('e')
loveTotal = LCount + OCount + VCount + ECount
compine = str(trueTotal) + str(loveTotal)
score = int(compine)
print(f'T occurs {TCount} time\n')
print(f'R occurs {RCount} time\n')
print(f'U occurs {UCount} time\n')
print(f'E occurs {ECount} time\n')
print(f'Total = {trueTotal} \n')

print(f'L occurs {LCount} time\n')
print(f'O occurs {OCount} time\n')
print(f'V occurs {VCount} time\n')
print(f'E occurs {ECount} time\n')
print(f'Total = {loveTotal} \n')
print(f'Love score = {compine}\n')
print(f'Your score = {compine}\n')

if score < 10 or score > 90:
    print(f'Your score is {compine}, you go together like coke and mentos.')
elif score >= 40 and score <=50:
    print(f'Your score is {compine}, you are alright together.')
else: 
    print(f'Your score is {compine}')
