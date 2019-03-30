#reverse each word individuallu
n=str(input())
a=n.split(" ")
u=0
for i in a:
    if(i!=len(a)):
       u=i[::-1]
       print(u,end=" ")
    else:
        print(u)
