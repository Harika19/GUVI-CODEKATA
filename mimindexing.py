n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(q):
    u,v=map(int,input().split())
    x.append(min(a[u-1:v]))
for j in range(len(x)):
    if j!=len(x)-1:
        print(x[j],end='\n')
    else:
        print(x[j],end='')
