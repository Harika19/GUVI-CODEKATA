n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(q):
    u,v=map(int,input().split())
    s=0
    for z in range(u-1,v):
        s=s+a[z]
    x.append(s)
for d in range(len(x)):
    if d!=len(x)-1:
        print(x[d],end='\n')
    else:
        print(x[d],end='')
