n=input()
l=list(n)
if len(n)>9:
    if l[0]=="0":
        print("Invalid")
    else:
        print("Valid")
    
else:
    print("Invalid")
    