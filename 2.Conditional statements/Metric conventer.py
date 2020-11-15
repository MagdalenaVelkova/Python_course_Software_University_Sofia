number=float(input())
in_measure=input()
out_measure=input()
if in_measure=='cm':
    number=number*10
elif in_measure=='m':
    number=number*1000

if out_measure=='mm':
    print(f'{number:.3f}')
elif out_measure=='cm':
    print(f'{number/10:.3f}')
elif out_measure == 'm':
    print(f'{number / 1000:.3f}')