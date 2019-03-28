n=int(input())
a=list(map(int,input().split()))
a.sort()
q=a[::-1]
r=0
for i in q:
    r=r*10+i
print(r)
