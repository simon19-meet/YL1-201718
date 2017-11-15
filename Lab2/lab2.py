#exercise 1
def FirstLast(a):
    b=[a[0],a[-1]]
    return b
list1=[5, 10, 15, 20, 25]
list1=FirstLast(list1)
print(list1)

#exercise 2
list_a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range(len(list_a)-1):
    if list_a[i]<5:
        print(list_a[i])
##A
list_b=[]
list_c=[]
for value in list_a:
    if value<5:
        list_b.append(value)
print(list_b)
##B
x=7
for value in list_a:
    if value<x:
        list_c.append(value)
print(list_c)

#exercise 3
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
a2 = []
b2 = []
for value in a:
    for val in b:
        if val==value:
            c.append(val)
print(c)
for i in range(15):
    r=random.randint(0,101)
    a2.append(r)
for i in range(20):
    r=random.randint(0,101)
    b2.append(r)
print(a2)
print(b2)
for i in a2:
    for j in b2:
        if(i==j):
            c.append(i)
            print(i)
#exercise 4
print("ex 4:")
number=r
print(number)
def IsPrime(num):
    for i in range(1,num):
        if num%i==0:
            return False
    return True
print(IsPrime(number))
        



    
