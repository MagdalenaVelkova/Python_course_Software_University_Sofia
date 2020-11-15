h=int(input())
min=int(input())
if min<45:
    print(f'{h}:{min+15}')
elif h<23 and min<=54:
    print(f'{h+1}:0{min-45}')
elif h<23 and min>54:
    print(f'{h+1}:{min-45}')
elif h>=23 and min<=54:
    print(f'0:0{min-45}')
elif h>=23 and min>54:
    print(f'0:{min-45}')