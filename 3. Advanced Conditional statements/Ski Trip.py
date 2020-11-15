n_days=int(input())
type_room=input()
grade=input()
if type_room=='room for one person':
    if n_days<=10:
        if grade=='positive':
            print(f'{((n_days-1)*18)*125/100}
        else:
            print(f'{(n_days-1)*18*90/100:.2f})
elif type_room=='apartament':
elif type_room=='president apartament':