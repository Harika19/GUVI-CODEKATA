n=(input())
if(n==n[::-1]):
    print("yes")
else:
    s=n.strip('0')
    if(s==s[::-1]):
        print("yes")
    else:
        f=n.lstrip('0')
        if(f==f[::-1]):
            print("yes")
        else:
            print("no")
        
