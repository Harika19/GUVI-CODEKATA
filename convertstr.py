#harika
a,b=input().split()
l=abs(len(a)-len(b))
for i in range(len(a)):
    if((len(b)==1) and (b[i] in a)) :
        break
    if(a[i]!=b[i]):
        l+=1
print(l)
