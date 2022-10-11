#nested if and elif statment practice

#over 120cm can play rollercoaster
height = int(input('what\'s your height in cm?\n'))

if height >= 120:
    print('you are allowed to play')
    age = int(input('how old are u\n'))
    if age < 12:
        print('please pay $5')
    elif age <= 18:
        print('please pay $8')
    else: 
        print('please pay $18')

else:
    print('you are not allowed to play. go grow taller')
