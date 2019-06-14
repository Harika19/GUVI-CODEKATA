from itertools import permutations
s=input()
f=[]
l=[]
per=permutations(s)
for x in list (per):
   print(''.join(x))
   
