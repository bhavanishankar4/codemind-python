def gcd(x,y):
    while (y):
        x,y=y,x%y
    return(x)
        
    
x,y=map(int,input().split())
hcf=gcd(x,y)
print(hcf)