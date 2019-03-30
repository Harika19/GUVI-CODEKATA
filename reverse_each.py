#reverse each word individuallu
n=input()
b=n.split()
x=len(b)
for i in range(x):
    t=b[i]
    if i!=x-1:
        print(t[::-1],end=' ')
    else:
        print(t[::-1])
'''n=str(input())
a=n.split(" ")
u=0
for i in a:
    if(i!=len(a)):
       u=i[::-1]
       print(u,end=" ")
    else:
        print(u)'''
