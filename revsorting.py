
a=int(input())
n=list(map(int,input().split()))
n.sort()
n.reverse()
for i in range(0,a):
    if(i!=len(n)-1):
        print(n[i],end='\n')
    else:
        print(n[i],end='')
