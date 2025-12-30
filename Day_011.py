# Day 11 -------------->>>>>>>

# --------------------Docstring--------------------------
def square(n):
    '''
    Docstring for square
    
    :param n: Description
    '''
    print(n**2)
square(5)
print(square.__doc__)   # doc attribute 

# --------------------Recursion----------------------

# Find factorial using recursive function

def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)

print(factorial(5))


# Fibonacci sequence

def fibonaci(n):
    if n<=1:
        return n
    
    return fibonaci(n-1)+fibonaci(n-2)

n = int(input("Enter number:  "))

for i in range(n):
    print(fibonaci(i))


