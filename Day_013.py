# Day 13 ----------------------->>>>>>>

# --------------------- Dictionaries -------------------

details = {"Name":"Shivam","age":19,"Region":"India"}
print(details)

# Accessing ditionary items

print(details["Name"])
print(details.get("Name"))      # get methds to print value / keys

print(details.values())         # prints all the value present in dictionary

print(details.keys())           # prints all the key present in dictionary

print(details.items())          # print all the items in key value pair

# Dictionary methods 

details.update({"Dob":2006})    # updates methods
print(details)

details.pop('age')              # pop methods
print(details)

details.popitem()               # popitem methods
print(details)

details.clear()                 # clear methods
print(details)

del details                     # del methods
# print(details)   # it give name error because details are deleted 



# --------------------- Else in loop --------------------

for i in range(5):
    print(i)
else:
    print("loop closed")     # here else loop execute because loop completly run

# ---------------------

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("loop closed")     # here else loop do not execute because loop break 
    