n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in lst:
    a.append(i)
b=set(a)
print(*b)
    
      