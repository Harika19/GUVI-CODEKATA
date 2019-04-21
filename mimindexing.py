
n,q=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(q):
    u,v=map(int,input().split())
    x.append(min(a[u-1:v]))
for d in range(0,len(x)):
    print(x[d])
