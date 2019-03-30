#reverse each word individuallu
n=str(input())
a=n.split(" ")
u=0
for i in a:
    u=i[::-1]
    s="".join(u)
    print(s,end=" ")
