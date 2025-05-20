import numpy as np

#create numpy array
a = np.zeros(3)  #size 3
print(a)
print(type(a))   #a is array
print(type(a[0])) #type float

b = np.zeros(10) #size 10
print(b)

#change shape
b.shape
print(b)

b.shape = (10,1)
print(b)

#change val to ones
b = np.ones(10) #size 10
print(b)
print(type(b))   #b is array
print(type(b[0])) #type float

#empty array
b = np.empty(3)
print(b)

#val in array
b = np.linspace(2,10,5) # from 2 to 10, 5 val/element
print(b)

#create array with val list
z = np.array([10,20])
print(z)

a_list = [1,2,3,4,5,6,7]
z= np.array([a_list])
print(z)
print(type(z))  #type is array

#2d array

b_list = [[9,5,6],[1,3,4]]
r = np.array([b_list])
print(r)

#random nmber
np.random.seed(0)
z1 = np.random.randint(10, size=6)
print(z1)

#access val in array
print(z1[0])   
print(z1[0:2]) #range 2 val
print(z1[-1]) # last val

v = np.array([1,2,3,4,5])
print(v)

v<3
print(v)

v>3
print(v)

v[v>3]
print(v)

a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])

sum_array= a_array + b_array
print(sum_array)

sum2=a_array + 30
print(sum2)

mul_array = a_array * b_array
print(mul_array)

mul_a=a_array * 10
print(mul_a)

#dot product
#A⋅B=(a1×b 1)+(a2×b2)+(a3×b 3)+(a4×b4)+(a5×b5)
dot = a_array @ b_array
print(dot)

#sort array
x = np.array([3,6,7,8,9])
print(np.sort(x))
