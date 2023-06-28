r,c=map(int,input().split())
e=0
o=0
for i in range(r):
    l=list(map(int,input().split()))
    if i%2==0:
        e+=sum(l)
    else:
        o+=sum(l)
print(e,o)