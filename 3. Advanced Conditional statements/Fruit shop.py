fruit=input()
day=input()
amount=float(input())
if day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday':
    if fruit=='banana':
        print(f'{amount*2.5:.2f}')
    elif fruit=='apple':
        print(f'{amount*1.2:.2f}')
    elif fruit == 'orange':
        print(f'{amount * 0.85:.2f}')
    elif fruit == 'grapefruit':
        print(f'{amount * 1.45:.2f}')
    elif fruit == 'kiwi':
        print(f'{amount * 2.70:.2f}')
    elif fruit == 'pineapple':
        print(f'{amount * 5.5:.2f}')
    elif fruit == 'grapes':
        print(f'{amount * 3.85:.2f}')
    else: print('error')
elif day=='Saturday' or day=='Sunday':
    if fruit=='banana':
        print(f'{amount*2.7:.2f}')
    elif fruit=='apple':
        print(f'{amount*1.25:.2f}')
    elif fruit == 'orange':
        print(f'{amount * 0.9:.2f}')
    elif fruit == 'grapefruit':
        print(f'{amount * 1.6:.2f}')
    elif fruit == 'kiwi':
        print(f'{amount * 3:.2f}')
    elif fruit == 'pineapple':
        print(f'{amount * 5.6:.2f}')
    elif fruit == 'grapes':
        print(f'{amount *4.2 :.2f}')
    else: print('error')
else: print('error')