n=input()
s=list(n)
for i in range(0,len(n),2):
    t=s[i]
    s[i]=s[i+1]
    s[i+1]=t
print("".join(s))
