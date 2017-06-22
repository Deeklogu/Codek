s=int(input("enter any number"))
x=0
while s!=0:
    q=s//10
    r=s%10
    x=(x*10)+r
    s=q
print(x)
