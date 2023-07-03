r,c=map(int,input().split())
a=[]
b=[]
for i in range(r):
    l=list(map(int,input().split()))
    a.append(l)
for j in range(len(a[0])):
    s=0
    for i in range(len(a)):
        s=s+a[i][j]
    b.append(s)
print(max(b))