s=input("enter any string")
c=0
c1=0
for i in s:
  if i.isalpha():
    c=c+1
  else:
    c1=c1+1

print(c)
print(c1)
