n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for x in a:
    if x not in b:
        b.append(x)
    else:
        c.append(x)
c.sort()
for i in c:
    print(i,end=' ')
