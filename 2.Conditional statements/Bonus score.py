a=int(input())
bonus = 0
if a<=100:
    bonus=bonus+5
elif 1000>=a>100:
    bonus=bonus+a/5
elif a>1000:
    bonus=bonus+a/10

if a % 2 == 0:
    bonus=bonus+1
elif a % 5 == 0:
    bonus=bonus+2
print(f'{bonus} {a+bonus}')