#Ray Tso
#2/28/18
#warmup8.py

num=1
total=0
while num<100000:
    if num%3==0 and num%10==0 and num&17==0:
        total+=num
    num+=1
print(total)
        
