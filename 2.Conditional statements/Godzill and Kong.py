buget=float(input())
extras=int(input())
price_pre_extra=float(input())
art=buget/10
costume=0
if extras>150:
    costume=extras*price_pre_extra*9/10
else: costume=extras*price_pre_extra

if buget-costume-art>=0:
    print(f'Action!')
    print(f'Wingard starts filming with {abs(buget-costume-art):.2f} leva left.')
else: print(f'Not enough money!\nWingard needs {abs(buget-costume-art):.2f} leva more.')
