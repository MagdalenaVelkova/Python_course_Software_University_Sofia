n=int(input())
sum_even=0
sum_odd=0
for i in range (n):
    number=int(input())
    if i%2==0:
        sum_even+=number
    else: sum_odd+=number
if sum_odd==sum_even:
    print(f'Yes\n Sum = {sum_odd}')
else: print(f'No\n Diff = {abs(sum_odd-sum_even)}')