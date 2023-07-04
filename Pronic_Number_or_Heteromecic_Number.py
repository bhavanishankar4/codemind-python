n=int(input())
f=0
temp=n
for i in range(1,n+1):
    if n%i==0:
        b=n//i
        if b==i+1:
            f=1
if f==1:
    if temp==i*b:
        print("YES")
else:
    print("NO")