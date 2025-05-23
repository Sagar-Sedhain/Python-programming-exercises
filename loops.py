# Loops in python

# while loop
""" r = int (input("enter number:"))
i = 1
while i < r:
    print (i**2)
    print("This is iteration number :", i)
    i+=1            # i = i+1
print("close loop") """


i = 1
while True:
    if i%9 == 0:
        print("inside IF")
        break
    else:
        print("inside Else")
        i = i+1
print("loops finished")


""" i = 1
while True:
    if i%9 != 0:
        print("inside IF")
        i = i + 1 
        continue
    else:
        print("something")
        print("somethingElse")
        break
print("loops finished") """