import math

f=open("17(2).txt")
m=[int(i) for i in f]
count=0
max_summ=0
mn7=min([int(i) for i in m if i%7==0])

def is_prime(x):
    if x<2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for i in range(len(m)-2):
    a,b,c=m[i],m[i+1],m[i+2]
    summa=a+b+c
    if is_prime(a) and is_prime(b) and is_prime(c):
            if (a*b*c)<(mn7*mn7):
                if a%3==0 or b%3==0 or c%3==0:
                    count+=1
                    if summa%5==0:
                        max_summ=max(summa,max_summ)
                
print(count,max_summ)
