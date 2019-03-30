a,b=list(map(int,input().split()))
e=list(map(int,input().split()))
d=list(map(int,input().split()))
c=0
for i in d:
    if i not in e:
        print("NO")
        c+=1
        break
if(c==0):
    print("YES")

