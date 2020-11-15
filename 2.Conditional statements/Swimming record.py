import math
record=float(input())
distance=float(input())
velocity=float(input())
Delay=(distance//15*12.5)
Ivancho_time=velocity*distance+Delay
if Ivancho_time>=record:
    print(f'No, he failed! He was {Ivancho_time-record:.2f} seconds slower.')
else: print(f'Yes, he succeeded! The new world record is {Ivancho_time:.2f} seconds.')


