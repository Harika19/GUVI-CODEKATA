k=int(input())
s=[]
for i in range(k):
    a=list(map(int,input().split()))
    for k in a:
        s.append(k)
s.sort()
for j in range(len(s)):
    if (j!=len(s)-1):
        print(s[j],end=' ')
    else:
        print(s[j],end='')

