type=input()
rows=int(input())
columns=int(input())
people=rows*columns
if type=='Premiere':
    print(f'{12*people:.2f}')
elif type=='Normal':
    print(f'{7.5 * people:.2f}')
elif type == 'Discount':
    print(f'{5 * people:.2f}')