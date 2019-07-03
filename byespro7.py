#harika
a=[]
n=int(input())
for i in range(0,n-1):
    a.append(abs(n-(2**i)))
print(min(a))
