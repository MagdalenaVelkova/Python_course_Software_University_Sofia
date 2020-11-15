first_time=int(input())
second_time=int(input())
third_time=int(input())
sum=first_time+second_time+third_time
if sum%60<10:
    print(f'{sum//60}:0{sum%60}')
else: print(f'{sum//60}:{sum%60}')
