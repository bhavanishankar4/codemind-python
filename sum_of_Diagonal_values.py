r,c=map(int,input().split())
l=[]
a=0
b=0
for i in range(r):
    lst=list(map(int,input().split()))
    l.append(lst)
for i in range(r):
    for j in range(c):
        if i==j:
            a+=l[i][j]
        elif i+j==r-1:
            b+=l[i][j]
print(a+b)