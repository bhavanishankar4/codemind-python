n=int(input())
l=list(map(int,input().split()))
k=int(input())
b=[]
for i in l:
    if i not in b and l.count(i)==k:
        b.append(i)
if len(b)>0:
    print(*b)
else:
    print("-1")