n=int(input())
salary=int(input())
penalty=0
for i in range(n):
    current_website=input()
    if current_website=='Facebook':
        penalty+=150
    elif current_website=='Instagram':
        penalty +=100
    elif current_website=='Reddit':
        penalty +=50
if salary-penalty<=0:
    print('You have lost your salary. ')
else: print(salary-penalty)