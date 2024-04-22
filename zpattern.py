name=str(input("enter name:"))
length=len(name)
for i in range(length):
    for j in range(length):
        if i==0 or i==length or i == length-1 or i+j==length-1:
            print(name[j],end=" ")
        else:
            print(" ",end=" ")
    print()
if (((i==0 or i==length) and j>=0 and j<=length)or i+j==length-1 ):
    print(name)
    
    
'''name = "pradivya"
length = len(name)
for i in range(length):
    print((length-i-1)*' ' + name[i])
for i in range(length-2, -1, -1):
    print((length-i-1)*' ' + name[i])'''

name = "Seetha"
length = len(name)
for i in range(length):
    print((length-i-1)*' ' + name[i])
for i in range(length-2, -1, -1):
    print((length-i-1)*' ' + name[i])