# Defining of function
def printSucess():
    print("hello")
    print("world")

printSucess()


def printSuccess1():
    print("hello")    
printSuccess1()


# Function (input argument)
def print_message(msg):
    print(msg)
    
print_message(2)


def printMsg(msg):
    if isinstance(msg,int):    
        print(msg)
    else:
        print("your input argument is not number")
printMsg("hello")

y = 12
printMsg(y)

# Multiple arguments
def powFunction(a,b):
    c = a**b
    print (c)
      
powFunction(4,3)
    

def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("error")
checkArgs(1,2,3)
checkArgs(2,1,"hell0")


# Order of input function

def f(a,b,c):
    print("A is :", a)
    print("B is :", b)
    print("c is :", c)
    
f(2,3,"hello")
f(c= "hello", b= 2, a = 1)


# Function (variables inside)

def addition(x,y):
    sumValue = x+y
    print(sumValue)
    
addition(7,4)


# function (return statement)
# Scope of variable

def addition(x,y):
    sumValue = x+y
    return sumValue
    
sumValue = addition(7,4)

print(sumValue)


# Variable outside the function

variableOutSidefunction = 3

def x():
    variableOutSidefunction = 5
    #print(variableOutSidefunction)
x()
print(variableOutSidefunction)


def a():
    print("A")
    q = 3
    w = 5
    c = q+w
    print("B")
    return
    print("hello")  
a()
    
    
def r():
    a = 1
    b = 2
    c = 3
    d = "hello"
    return a,b,c,d
w,x,y,z = r()

print (w,x,y,z)


# Functions number of input arguments

def add1(*numb):
    sum = 0
    for i in range(len(numb)):
        sum += numb[i] # sum = sum + numb [i]
    return sum
print(add1(1,2,3,4,5,9.1))


# function  variable number of input variable 

def variable(**numb):
    for x in numb:
        print (x, numb[x])
variable(a = 3, b = 2, c = "nuibiwe")



# function default value

A = [1,2,3]
A2 = A
A2[0] = 7
print (A)

def  AA(A = [0,2,3,4]):
    for i in A:
        print (i)
A2 = [1,6,7]
AA()
AA(A2)


# Function exercise
#finding the minimum number and its index

def farrange(L):
    m = L[0]
    idx = 0
    i = 0
    for x in L:
        if x<m:
            m =x
            idx = i
        else:
            pass
        i +=1
    return m,idx
(a,b) = farrange([2,3,1, 9,6,7])
print(a,b)

# Swaping the value

def swapValue(L,idx1,idx2):
    temp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = temp
    return L
L= [1,2,3,4,5,6,7]
L2 = swapValue (L,0,1)
print(L2)
 