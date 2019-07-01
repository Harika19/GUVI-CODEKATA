a=input()
b="dhoni"
f=0
if(len(a)!=len(b)):
    print("no")
else:
    for i in b:
        if i in a:
            f=1
        else:
            f=0
            break
    if(f==1):
        print("yes")
    else:
        print("no")
