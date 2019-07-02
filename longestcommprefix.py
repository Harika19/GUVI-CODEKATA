#harika
n=int(input())
c=[]
for i in range(0,n):
    c.append(input())
l=[]
for j in zip(*c):
    if(j.count(j[0])==len(j)):
        l.append(j[0])
  
    else:
        break
print(''.join(l))
