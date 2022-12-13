n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
e=[]
f=0
for i in l:
    c.append(i)
for i in l:
    if i<a or i>b:
        d.append(i)
for i in l:
    if i not in d:
        e.append(i)
if len(e)>0:
    print(*e)
else:
    print('-1')
