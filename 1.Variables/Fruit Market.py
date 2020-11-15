price_Q=float(input())
B_kg=float(input())
P_kg=float(input())
M_kg=float(input())
Q_kg=float(input())
price_M=price_Q/2
price_P=60/100*price_M
price_B=price_M/5
sum=price_Q*Q_kg + price_B*B_kg + price_P*P_kg + price_M*M_kg
print(sum)