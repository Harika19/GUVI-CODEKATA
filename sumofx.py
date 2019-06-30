#harika
def sums(n):
    s=0
    r=0
    while(n):
        r=n%10
        s=s+r
        n=int(n/10)
    return s
def cals(n):
    for i in range(n+1):
        if(i+sums(i)==n):
            return i      
    return -1
n=int(input())
print("1",end='\n')
print(cals(n))    
