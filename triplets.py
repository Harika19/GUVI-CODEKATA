n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(0,len(a)-2):
    for j in range(1,len(a)-1):
        for k in range(2,len(a)):
            if((a[i]<a[j]<a[k]) and (i<j<k)):
                c+=1
print(c)
