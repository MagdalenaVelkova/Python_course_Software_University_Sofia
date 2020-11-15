city=input()
sales=float(input())
commission=0
if city=='Sofia':
    if sales<=500 and sales>=0:
            commission=5/100
            print(f'{commission * sales:.2f}')
    elif sales<=1000 and sales>500:
            commission=7/100
            print(f'{commission * sales:.2f}')
    elif sales<=10000 and sales>1000:
            commission=8/100
            print(f'{commission * sales:.2f}')
    else: print(f'{12/100 * sales:.2f}')