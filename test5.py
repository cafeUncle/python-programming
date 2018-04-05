# if else elif == != > >=

age = 21

if age > 16:
    print('you are old enough to drive')
else:
    print('you are not old enough to driver')

if age >= 21:
    print('21')
elif age >= 16:
    print('16')
else:
    print('0')

if (age >= 1) and (age <= 18):
    print('you get!')
elif (age == 21) or (age >= 65):
    print('guess')
elif not(age == 30):
    print('not')
else:
    print('yet')