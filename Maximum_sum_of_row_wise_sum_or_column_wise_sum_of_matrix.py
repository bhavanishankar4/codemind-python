r,c=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(r):
    l=list(map(int,input().split()))
    a.append(l)
    b.append(sum(l))
    
for j in range(len(a[0])):
    s=0
    for i in range(len(a)):
        s=s+a[i][j]
    c.append(s)
d=(max(b))
e=(max(c))
f=[d,e]
print(max(f))