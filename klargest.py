a,b=list(map(int,input().split()))
s=list(map(int,input().split()))
s.sort()
h=s[::-1]
for i in range(b):
    if(i==b-1):
        print(h[i])
