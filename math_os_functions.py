"""math library and OS library

"""

import math
print("math.sin(1) ", math.sin(1))

print("math.factorial(5) ", math.factorial(5))

print("math.ceil(4.5) ", math.ceil(4.5))
print("math.ceil(4.4) ", math.ceil(4.4))

print("math.pi ", math.pi)


import os
print(os.getenv('HOME'))
print(os.getcwd())
print(os.system('uname -a'))  #issue a system command

import platform #the platform module provides access to identification information for the system on which python is running
print(platform.architecture())
print(platform.machine())
print(platform.system())
print(platform.uname())
print(platform.platform())

import sys
#this module gives access some Python interpreter variables and to certain functions that are closely-aligned with the interpreters'
print(sys.platform)
print(sys.argv)
print(sys.maxsize)
print(sys.builtin_module_names)
print(sys.modules)
