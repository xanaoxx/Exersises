f=open("17(3).txt")
m=[int(i) for i in f]
count=0
max_multi=0

def count_divisors(x):
    div=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            div.add(i)
            div.add(x//i)
    return len(sorted(div))
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_square_of_prime(x):
    if x<1:
        return False
    root=int(x**0.5)
    if root*root==x and is_prime(root):
        return True
    return False

for i in range(len(m)-1):
    div=abs(m[i]-m[i+1])
    if is_square_of_prime(div) and count_divisors(m[i])==count_divisors(m[i+1]):
        count+=1
        multi=m[i]*m[i+1]
        if multi%7==0:
            max_multi=max(max_multi,multi)
print(count,max_multi)
        
