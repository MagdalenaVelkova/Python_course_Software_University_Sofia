commission=0
city=input()
sales=float(input())
if sales<0:
    print('error')
else:
    if city=='Sofia':
        if sales<=500 and sales>=0:
            print(f'{5/100 * sales:.2f}')
        elif sales<=1000 and sales>500:
            print(f'{7/100 * sales:.2f}')
        elif sales<=10000 and sales>1000:
            print(f'{8/100 * sales:.2f}')
        else: print(f'{12/100 * sales:.2f}')
    elif city=='Varna':
        if sales <= 500:
            commission = 4.5 / 100
            print(f'{commission * sales:.2f}')
        elif sales <= 1000:
            commission = 7.5 / 100
            print(f'{commission * sales:.2f}')
        elif sales <= 10000:
            commission = 10 / 100
            print(f'{commission * sales:.2f}')
        else: print(f'{13/100* sales:.2f}')
    elif city=='Plovdiv':
        if sales <= 500:
            commission = 5.5 / 100
            print(f'{commission * sales:.2f}')
        elif sales <= 1000:
            commission = 8 / 100
            print(f'{commission * sales:.2f}')
        elif sales <= 10000:
            commission = 12 / 100
            print(f'{commission * sales:.2f}')
        else: print(f'{14.5/100 * sales:.2f}')
    else: print('error')




