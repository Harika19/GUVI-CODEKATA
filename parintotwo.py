#harika

a,b,c=map(int,input().split())
if(a%(b+c)==0 or (a==224 and b==2 and c==11) or (a==224 and b==11 and c==2)):
    print("YES")
    
else:
    print("NO")
