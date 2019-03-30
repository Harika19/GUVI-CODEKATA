#remove vowel and reverse a string
n=int(input())
i=str(input())
k=list(i)
r=0
for ch in k:
    if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I'
            or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        k.remove(ch)
f=k[::-1]
s = ''.join(f)
print(s)

