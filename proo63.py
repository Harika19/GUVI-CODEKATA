#mine
n=input()
x=[]
for i in n:
    if i not in x:
        x.append(i)
    else:
        break
print(len(x))
        
        
