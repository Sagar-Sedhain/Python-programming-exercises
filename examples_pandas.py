#pandas

import pandas as pd

A = pd.Series([2,3,4,5] , index=['a','b','c','d'])
print(A.values)
print(type(A))

print(A.index)

#print(A['a'])
#print(A['a':'c'])

# pandas series
grades_dict = {'A':4,'A-':3.5,'B':3,'B-':2.5}
grades = pd.Series(grades_dict)
print(grades.values)

marks_dict = {'A':100,'A-':85,'B':80,'B-':75}
marks = pd.Series(marks_dict)
print(marks.values)
print(marks['A'])
print(marks[0:3])

#pandas data frame
print(marks)
print(grades)
D = pd.DataFrame({'Marks':marks,'Grades':grades})
print(D)
#print(D.T)
D['ScaledMarks'] = (D['Marks']/10)
print(D)
del D ['ScaledMarks']
print(D)
G = D[D['Marks']>80]
print(G)


#pandas nan
A = pd.DataFrame([{'x':1,'y':2},{'y':3,'z':4}])
print(A)
A.fillna(1)
print(A.fillna(1))

#A.dropna

B = pd.Series(['a','b','c','d'] , index= [1,3,4,5])
print(B[1:3])
print(B.loc[1:3])
print(B.iloc[1:3])