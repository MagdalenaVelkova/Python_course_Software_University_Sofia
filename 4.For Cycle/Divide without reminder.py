n=int(input())
div_2=0
div_3=0
div_4=0
for i in range (n):
    current_number=int(input())
    if current_number%2==0:
        div_2+=1
    if current_number%3==0:
        div_3+=1
    if current_number%4==0:
        div_4+=1
print(f'{div_2/n*100:.2f}%\n{div_3/n*100:.2f}%\n{div_4/n*100:.2f}%')
