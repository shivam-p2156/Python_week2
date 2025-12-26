# Day 8 -------------->>>>>>>

# ----------- Function ------------

def add(a,b):
    print(a+b)

add(10,20)

def name(name1,name2):
    print("Hello,",name1,name2)

name("shivam","prajapati")

# Default arguments

def num(a=10,b=30):
    print(b-a)

num()
num(20,60)

# Keyword arguments

def num2(a,b):
    print(a+b)

num2(a=10,b=10)
num2(b=20,a=60)

# Required arguments

def num3(a,b):
    print((a+b)/2)

num3(20,20)

# Return statement\

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))