s=int(input("enter any number"))
n=s
b=0
while n!=0:
    q=n//10
    r=n%10
    b=b+(r*r*r)
    n=q
if b==s:
    print("armstrong")
else:
    print("not armstrong")
