n=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
for i in range(0,n-1,2):
    if(a[i]!=a[i+1]):
        print(a[i])
        c=c+1
        break
if(c==0):
    print(a[-1])

