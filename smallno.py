#harika
#small no formed after deleting k digits using combinations
from itertools import combinations
a,b=input().split()
b=int(b)
k=[]
d=len(a)-b
f=combinations(a,d)
for i in list(f):
  k.append("".join(i))

print(min(k))
