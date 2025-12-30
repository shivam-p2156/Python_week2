# Day 10 --------------->>>>>>>>

# Tuples 

# It is simillar to a list 

tup = (0,1,2,3,4,5,6,7,8,9)
tup1 = (1,2,"shivam",True,95.05)
print(tup, type(tup))

print(tup1)

# Tuple Index

fruits = ("mango","grapes","orange","banana","litchi","guava") 
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[-1])

# Check for items using in keyword

if "mango" in fruits:
    print("yes")
else:
    print("no")

if "apple" in fruits:
    print("yes")
else:
    print("no")
    
# Range of index 

print(fruits[0:6])
print(fruits[:6])   # it print element from start to 6 index
print(fruits[1:])    # it print element from index 1 to end
print(fruits[1:6:2])    # IT IS JUMPING INDEX. it print elements from INDEX O TO 6 BUT TAKE THE STEP OF 2 NUMBERS 


# Manipulating tuples

""" The tuples is a immutable , it is do not change or alter after the creation 
 if you want to change elemnet of tuples you can convert it into list 
 and then change the elemnt then after change convert into tuples.
"""

contry = ("Russia","India","Brazil","Pakistan","Japan","England","Africa")

temp = list(contry)
temp.append("America")
temp[5] = "Nepal"
temp.pop(3)

contry = tuple(temp)

print(contry)

# Methods of tuples

t2 = (1,1,2,3,5,1,6,1,4,5,2,3)
print(t2.count(1))
print(len(t2))

# Index Methods 

print(t2.index(1))

print(t2.index(1,2,8))   # (element, start, end) indexing element 1 between index 2 to index 8

# f-string in python 

name = "shivam"
age = 19

print(f"Hello, My name is {name} and my age is {age}")

print(f"{2*60}")

print(type(f"{2*60}"))
