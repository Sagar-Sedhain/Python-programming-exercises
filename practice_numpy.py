# numpy - nummerical python 
import numpy as np 

a= np.array ([1,2,3,4,5,6],dtype='i') #list
b = np.array((8,7,9)) #tuple
print(a)
print(type(a))
print(type(a.dtype))

# numpy dimension
x = np.array ([[1,2,3],[4,5,6]])
print(x.ndim)
print(x)

y = np.array ([[[3,2,1],[6,5,6]],[[4,6,7],[2,1,5]]])

print(y.ndim)
print(y)
print(y.shape)

B = np.array([1])
B.ndim
print(B.ndim)

B = np.array((1,2,3)) 
B.ndim
print(B.ndim)

A = np.arange(100)
print(A)

""" A = np.arange(20,100,3)
print(A) """

B = A [3:10]
print(B)

B [0] = -1200
"""print(B) """

#print(A)

B = A[3:10].copy()
print(B)
print(A [::5])
print(A [::-5])
print(A [::-1])

print(A)

idx = np.argwhere(A == -1200)[0][0]
print(idx)

A [idx] = 3
print(A)

A = np.round(10* np.random.rand(5 ,4))
print(A)

print (A[1,2])
print (A[1,:])
print (A[:,1])

print (A[1:3,2:4])
print(A.T)

import numpy.linalg as la
print(la.inv(np.random.rand(3,3)))

print(A)
A.sort(axis = 1)
print(A)

X = np.arange(50)
Y = X [[3,5,6]]


Y [0] = -4
print(Y)
print(X)
#Y = X[X<40]
Y = X[(X<40) & (X>30)]
print(Y)

# & , and
# / , or
# not


# numpy broadcasting
A = np.array ([ [1,2,3],[1,5,6]])
#B = A + 5
#print (B)

#c = A+(np.arange(2).reshape(2,1))
#print(c)
B = np.round(10*np.random.rand(2,2))

C = np.hstack((A,B))
print(C)

A  = np.random.permutation(np.arange(10))

print(A)

print(np.sort(A))

A = np.array(['hello', 'how', 'are', 'you1'])
B = np.sort(A)
print(B)

