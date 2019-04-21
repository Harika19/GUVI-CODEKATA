n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(q):
    u,v=map(int,input().split())
    x.append(min(a[u-1:v]))
for d in range(len(x)):
    if d!=len(x)-1:
        print(x[d],end='\n')
    else:
        print(x[d],end='')
