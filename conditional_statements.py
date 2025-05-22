#control flow 

# (if condition)
""" a = int(input("enter number 1st:"))
b = int(input("enter number 2nd:"))
if a>b:
    print(a)
if b>a:
    print(b) """
    
#(if-else condition)
""" a = int(input("enter number 1st:"))
b = int(input("enter number 2nd:"))

if a>b:
    print("1st is greater number"
else:
    print("2nd is greater number")
     """
     
     
# (If-Elif-Else)

""" a = float(input("enter number 1st:"))
b = float(input("enter number 2nd:"))

if a>b:
    print("1st is greater number")
elif a == b:
      print("a and b are equal")
else:
    print("2nd is greater number") """
    
    

""" a = int(input("Enter marks:"))
if a >= 85:
    print("A grade")
elif (a < 85 ) and (a >= 80):
    print("A- grade")
elif ( a > 80 ) and (a >= 75):
    print("B grade")
elif ( a > 75 ) and (a >= 70):
    print("B- grade")
else:
    print("Below average")
     """

# Nested if

x = int(input("Enter numbers:"))
if x>5:
    print(">5")
    print("Inside the top if")
    if x>10:
        print(">10")
        print("Inside the nested if")
    else:
        print("<=10")
        print("Inside the else part of nested if")
print("Outside all ifs")        