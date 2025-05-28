#concate of string
a = 'hey!'
b = 'How are you'
c = a + ' ' +b
print(c)

# Concatenate int value and string
a = 2
b = "hello"
c = b+" "+ str(a)
print (c)

# multiline string
a = """Hello my name is sagar.
i live in linz austria.
i am from nepal"""
print(a)

# indexing and sclicing

# [start:end:step] if step,start,end is not mentioned the default index is 0, so we have to mention the step 

a = 'Buddha was born in nepal'
print(a[3:10])
print(a[-3:-10])
print (len(a))
print(len(a[0:3]))
print (a[::1])


#sting strip methods
a = "A Lazy FOx JumPs       Over the wall 1"
b = a.strip()
print(b)
print(b.lower())
print(b.upper())
print(a.replace("1","."))


#a = "abc;def;ghij;klm;123"
#print(a.replace(";",""))

L = a.split(";")
print(L)
print(L[0])

L = ['hello',4,'how',5,'are']
L.append('ram')
L.reverse()
print(L) 
 
# List, tuple, set, dictionary 
L = ['hello',4,'how',5,'are']
T = (a,3,4.9,'name',3)
S = {1,23,3,4.8,'name'}
D = {3:'three', 'B':23, 'new':'newvalue','y':'xy', 'z':12}
D2 = {'A':L, 'B':T, 'C':S, 'D':D }

K = D2['D']
for x in K:
    print(x,K[x])
#print(L,T,S,D)

M = [x**2 for x in range(10)]
print (M)

# take a differernt marks data from students different students and compute its average value 

def getDataFromUser():
    D = {}
    while True:
        studentId = input('Enter student ID: ')
        studentMark = input('Enter the marks by comma separated value: ')
        moreStudents = input ( 'Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, 'is already inserted')
        else:
            D[studentId] = studentMark.split(',')
            
        if moreStudents.lower() == 'no':
            return D
        
studentData = getDataFromUser()


#print(studentData)

def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
        
    return avgMarks

avgM =  getAvgMarks(studentData)

for x in avgM:
    print(('student id: ', x,'got:',avgM[x]))
