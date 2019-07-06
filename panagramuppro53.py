s=str(input())
s=s.lower()
l=[]
q='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i not in l:
        l.append(i)       
l.sort()
u=''.join(l)
x=u.strip()
if(x==q):
    print("yes")
else:
    print("no")        
