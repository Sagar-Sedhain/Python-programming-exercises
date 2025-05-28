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

