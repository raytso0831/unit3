#Ray Tso
#2/28/18
#warmup8.py

total=0
num=100000
for i in range(1,num+1):
    if num%3 and num%10 and num%17==0:
        total+=i
        print(total)
