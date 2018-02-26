#Ray Tso
#2/18/18
#perfectNumber.py

num=int(input('Enter a number:'))
for i in range(1,num):
    if num%i==0:
        print(i)
    
    if i==num:
        print('This number is a a perfect number')
