
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
if(abs((a-c)==(g-e))==abs((b-h)==(d-f))):
    print("yes")
else:
    print("no")
