import sys
n=int(input())
sum=0
max_num=-sys.maxsize
for i in range (n):
    number=int(input())
    sum=sum+number
    if number>max_num:
        max_num=number
if max_num==sum-max_num:
    print(f'Yes \n Sum = {sum-max_num}' )
else: print(f'No \n Diff = {abs(sum-2*max_num)}')