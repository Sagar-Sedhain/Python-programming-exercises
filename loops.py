# Loops in python

# while loop
""" r = int (input("enter number:"))
i = 1
while i < r:
    print (i**2)
    print("This is iteration number :", i)
    i+=1            # i = i+1
print("close loop")
 """

i = 1
while True:
    if i%9 == 0:
        print("inside IF")
        break
    else:
        print("inside Else")
        i = i+1
print("loops finished")


i = 1
while True:
    if i%9 != 0:
        print("inside IF")
        i = i + 1 
        continue
    else:
        print("something")
        print("somethingElse")
        break
print("loops finished")


# For loop
A = []
#for i in range(10):
for i in range(0,10,2):
     
    print(i)
    A.append(i**2)
print(A) 


# else in for Loops
S = {"apple",3.9,"cherry", "hello", "ram", 4}
i = 1
for x in S:
    print(x)
    i = i+1
    if i ==4:
        break
    else:
        pass 
else:
    print("Loops terminate")
print("out from the loop")
 
A ={"hello":11, "ram":12, "krishna":"abc"}
for x in A:
    print(x,A[x])  
    
    
# print in increasing  order
    
A = [1,2,3,-5,7,9,3,2]
for j in range (len(A)):
    B = A[j]
    idx = j
    c = j
    for i in range(j, len(A)):
        if A[i]<B:
            B = A[i]
            idx = c
        c += 1
    tmp = A[j]
    A[j] = B
    A[idx] = tmp
print(A)

    