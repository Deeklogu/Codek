s=int(input("enter any number to be multiplied"))
n=int(input("enter any number where the table to be stopped"))
for i in range(1,n+1):
    a=i*s
    print(str(i) +" *"+ str(s)+" ="+str(a))
