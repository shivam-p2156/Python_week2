# Day 14 ------------------------------->>>>>>>

#  --------------------------- Excaption handling -----------------------------

try:
    num = int(input("Enter an integer: "))
    a = [6, 3,5,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

# Finally clause

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


# Raising Custom errors

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 