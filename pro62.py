
n=input()
x=[]
v=""
if(n==n[::-1]):
    x.append(0)
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        v=n[i:j+1]
        if(v==v[::-1]):
            x.append(len(n)-len(v))
print(min(x))
