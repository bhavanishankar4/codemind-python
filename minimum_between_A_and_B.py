n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
e=[]
for i in l:
    if i<a or i>b:
        d.append(i)
for i in l:
    if i not in d:
        c.append(i)
if len(c)>0:
    print(min(c))  
else:
    print('-1')
        
    
    
