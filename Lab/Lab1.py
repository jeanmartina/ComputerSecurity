import copy

print([x**2 for x in range(10)])
print(0xFF)
x=3.14
print(type(x))
print(1<<16)
x=16
print(x & 0x04)
print(~x)
print(float(1)/2)
a=[1,2,3,4,'x']
a.append(19)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(type(a))
print(dir(a))
a={}
print(dir(a))

''' tuples are not changable'''
x=((1,2),(3,4),"mystring")
print(type(x))
one,a,b=x
print(one)
print(a)
print(b)

''' control structures '''

if x==7:
    print("success")

''' reference sematics '''
a=[1,2,3]
b=copy.deepcopy(a)
a.append(4)
print(b)