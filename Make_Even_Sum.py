n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i%2==1:
        a.append(i)
if len(a)%2==0:
    print('1')
else:
    print('0')
    
    