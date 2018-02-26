#Ray Tso
#2/18/18
#perfectNumber.py


num = int(input('Enter a number: '))
total = 0
for i in range(1,num):
    if num%i==0:
        total = total + i
if total == num:
    print('This number is a Perfect number')
else:
    print('This number is Not perfect')