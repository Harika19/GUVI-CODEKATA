n,k=map(int,input().split())
a=list(map(int,input().split()))
t=0
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]+a[j]==k):
            t=1
            print("yes")
            break
if(t==0):
    print("no")
        
