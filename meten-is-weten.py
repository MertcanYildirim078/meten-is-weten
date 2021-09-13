a = input('De waarde van a ')
b = input('De waarde van b ')

if a > b:
    a = max
    print('a is het grootste getal' +str (a))

elif a < b:
    a = min
    print('a is het kleinste getal' +str (a))
    



else:
    print(str('a is gelijk aan b'))

    print('Het minimum is: ' +str (min))
    print('Het maximum is: ' +str (max))
