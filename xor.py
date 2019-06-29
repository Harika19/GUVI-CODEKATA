a,b=map(int,input().split())
c=list(map(int,input().split()))
x=[]
for i in range(b):
    u,v=map(int,input().split())
    s=0
    for j in range(u-1,v):
        s=s^c[j]
    x.append(s)
for k in range(len(x)):
    if (k!=len(x)-1):
        print(x[k],end='\n')
    else:
        print(x[k],end='')
    
