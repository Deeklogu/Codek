s=int(input("enter any number"))
f=0
for i in range(2,s):
    if s%i==0:
        f=1
        print("not prime number")
if f==0:
     print("prime number")
