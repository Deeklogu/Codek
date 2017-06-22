s=int(input("enter first number"))
x=int(input("enter last number"))
b=0
for i in range(s,x+1):
    n=i
    while n!=0:
        q=n//10
        r=n%10
        b=b+(r*r*r)
        n=q
    if b==i:
        print(b)
    b=0
