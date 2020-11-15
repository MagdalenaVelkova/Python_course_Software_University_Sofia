import math
type=input()
if type=='square':
    a=float(input())
    square_area=a*a
    print(f'{square_area:.3f}')
elif type=='rectangle':
    a=float(input())
    b=float(input())
    print(f'{a*b:.3f}')
elif type=='circle':
    r=float(input())
    print(f'{r*r*math.pi:.3f}')
elif type=='triangle':
    a=float(input())
    ha=float(input())
    print(f'{a*ha/2:.3f}')