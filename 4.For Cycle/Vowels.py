text=input()
sum=0
for s in text:
    if s=='a' or s=='A':
        sum=sum+1
    elif s=='e' or s=='E':
        sum=sum+2
    elif s == 'i' or s == 'I':
        sum = sum + 3
    elif s == 'o' or s == 'O':
        sum = sum + 4
    elif s == 'u' or s == 'U':
        sum = sum + 5
print(sum)