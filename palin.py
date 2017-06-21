s=int(input("enter any number"))
q=0
n=s
r=0
x=0
while n!=0:
    q=n//10
    r=n%10
    x=(x*10)+r
    n=q
if (x==s):
    print("palindrome")
else:
    print("not a palindrome")
