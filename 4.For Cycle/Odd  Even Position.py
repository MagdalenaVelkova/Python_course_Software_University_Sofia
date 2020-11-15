import sys
n=int(input())
OddSum=0
EvenSum=0
OddMin=sys.maxsize
EvenMin=sys.maxsize
OddMax=-sys.maxsize
EvenMax=-sys.maxsize

for i in range(1,n+1):
        current_number=float(input())
        if i%2==0:
            EvenSum+=current_number
            if current_number>EvenMax:
                EvenMax=current_number
            if current_number<EvenMin:
                EvenMin=current_number


        elif i%2!=0:
            OddSum+=current_number
            if current_number>OddMax:
                OddMax=current_number
            if current_number<OddMin:
                OddMin=current_number
if n==1:
    print(f'OddSum={OddSum:.2f},\nOddMin={current_number:.2f},\nOddMax={current_number:.2f},\nEvenSum={EvenSum:.2f},\nEvenMin=No,\nEvenMax=No')
elif n==0:
    print(
        f'OddSum={OddSum:.2f},\nOddMin=No,\nOddMax=No,\nEvenSum={EvenSum:.2f},\nEvenMin=No,\nEvenMax=No')
else:
    print(f'OddSum={OddSum:.2f},\nOddMin={OddMin:.2f},\nOddMax={OddMax:.2f},\nEvenSum={EvenSum:.2f},\nEvenMin={EvenMin:.2f},\nEvenMax={EvenMax:.2f}')