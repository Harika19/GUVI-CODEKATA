n=int(input())
a=list(map(int,input().split()))
t=0
b=[]
for i in range(n):
    if a[i]==i:
        t+=1
        b.append(i)
if t!=0:
    for j in b:
       
            print(j,end=' ')
       
else:
    print(-1)
