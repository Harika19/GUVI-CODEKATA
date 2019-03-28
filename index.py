n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in range(n):
    if (a[i]==i):
        c=c+1
        b.append(i)

if (c!=0):
    for j in b:
        if (j!=b[-1]):
            print(j,end=' ')
        else:
            print(j)
else:
    print(-1)
