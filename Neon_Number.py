n=int(input())
add=0
Ori=n
N=pow(n,2)
while N:
    r=N%10
    add=add+r
    N=N//10
if Ori==add:
    print("Neon Number")
else:
    print("Not Neon Number")