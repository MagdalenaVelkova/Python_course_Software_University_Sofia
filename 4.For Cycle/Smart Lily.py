import math
lily_age=int(input())
washing_machine_price=float(input())
price_of_toy=int(input())
if lily_age%2==0:
    toy_money = (lily_age // 2) * price_of_toy
else: toy_money=(lily_age//2+1)*price_of_toy

money=0
for age in range(1,lily_age+1):
    if age%2==0:
        money=age*5-1+money
if toy_money+money<washing_machine_price:
    print(f'No! {washing_machine_price-toy_money-money:.2f}')
else: print(f'Yes! {toy_money+money-washing_machine_price:.2f}')