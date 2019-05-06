
n=int(input())
a=list(map(int,input().split()))
left=[]
right=[]
for i in range(0,n-1):
    left=a[:i+1]
    right=a[i+1:]
    if((sum(left)//len(left))==(sum(right)//len(right))):
        print("yes")
        break
else:
        print("no")
    
