c=0
a,b=map(str,input().split())
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if(a[i]==b[j]):
            c+=1
            a.replace(a[i],'')
            b.replace(b[j],'')
if(c>=2):
    print("yes")
else:
    print("no")
