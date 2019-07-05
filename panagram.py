s=str(input())
l=[]
q=' abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i not in l:
        l.append(i)       
l.sort()
u=''.join(l)
print(u)
if(u==q):
    print("yes")
else:
    print("no")        
