s=int(input("enter any number"))
a=int(input("enter any number"))
if s>a:
    s,a=s,a
else:
    s,a=a,s
while a:
    s,a=a,s%a
print(s)
