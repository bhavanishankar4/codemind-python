a=int(input())
b=list(map(int,input().split()))
c=[]
z=[]
for i in range(1,10):
    d=i*i
    c.append(d)
for i in b:
    if i in c:
        z.append(i)
print(sum(z))