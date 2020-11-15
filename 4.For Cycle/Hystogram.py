n=int(input())
less_than_200=0
between_200_399=0
between_400_599=0
between_600_799=0
bigger_than_800=0
for i in range (n):
    current_number=int(input())
    if current_number<200:
        less_than_200+=1
    elif 200<=current_number<=399:
        between_200_399+=1
    elif 400<=current_number<=599:
        between_400_599+=1
    elif 600<=current_number<=799:
        between_600_799+=1
    else: bigger_than_800+=1
print(f'{less_than_200/n*100:.2f}%\n{between_200_399/n*100:.2f}%\n{between_400_599/n*100:.2f}%\n{between_600_799/n*100:.2f}%\n{bigger_than_800/n*100:.2f}%')
