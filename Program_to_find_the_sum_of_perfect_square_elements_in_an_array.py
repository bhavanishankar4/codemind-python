a=int(input())
l=list(map(int,input().split()))
b=[]
d=[]
for i in range(1,10):
    c=i*i
    b.append(c)
for i in l:
    if i in b:
        d.append(i)
print(sum(d))