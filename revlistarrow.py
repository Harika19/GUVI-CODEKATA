n=int(input())
a=list(map(int,input().split()))
s=a[::-1]
for i in range(n):
    if (i!=n-1):
        print(s[i],end='->')
    else:
        print(s[i],end='')
