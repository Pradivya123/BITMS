'''num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
if(num1>num2):
    print(num1,'num1 is greater')
elif(num1==num2):
    print('both are equal')
else:
    print(num2,'num2 is greater')'''
    

'''num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
print('num1 is greater' if num1>num2 else '''

#ternary
'''a=50
b=10
c=-15
print('a' if a>b and a>c else 'b' if b>c else 'c')'''

'''a=20
b=82
c=-23
d=56
e=-45
print('a' if a>b and a>c and a>d and a>e else 'b' if b>c and b>d and b>e else 'c' if c>d and c>e else 'd' if d>e else 'e')


num1=21
num2=12
num3=30
print('num1 is sufficient' if num1==num2 else 'num2 is less than 21' if)'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
for i in range(65,91):
    for j in range(65,i+1):
        print(chr(j),end=' ')
    print()'''
    
'''for i in range(1,11):
    print(i/10,end=' ')'''

a=-5
print(abs(a))
print(pow(2,3))

import math
a=math.sqrt(80)
print(a)
b=math.ceil(a)#ceil is roundup value of sqrt
print(b)


def divya():
    for i in range(1,11):
        print(i,"* 10","=",i*10)
divya()

      
      
      