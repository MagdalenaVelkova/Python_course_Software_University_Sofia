v=float(input())
if v<=10:
    print('slow')
elif v<=50:
    print('average')
elif v<=150:
    print('fast')
elif v<=1000:
    print('ultra fast')
elif v>1000:
    print('extremely fast')