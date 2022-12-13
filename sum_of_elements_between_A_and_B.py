n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in l:
    c.append(i)
e=sum(c)    
for i in l:
    if i<a or i>b:
        d.append(i)
f=sum(d)        
print(e-f)        
    