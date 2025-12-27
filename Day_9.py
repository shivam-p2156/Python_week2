# Day 9 ----------->>>>>>>>>

# ---------- Lists ---------

l = [1,2,3,4,5,6,7,8,9]
l1 = [1,5,3,"Hello","Shivam",True,50.25]

print(l)
print(l1)

# Lists Index

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[5])

# Range of index

print(l1[:])  # it print elements of list from start to end 
print(l1[1:]) # it print elements of list from index 1 to end
print(l1[:6])  # it print elements of list from start to 6 index
print(l1[0:7:2])  # IT IS JUMPING INDEX it print elements of list from INDEX O TO 7 BUT TAKE THE STEP OF 2 NUMBERS 

# Methods of list 

l2 = [1,8,4,6,7,3,4,6,4,5,8,7,9,2,1]

l2.sort()
print(l2)   # sort method
l2.sort(reverse=True)      # This method reverse the list 
print(l2) 

l3 = ["print", "elements","list", "from","value"]
l3.reverse()  # reverse method
print(l3)

l4 = ["print", "elements","list", "from","value"]
print(l4.index("print"))  # index method

print(l2.count(4))   # count method 

l5 = l4.copy()   # copy method 
print(l5)

l6 = ["Hello", "Shivam", "prajapati"]
l6.append("Welcome")   # append method
print(l6)

l6.insert(2, "Good evening")    # insert method 

l5.extend(l6)  #exend method  (It join 2 list in one list )
print(l5)   
