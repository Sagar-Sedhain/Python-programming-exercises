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