a=int(input("enter range"))
b=0
c=1
i=0
list=[]
list.append(b)
list.append(c)
while i<=a:
    d=b+c
    b=c
    c=d
    i=i+1
    list.append(d)
print(list)
