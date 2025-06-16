try:
    a = int(input("Number : "))
except:
    print("not a number")
else:
    print("it runs when no error encounterd.")
finally:
    print("runs always even error encountered or not.")

#ZeroDivisonError
#NameError 
#IndexError

import math
def square_root(number1):
    try:
        return math.sqrt(number1)
    except:
        print("Invalid input! Please enter a positive integer or a float value")
        return

square_root(-1)