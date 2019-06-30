
a=int(input())
b=list(map(int,input().split()))
g=[]
c=1
for i in range(0,a-1):
    if(b[i+1]>b[i]):
        c+=1
    else:
        g.append(c)
        c=1
g.append(c)
print(max(g))
