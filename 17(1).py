f=open("17(1).txt")
m=[int(i) for i in f]

arifm=sum(m)/len(m)

def is_palindrom(num):
    binn=bin(num)[2:]
    return binn==binn[::-1]

count=0
max_sum=0
for i in range(len(m)-1):
    multi=m[i]*m[i+1]
    summa=m[i]+m[i+1]
    if (m[i]%2==0 and m[i+1]%2==0):
        if is_palindrom(multi):
            count+=1
            max_sum=max(max_sum,summa)
    elif (m[i]%2!=0 or m[i+1]%2!=0) and summa>arifm:
        count+=1
        max_sum=max(max_sum,summa)

print(count,max_sum)
            
        

