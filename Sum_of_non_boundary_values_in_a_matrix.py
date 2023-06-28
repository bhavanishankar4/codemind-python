r,c=map(int,input().split())
l=[]
a=0
for i in range(r):
    lst=list(map(int,input().split()))
    l.append(lst)
for i in range(1,r-1):
    for j in range(1,c-1):
        a+=l[i][j]
print(a)
    