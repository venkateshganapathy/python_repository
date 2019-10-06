"""function basics

"""

#using recursion
"""
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

m = 6
print(fibonacci(m))

import sys
print(sys.getrecursionlimit())
"""

def fibo(n):
    fibo_current = 0
    for _ in range(n+1):
        fibo_current += _
    return fibo_current

while True:
   input_value = int(input("Dear user, please enter value for which you want to calculate fibonacci value or enter -1 to exit: "))
   print(fibo(input_value))
   if input_value == -1:
       break
