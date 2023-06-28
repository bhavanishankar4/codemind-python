r,c=map(int,input().split())
l=[]
a=0
b=0
for i in range(r):
    lst=list(map(int,input().split()))
    l.append(lst)
for i in range(r):
    for j in range(c):
        a+=l[i][j]
for i in range(1,r-1):
    for j in range(1,c-1):
        b+=l[i][j]
print(a-b)
