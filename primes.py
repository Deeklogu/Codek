x=int(input("enter the first number"))
y=int(input("enter the last number"))
flag=0
for i in range(x,y+1):
    for j in range(2,x):
        if i%j==0:
            flag=1
        else:
            print(i)
