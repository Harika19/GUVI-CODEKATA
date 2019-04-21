N,Q=map(int,input().split())
x=[]
a=list(map(int,input().split()))
for j in range(Q):
    u,v=map(int,input().split())
    s=0
    for k in range(u-1,v):
        s=s+a[k]
    x.append(s)
for l in range(len(x)):
    if(l!=len(x)-1):
        print(x[l],end='\n')
    else:
        print(x[l],end='')
